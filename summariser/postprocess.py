import re

def clean_summary(text: str) -> str:
    """Strip markdown artefacts and normalise whitespace."""
    text = re.sub(r"#{1,6}\s*", "", text)
    text = re.sub(r"\*{1,2}([^*]+)\*{1,2}", r"", text)
    text = re.sub(r"
{3,}", "

", text)
    return text.strip()

def extract_action_items(summary: str) -> list[str]:
    lines = summary.splitlines()
    return [l.strip().lstrip("-•* ") for l in lines
            if any(kw in l.lower() for kw in ("action", "follow up", "owner", "deadline", "will "))]
