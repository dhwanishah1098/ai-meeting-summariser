def summarise_week(meetings: list[dict]) -> dict:
    all_actions = [a for m in meetings for a in m.get('action_items',[])]
    all_decisions = [d for m in meetings for d in m.get('decisions',[])]
    topics = {t for m in meetings for t in m.get('topics',[])}
    return {'meetings': len(meetings), 'action_items': len(all_actions), 'decisions': len(all_decisions), 'topics': list(topics)}
