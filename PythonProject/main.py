import requests
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

# ======================
# Supabase
# ======================

SUPABASE_URL = os.getenv("https://gqguqdjjikwryraiovbg.supabase.co")
SUPABASE_KEY = os.getenv("sb_publishable_y16KZFuk6zMgatlIN40WzA_vcoiWP45")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

URL_ZAPI = (
    f"https://api.z-api.io/instances/"
    f"{INSTANCE_ID}/token/{TOKEN}/send-text"
)

HEADERS = {
    "Client-Token": CLIENT_TOKEN,
    "Content-Type": "application/json"
}

response = (
    supabase
    .table("contatos")
    .select("*")
    .limit(3)
    .execute()
)

contatos = response.data

for contato in contatos:

    nome = contato["nome"]
    telefone = contato["telefone"]

    mensagem = (
        f"Olá, {nome} tudo bem com você?"
    )

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    resposta = requests.post(
        URL_ZAPI,
        json=payload,
        headers=HEADERS
    )

    print(
        f"Mensagem enviada para "
        f"{nome}: {resposta.status_code}"
    )