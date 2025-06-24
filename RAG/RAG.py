import langchain
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv, find_dotenv
import os
import bs4

# Reading the models.
# api_key = load_dotenv(find_dotenv(''))
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Collecting Data From Internet. 
WebBaseLoader(
    web_path = ("http://lilianweng.github.io/posts/2023-06-23-agent/"),
    bs_kwargs = dict(
        parse_only = bs4.SoupStrainer(
            class = ("post-content", "post-title", "post-header")
        )
    ),

)

loader.load()