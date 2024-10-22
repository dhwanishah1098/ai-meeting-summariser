def format_summary_email(summary: dict) -> str:
    lines = [f"Meeting: {summary['title']}", f"Date: {summary['date']}", '']
    lines += ['Key Decisions:', *[f'  - {d}' for d in summary.get('decisions', [])]]
    lines += ['', 'Action Items:', *[f'  - {a}' for a in summary.get('actions', [])]]
    return '\n'.join(lines)
