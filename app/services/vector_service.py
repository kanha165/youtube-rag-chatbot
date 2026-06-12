import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="youtube_rag"
)


def store_chunks(video_id, chunks):

    if not chunks:
        raise ValueError(
            f"No chunks generated for video {video_id}"
        )

    ids = [
        f"{video_id}_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=[
            {"video_id": video_id}
            for _ in chunks
        ]
    )

    return True


def search_chunks(
        query,
        video_id,
        n_results=5
):

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={
            "video_id": video_id
        }
    )

    return results


def get_context(
        query,
        video_id
):

    results = search_chunks(
        query,
        video_id
    )

    documents = results[
        "documents"
    ][0]

    context = "\n".join(
        documents
    )

    return context



import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="youtube_rag"
)

# NEW FUNCTION
def video_exists(video_id):

    results = collection.get(
        where={
            "video_id": video_id
        }
    )

    return len(results["ids"]) > 0