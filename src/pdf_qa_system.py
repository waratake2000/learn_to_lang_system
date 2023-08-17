import json
import os

with open("./apikey.json") as f:
    json_file = json.load(f)
os.environ["OPENAI_API_KEY"] = json_file["apikey"]
print(json_file["apikey"])


from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter

from langchain.document_loaders import UnstructuredURLLoader

urls = [
    "https://zenn.dev/umi_mori/articles/what-is-gpt-4", # GPT-4とは？【概要と使い方 / GPT-3.5と比較 / ChatGPTでの使用方法】
    "https://zenn.dev/umi_mori/articles/chatgpt-api-python", # ChatGPT APIの「概要と使い方」（Pythonコード付き）
    "https://zenn.dev/umi_mori/articles/chatgpt-google-chrome-plugins" # ChatGPTの便利プラグイン7選【Google Chrome拡張機能】
]

loader = UnstructuredURLLoader(urls=urls)
# print(loader.load())

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 300,
    chunk_overlap = 0,
    length_function = len,
)

index = VectorstoreIndexCreator(
    vectorstore_cls=Chroma, # Default
    embedding=OpenAIEmbeddings(), # Default
    text_splitter=text_splitter,
).from_loaders([loader])

query = "7番目に紹介しているChatGPT便利プラグインは？"

answer = index.query(query)
print(answer)
