# AI Intent Router Service

This project implements an intent-based routing system for AI assistants.

Features:
- Intent classification
- Persona-based routing
- Structured JSON responses
- Error handling
- Logging with JSONL
- Confidence threshold
- Manual override support

Architecture:

User Message
      ↓
Intent Classifier
      ↓
Intent JSON
      ↓
Router
      ↓
Expert Persona
      ↓
Final Response
      ↓
Logged to route_log.jsonl