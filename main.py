#!/usr/bin/env python3
from core import llm


def iniciar_cli():
    while True:
        try:
            pergunta = input("\n[ANALISTA SOC] > ")
            if pergunta.lower().strip() in ['sair', 'exit', 'quit']:
                print("\nEncerrando o assistente")
                break
            if not pergunta.strip():
                continue

            print("\n Analisando o Banco Vetorial...")
            resposta = llm.consultar_assistente(pergunta)

            print(f"\n[ASSISTENTE SOC]\n{resposta}\n")
            print("-"*60)
        except KeyboardInterrupt:
            # Captura o Ctrl+C para sair de forma elegante sem cuspir erro na tela
            print("\n\nOperação cancelada pelo usuário. Encerrando...")
            break
        except Exception as e:
            print(f"\n[ERRO DE SISTEMA]: {e}")

if __name__ == "__main__":
    iniciar_cli()
