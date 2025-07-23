def extract_owners(action_items: list[str]) -> list[dict]:
    import re
    result = []
    for item in action_items:
        owner = re.search(r'@(\w+)', item)
        result.append({'item': item, 'owner': owner.group(1) if owner else 'TBD'})
    return result
