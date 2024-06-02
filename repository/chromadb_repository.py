import chromadb

class chromaDbRepository:

    currentId = 1

    def create_collection(self, collection_name="DefautDatabaseCollection"):
        chroma_client = chromadb.Client()
        return chroma_client.get_or_create_collection(name=collection_name)

    def add_document(self, collection, list_of_documents):

        ids = []
        idCount = 0
        for document in list_of_documents:
            ids.append("id" + str(idCount))
            idCount += 1

        collection.add(
            documents=list_of_documents,
            ids=ids
        )
        return True

    def query(self, collection, query_text, num_results):
        if collection is None:
            print("missing collection")
            return False

        return collection.query(
            query_texts=[query_text],  # Chroma will embed this for you
            n_results=num_results  # how many results to return
        )


db = chromaDbRepository
default_collection = db.create_collection()

db.add_document(
    collection=default_collection,
    list_of_documents=["test doc1", "test doc2", "test doc3", "Test 1"])

result = db.query(
    collection=default_collection,
    query_text="test 1",
    num_results=2
)

print("Result:", result)
