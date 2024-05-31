
import anthropic

from data import alpha_vantage_service
from data import chromadb_repository

#https://docs.anthropic.com/claude/docs/quickstart-guide

davids_key = "sk-ant-api03-XPu...DAAA"
govindas_key = ""
sindhus_key = ""
jirens_key = ""

# client = anthropic.Anthropic(
#     api_key = davids_key #REPLACE WITH YOUR KEY
# )
#
# message = client.messages.create(
#     model="claude-3-opus-20240229",
#     max_tokens=1000,
#     temperature=0.0,
#     system="Respond only in Yoda-speak.",
#     messages=[
#         {"role": "user", "content": "How are you today?"}
#     ]
# )
#
# print(message.content)

# tesla_data = alpha_vantage_service.get_overview("TSLA")
# print(tesla_data)

db = chromadb_repository.chromaDbRepository
default_collection = db.create_collection()

db.add_document(
    collection=default_collection,
    list_of_documents=["test doc1", "test doc2", "test doc3"])

result = db.query(
    collection=default_collection,
    query_text="test 1",
    num_results=2
)

print("Result:", result)