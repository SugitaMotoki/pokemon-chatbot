from langchain_openai import ChatOpenAI

def get_model(
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0
    ):
    return ChatOpenAI(
        model=model_name,
        temperature=temperature
    )
