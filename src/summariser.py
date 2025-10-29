"""LLM-based summarisation and action item extraction."""
import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SUMMARY_PROMPT = """
You are a professional meeting analyst. Given the following meeting transcript, produce:
1. A concise executive summary (3-5 sentences)
2. Key discussion points (bullet list)
3. Decisions made
4. Action items in JSON format: [{{"task": "...", "owner": "...", "deadline": "..."}}]

Transcript:
{transcript}

Respond in this exact JSON structure:
{{
  "summary": "...",
  "key_points": ["...", "..."],
  "decisions": ["...", "..."],
  "action_items": [{{"task": "...", "owner": "...", "deadline": "..."}}]
}}
"""

def summarise(transcript: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": SUMMARY_PROMPT.format(transcript=transcript)}],
        temperature=0.2,
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
