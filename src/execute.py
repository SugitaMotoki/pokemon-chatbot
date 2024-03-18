from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from constants import Data
from ai.model import get_model
from ai.retrievers import get_retriever
from ai.prompts import prompt

model = get_model()
document_chain = create_stuff_documents_chain(model, prompt)
retriever = get_retriever(Data.POKEMON)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({
  "input": "図鑑番号30番のポケモンの名前は？",
})

print(response["context"])
print(response["answer"])
