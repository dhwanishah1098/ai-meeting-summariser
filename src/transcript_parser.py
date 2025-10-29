"""Parse transcripts from various meeting platforms."""
import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class Turn:
    speaker: str
    timestamp: Optional[str]
    text: str

def parse_zoom(raw: str) -> list[Turn]:
    """Parse Zoom auto-generated transcript format."""
    turns = []
    pattern = re.compile(r'^(\d{2}:\d{2}:\d{2})\s+(.+?)\n(.+?)(?=\n\d{2}:\d{2}:\d{2}|\Z)', re.MULTILINE | re.DOTALL)
    for m in pattern.finditer(raw):
        turns.append(Turn(speaker=m.group(2).strip(), timestamp=m.group(1), text=m.group(3).strip()))
    return turns

def parse_plain(raw: str) -> list[Turn]:
    """Parse plain speaker: text format."""
    turns = []
    for line in raw.strip().splitlines():
        if ':' in line:
            speaker, _, text = line.partition(':')
            turns.append(Turn(speaker=speaker.strip(), timestamp=None, text=text.strip()))
    return turns

def turns_to_text(turns: list[Turn]) -> str:
    return '\n'.join(f"{t.speaker}: {t.text}" for t in turns)
