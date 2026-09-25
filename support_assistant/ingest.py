"""Load support Markdown files, split them into chunks, and store them in ChromaDB."""

from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "support_knowledge"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120


def split_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks, preferring word boundaries."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be between zero and chunk_size - 1")

    text = " ".join(text.split())
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            boundary = text.rfind(" ", start + chunk_size // 2, end)
            if boundary > start:
                end = boundary
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = max(start + 1, end - overlap)
    return chunks


def ingest_documents() -> int:
    """Embed Markdown files under data/ and upsert their chunks into ChromaDB.

    Existing chunks for each source are removed before adding its current version,
    so rerunning this script updates changed documents without stale chunks.
    Returns the number of chunks stored.
    """
    files = sorted(DATA_DIR.rglob("*.md"))
    if not files:
        raise FileNotFoundError(f"No Markdown support documents found in {DATA_DIR}")

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    embedding_function = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"},
    )

    total_chunks = 0
    for file_path in files:
        source = file_path.relative_to(DATA_DIR).as_posix()
        content = file_path.read_text(encoding="utf-8").strip()
        chunks = split_text(content)
        collection.delete(where={"source": source})
        if not chunks:
            print(f"Skipped empty document: {source}")
            continue

        ids = [f"{source}::chunk-{index}" for index in range(len(chunks))]
        metadatas = [{"source": source, "chunk_index": index} for index in range(len(chunks))]
        collection.upsert(ids=ids, documents=chunks, metadatas=metadatas)
        total_chunks += len(chunks)
        print(f"Ingested {len(chunks)} chunk(s): {source}")

    print(
        f"Done. Stored {total_chunks} chunk(s) from {len(files)} document(s) "
        f"in '{COLLECTION_NAME}' at {CHROMA_DIR}."
    )
    return total_chunks


if __name__ == "__main__":
    ingest_documents()
