from conversor import *
import os

def menu():
    while True:
        print("\n--- CONVERSOR DE MOEDAS ---")
        print("1 - Real para Dólar")
        print("2 - Real para Euro")
        print("3 - Ver histórico")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Valor em reais: "))
            print(real_para_dolar(valor))

        elif opcao == "2":
            valor = float(input("Valor em reais: "))
            print(real_para_euro(valor))

        elif opcao == "3":
            for h in mostrar_historico():
                print(h)

        elif opcao == "0":
            print("Saindo...")
            break
            
        print("Teste CI")

if __name__ == "__main__":
    if os.getenv("CI"):
        print("Executando no CI com sucesso!")
    else:
        menu()