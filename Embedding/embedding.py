from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
embeddings = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2"
                                   )
texts = ["This is a test document.", "This is another test document."]
vector = embeddings.embed_query(texts)
print(str(vector))