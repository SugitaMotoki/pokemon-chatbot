from os.path import join, dirname, isfile

import sys
sys.path.append(join(dirname(__file__), ".."))
from constants import Data

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_pokemon_documents():
    csv_path = join(dirname(__file__), "..", "data", "pokemon", "pokemon.csv")
    loader=CSVLoader(file_path=csv_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n\n",
        chunk_size=100,
        chunk_overlap=10,
    )

    return text_splitter.split_documents(docs)

def get_movie_documents():
    url = "https://w.wiki/4hmn"
    loader = WebBaseLoader(url)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n\n",
        chunk_size=100,
        chunk_overlap=10,
    )

    return text_splitter.split_documents(docs)

def get_documents(data: Data):
    match data:
        case Data.POKEMON:
            return get_pokemon_documents()
        case Data.MOVIE:
            return get_movie_documents()
        case _:
            raise ValueError("unknown data")

if __name__ == "__main__":
    docs = get_documents(Data.POKEMON)
    print(docs)
    pass
