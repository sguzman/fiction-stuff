# Transcription Process Guide

This document outlines the standard procedure for taking a raw narrative text (like a short story or a book chapter) and transcribing it into the structured TOML ontology format used by this repository.

## The Pipeline

The process consists of the following steps:

1. **Source Ingestion:** Obtain the source text in a plain text (`.txt`) or markdown (`.md`) format.
2. **Schema Reference:** Ensure the target output adheres to the JSON schemas defined in `docs/schema/`.
3. **Automated Extraction:** Use the `scripts/transcribe.py` tool to parse the text. This tool utilizes a Large Language Model (LLM) to identify entities, rules, and narrative checkpoints.
4. **Manual Review & Curation:** The LLM output is not always perfect. After generation, review the created `.toml` files in `data/examples/<book_name>` to ensure character traits, relations, and plot points are captured accurately.
5. **Schema Validation:** Ensure the final files pass JSON Schema validation.

## Running the Automated Script

The primary way to transcribe a text is via the `transcribe.py` script. 

### Prerequisites
- Install dependencies: `pip install -r scripts/requirements.txt`
- Set your API key for the corresponding LLM (e.g., `GEMINI_API_KEY` or `OPENAI_API_KEY`, depending on the active script configuration).

### Execution

```bash
python scripts/transcribe.py --input path/to/story.txt --story-name "story_slug"
```

This will automatically create a directory under `data/examples/story_slug/` with the populated subdirectories:
- `agents_and_entities/`
- `dynamics_and_rules/`
- `narrative_state/`
- `world_and_lore/`

## Hybrid / Manual Approach

If you prefer to transcribe incrementally using an AI assistant (like me):
1. **Prompting:** Ask the assistant to "Extract the main characters from this text based on `docs/schema/agents_and_entities/character_main.schema.json` and output them as TOML."
2. **Copy/Paste:** Save the assistant's output to the corresponding folder under `data/examples/<your_story>/agents_and_entities/`.
3. **Iterate:** Repeat for `world_and_lore`, `dynamics_and_rules`, and `narrative_state`.
