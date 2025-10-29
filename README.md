# AI Meeting Summariser

Automatically convert meeting transcripts or audio into structured summaries and action item lists using LLMs.

## Features
- Transcript → structured summary
- Action item extraction with owner + deadline
- Slack / email delivery of summary
- Supports Zoom, Teams, Google Meet transcript formats

## Quick Start
```bash
pip install -r requirements.txt
python summarise.py --transcript meeting.txt --output summary.md
```
