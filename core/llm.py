from dotenv import load_dotenv
from groq import Groq
from crud.repository import Database_search
import os


load_dotenv()


if not os.getenv("GROQ_API_KEY"):
    print("ERRO: GROQ_API_KEY não encontrada no arquivo .env.")
    print("Crie um arquivo .env na raiz com: GROQ_API_KEY=sua_chave")
    exit(1)

client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

SYSTEM_PROMPT = """
Você é um analista sênior de um Security Operations Center (SOC). Sua tarefa é analisar logs de sistema e devolver de forma exata e precisa as informações solicitadas.

DIRETRIZES ABSOLUTAS:
1. Responda de forma direta, técnica e profissional.
2. Baseie sua resposta EXCLUSIVAMENTE na seção [CONTEXTO DE LOGS] fornecida abaixo.
3. Em hipótese alguma invente informações, IPs, portas ou ações.
4. Se a informação não estiver no contexto, responda APENAS: "Não encontrei essa informação nos logs fornecidos."

[CONTEXTO DE LOGS]
{contexto}

"""
def consultar_assistente(pergunta_usuario: str):
    resultados = Database_search(pergunta_usuario)

    logs_recuperados = "\n".join(resultados['documents'][0])

    prompt_final = SYSTEM_PROMPT.format(contexto=logs_recuperados)

    chat_completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
         messages=[
            {
                "role": "system",
                "content": prompt_final
            },
            {
                "role": "user",
                "content": pergunta_usuario # Aqui entra a pergunta crua que o usuário digitou
            }
        ],
        temperature=0.0 # Temperatura zero para impedir alucinações criativas
    )

    return chat_completion.choices[0].message.content
