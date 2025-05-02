TOPICS = ['budget','timeline','risk','decision','action','blocker','milestone']
def detect_topics(text: str) -> list[str]:
    lower = text.lower()
    return [t for t in TOPICS if t in lower]
