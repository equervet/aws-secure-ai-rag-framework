# Level 0: Prompt-Based LLM Demo

## Purpose

This example is the Level 0 teaching demo. It demonstrates grounded prompting rather than RAG because it has no retrieval step.

- No S3 knowledge bucket
- No retrieval step
- Fixed, curated knowledge included in Lambda prompt construction
- API Gateway and Bedrock still demonstrate the core request flow

## Files

- Lambda reference implementation: [src/handler.py](src/handler.py)
- CloudFormation template: [../../templates/cloudformation/level-0-llm-prompt-demo.yaml](../../templates/cloudformation/level-0-llm-prompt-demo.yaml)

## Notes

- Use this for teaching and first demos, not as a secure production pattern.
- The S3-backed Level 1 starter is the first actual RAG architecture in the framework.
