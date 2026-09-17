# AWS Secure AI RAG Framework

[![ShellCheck](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/shellcheck.yml/badge.svg)](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/shellcheck.yml)
[![PSScriptAnalyzer](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/psscriptanalyzer.yml/badge.svg)](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/psscriptanalyzer.yml)
[![CodeQL](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/codeql.yml/badge.svg)](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/codeql.yml)
[![Semgrep](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/semgrep.yml/badge.svg)](https://github.com/equervet/aws-secure-ai-rag-framework/actions/workflows/semgrep.yml)

Explore the full documentation with a better UI on the GitHub Pages-hosted [documentation site](https://equervet.github.io/aws-secure-ai-rag-framework/).

Open-source guidance for building secure AI and retrieval-augmented generation solutions with a practical AWS implementation path, level-based architecture guidance, infrastructure templates, and deployment guidance.

This project is AWS-first where security controls need concrete examples, but it aims to stay cloud-aware and portable at the design level whenever possible.

## Who This Is For

- Teams that want secure RAG patterns without starting from a blank page.
- Departments that need a simple path from proof of concept to enterprise controls.
- Platform, cloud, security, and application teams working at different maturity levels.

## Framework Model

The framework has **three maturity levels plus a Level 0 teaching demo**. Readers can start at the level that matches their operational needs and apply profiles for requirements that cut across maturity.

### Level 0: Prompt-Based LLM Demo

The simplest teaching path stores fixed knowledge in Lambda (no RAG storage). Level 0 shows grounded prompting, not RAG, because there's no step to retrieve document knowledge.

See [docs/levels/level-0-llm-prompt-demo.md](docs/levels/level-0-llm-prompt-demo.md)

### Level 1: Starter

Simple, low-cost AWS RAG sample app with **S3-backed knowledge**, **lightweight retrieval**, and a **deployable built-in web client**.

> 🚧 **Coming soon** — content for this section is in progress.

### Level 2: Foundation

Production-oriented baseline for a single team or department with stronger security, operations, and deployment discipline.

> 🚧 **Coming soon** — content for this section is in progress.

### Level 3: Enterprise

Multi-team, multi-environment, governed RAG platform patterns for larger organizations.

> 🚧 **Coming soon** — content for this section is in progress.

## Cross-Cutting Profiles

Profiles add requirements to a maturity-level architecture; they are not later maturity stages.

### Regulated Profile

Private networking, strict data boundaries, auditability, residency, and compliance controls, typically applied to Level 2 or Level 3.

> 🚧 **Coming soon** — content for this section is in progress.

### Portable Profile

Cloud-agnostic mapping of the core patterns across providers while keeping AWS implementations as the most complete reference.

> 🚧 **Coming soon** — content for this section is in progress.

## Capability Matrix

> 🚧 **Coming soon** — content for this section is in progress.

## Design Principles

- Security by default, not as an optional hardening step.
- Retrieval quality and data governance are equally important.
- Start simple, then add controls in clear increments.
- Prefer managed services when they reduce operational risk.
- Keep architecture patterns portable even when implementation assets are AWS-specific.

## Planned Content Types

- Level guides with embedded architecture diagrams
- CloudFormation templates
- Security control mappings
- Implementation playbooks
- Decision guides by maturity level
- Example applications and sample datasets

## Suggested Starting Point

> 🚧 **Coming soon** — content for this section is in progress.

## Current Status

This repository is in the initial documentation and structure phase. Each maturity level is intended to have **one level document** in [docs/levels](docs/levels) and **one deployment guide** in [docs/guides](docs/guides), with the architecture explanation kept inside the level page. Level 1 currently centers on a low-cost AWS RAG sample that can be deployed, understood, and extended. The Level 0 prompt-based LLM demo provides a smaller introduction to grounded prompting before retrieval, while Levels 2 and 3 describe the path to production and enterprise operation.
