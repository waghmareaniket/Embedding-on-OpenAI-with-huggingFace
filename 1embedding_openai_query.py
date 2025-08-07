from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32) #dim is (vector)matrics want
result=embedding.embed_query('Delhi is capital of India')
print(result)