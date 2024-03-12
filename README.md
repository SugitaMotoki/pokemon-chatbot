# Pokemon Chatbot

## 実行手順

### Clone

```bash
git clone git@github.com:SugitaMotoki/pokemon-chatbot.git
```
```bash
cd pokemon_chatbot
```

### Python

```bash
python3.11 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

### Streamlit

```bash
mkdir .streamlit
```
```bash
echo "OPENAI_API_KEY = \"[YOUR_API_KEY]\"" > .streamlit/secrets.toml
```
```bash
streamlit run pokemon_chatbot/streamlit.py
```