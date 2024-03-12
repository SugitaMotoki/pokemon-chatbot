from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.tools.retriever import create_retriever_tool
from .embeddings import embeddings

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders.csv_loader import CSVLoader


def create_retriever_tool_wrapper(
        loader: BaseLoader,
        name: str,
        description: str,
    ):

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)

    vector = FAISS.from_documents(documents, embeddings)
    retriever = vector.as_retriever()

    return create_retriever_tool(
        retriever,
        name,
        description,
    )


movie_loader = WebBaseLoader("https://w.wiki/4hmn")
movie_retriever_tool = create_retriever_tool_wrapper(
    loader=movie_loader,
    name="movie_search",
    description="劇場版ポケットモンスターのWikipedia内を検索します",
)


pokemon_loader=CSVLoader(file_path="pokemon_chatbot/data/pokemon.csv")
pokemon_retriever_tool = create_retriever_tool_wrapper(
    loader=pokemon_loader,
    name="pokemon_search",
    description="ポケモンのデータをCSVから検索します",
)
