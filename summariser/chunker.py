def chunk_transcript(text, max_tokens=3000):
    words = text.split()
    chunks, buf = [], []
    for w in words:
        buf.append(w)
        if len(' '.join(buf)) > max_tokens * 4:
            chunks.append(' '.join(buf))
            buf = []
    if buf: chunks.append(' '.join(buf))
    return chunks
