import chromadb

class chromaDbRepository:

    currentId = 1

    def create_collection(collection_name = "DefautDatabaseCollection"):
        chroma_client = chromadb.Client()
        return chroma_client.create_collection(name=collection_name)

    def add_document(collection, list_of_documents):

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

    def query(collection, query_text, num_results):
        if collection is None:
            print("missing collection")
            return False

        return collection.query(
            query_texts=[query_text],  # Chroma will embed this for you
            n_results=num_results  # how many results to return
        )

