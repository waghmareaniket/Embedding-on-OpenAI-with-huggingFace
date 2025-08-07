from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32) #dim is (vector)matrics want
documents=[
    " delhi is capital of india",
    "paris is capital of France"
]

result=embedding.embed_documents(documents)
print(result)