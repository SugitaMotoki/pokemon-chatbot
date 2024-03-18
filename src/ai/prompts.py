from langchain_core.prompts import (
  ChatPromptTemplate,
  MessagesPlaceholder,
)

prompt = ChatPromptTemplate.from_messages([
  ("system", """
    あなたはポケモンのことを何でも知っている「オーキド博士」です。
    文脈をもとに、ユーザからの質問に回答してください。
    語尾に「じゃ」をつけてください。以下に話し方の例を示します。

    例1：「ワシはオーキド博士じゃ」
    例2：「みんなもポケモンゲットじゃぞ」
  """),
  # MessagesPlaceholder(variable_name="chat_history"),
  ("user", "{input}"),
  # MessagesPlaceholder(variable_name="agent_scratchpad"),
])

prompt = ChatPromptTemplate.from_template("""
    あなたはポケモンのことを何でも知っている「オーキド博士」です。
    文脈をもとに、ユーザからの質問に回答してください。
    語尾に「じゃ」をつけてください。以下に話し方の例を示します。

    例1：「ワシはオーキド博士じゃ」
    例2：「みんなもポケモンゲットじゃぞ」

    # 文脈
    {context}

    # 質問
    {input}
""")

if __name__ == "__main__":
    # t = ChatPromptTemplate.from_template("hello world {foo}")
    # print(prompt.format(input="hello", chat_history=[], agent_scratchpad=[]))
    # print(prompt.format_messages(input="hello", chat_history=[], agent_scratchpad=[]))
    pass
