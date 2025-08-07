from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model="Xenova/all-MiniLM-L6-v2")
text='delhi is capital of india'
vector=embedding.embed_query(text)
print(str(vector))