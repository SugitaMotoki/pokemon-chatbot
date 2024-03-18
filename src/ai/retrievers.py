from os.path import join, dirname, isdir

import sys
sys.path.append(join(dirname(__file__), ".."))
from constants import Data

from langchain.vectorstores.faiss import FAISS
from .embedding import get_embedding
from .documents import get_documents


def get_vector_db(data: Data):
    embedding = get_embedding()

    db_path = join(data.dir_path, "vector_db")

    if isdir(db_path):
        return FAISS.load_local(db_path, embeddings=embedding, allow_dangerous_deserialization=True)
    else:
        documents = get_documents(data)
        vector_db = FAISS.from_documents(documents, embedding)
        vector_db.save_local(db_path)
        return vector_db
    

def get_retriever(data: Data):
    vector_db = get_vector_db(data)
    return vector_db.as_retriever()


if __name__ == "__main__":
    pass