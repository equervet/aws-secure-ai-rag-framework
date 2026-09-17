import json
import os

import boto3


bedrock_client = boto3.client("bedrock-runtime")

BEDROCK_MODEL_ID = os.environ["BEDROCK_MODEL_ID"]

PROMPT_CONTEXT = """
Level 1 security defaults include least-privilege IAM, encryption at rest, CloudWatch logging, curated knowledge sources, and no hardcoded secrets.

The main Level 1 architecture uses API Gateway, Lambda, S3, and Amazon Bedrock.

The prompt-based LLM demo is intended only for teaching because it has no retrieval step and knowledge updates require redeployment.
""".strip()

HTML_PAGE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Level 0 Prompt-Based LLM Demo</title>
  <style>
    body { font-family: Georgia, serif; margin: 0; padding: 32px; background: #f4efe3; color: #1e2a2f; }
    main { max-width: 840px; margin: 0 auto; background: #fffdf8; border: 1px solid #d9d1c3; border-radius: 16px; padding: 24px; }
    textarea, button { width: 100%; font: inherit; }
    textarea { min-height: 140px; padding: 12px; margin: 8px 0 16px; border: 1px solid #d9d1c3; border-radius: 10px; box-sizing: border-box; }
    button { padding: 12px 16px; border: 0; border-radius: 999px; background: #8a5a2b; color: white; font-weight: 700; cursor: pointer; }
    .answer { margin-top: 20px; padding: 16px; background: #fcfaf4; border: 1px solid #d9d1c3; border-radius: 12px; white-space: pre-wrap; }
  </style>
</head>
<body>
  <main>
    <p>Prompt-based LLM demo variant</p>
    <h1>Level 0 Prompt-Based LLM Demo</h1>
    <textarea id=\"question\" placeholder=\"Why is this demo not considered RAG?\"></textarea>
    <button id=\"submit\" type=\"button\">Ask</button>
    <p id=\"status\"></p>
    <div id=\"answer\" class=\"answer\" hidden></div>
  </main>
  <script>
    const submitButton = document.getElementById('submit');
    const questionInput = document.getElementById('question');
    const statusNode = document.getElementById('status');
    const answerNode = document.getElementById('answer');

    submitButton.addEventListener('click', async () => {
      const question = questionInput.value.trim();
      answerNode.hidden = true;

      if (!question) {
        statusNode.textContent = 'Enter a question.';
        return;
      }

      submitButton.disabled = true;
      statusNode.textContent = 'Querying the prompt-based LLM demo...';

      try {
        const response = await fetch('/ask', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question })
        });
        const payload = await response.json();

        if (!response.ok) {
          throw new Error(payload.message || 'Request failed.');
        }

        answerNode.textContent = payload.answer || 'No answer returned.';
        answerNode.hidden = false;
        statusNode.textContent = 'Request completed.';
      } catch (error) {
        statusNode.textContent = error.message;
      } finally {
        submitButton.disabled = false;
      }
    });
  </script>
</body>
</html>
"""


def build_prompt(question):
    return (
        "You are a secure AWS starter assistant. Use only the provided prompt context. "
        "If the answer is not present, say the prompt-based LLM demo does not contain it.\n\n"
        f"Prompt context:\n{PROMPT_CONTEXT}\n\n"
        f"Question: {question}\n\n"
        "Answer concisely."
    )


def invoke_bedrock(prompt):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ]
    }
    response = bedrock_client.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        body=json.dumps(payload),
        contentType="application/json",
        accept="application/json",
    )
    response_body = json.loads(response["body"].read())
    content = response_body.get("output", {}).get("message", {}).get("content", [])

    if content and isinstance(content, list):
        text_parts = [entry.get("text", "") for entry in content if isinstance(entry, dict)]
        return "\n".join(part for part in text_parts if part).strip()

    return "No response text returned by the model."


def html_response():
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html; charset=utf-8"},
        "body": HTML_PAGE,
    }


def handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "")
    path = event.get("rawPath", "")

    if method == "GET" and path == "/":
        return html_response()

    if method != "POST" or path != "/ask":
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Not found"}),
        }

    request_body = json.loads(event.get("body") or "{}")
    question = (request_body.get("question") or "").strip()

    if not question:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "question is required"}),
        }

    answer = invoke_bedrock(build_prompt(question))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "answer": answer,
                "variant": "llm-prompt-demo",
            }
        ),
    }
