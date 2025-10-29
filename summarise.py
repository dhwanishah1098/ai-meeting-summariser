"""CLI: python summarise.py --transcript meeting.txt --output summary.md"""
import argparse, json, sys
from pathlib import Path
from src.transcript_parser import parse_plain, turns_to_text
from src.summariser import summarise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--output", default="summary.md")
    args = parser.parse_args()

    raw = Path(args.transcript).read_text(encoding="utf-8")
    turns = parse_plain(raw)
    text = turns_to_text(turns)
    result = summarise(text)

    md = f"# Meeting Summary\n\n## Summary\n{result['summary']}\n\n"
    md += "## Key Points\n" + '\n'.join(f"- {p}" for p in result['key_points']) + "\n\n"
    md += "## Decisions\n" + '\n'.join(f"- {d}" for d in result['decisions']) + "\n\n"
    md += "## Action Items\n| Task | Owner | Deadline |\n|---|---|---|\n"
    for item in result['action_items']:
        md += f"| {item['task']} | {item['owner']} | {item['deadline']} |\n"

    Path(args.output).write_text(md)
    print(f"Summary written to {args.output}")

if __name__ == "__main__":
    main()
