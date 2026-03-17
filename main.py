from processamento import (
    notas_alunos,
    executar_processamento,
    gerar_relatorio
)

def adicionar_aluno(lista):
    nome = input("\nNome do aluno: ")

    notas = []
    while True:
        entrada = input("Digite uma nota (ou 'fim'): ")
        if entrada.lower() == "fim":
            break

        notas.append(entrada) 

    lista.append((nome, notas))  
    print("Aluno adicionado!")


def main():
    dados = list(notas_alunos)  

    resultados = None

    while True:
        print("\n=== SISTEMA DE NOTAS ===")
        print("1 - Ver alunos cadastrados")
        print("2 - Adicionar aluno")
        print("3 - Processar dados")
        print("4 - Ver resultados")
        print("5 - Gerar relatório")
        print("6 - Sair")

        op = input("Escolha: ")

        if op == "1":
            print("\n=== ALUNOS ===")
            for nome, notas in dados:
                print(f"{nome}: {notas}")

        elif op == "2":
            adicionar_aluno(dados)

        elif op == "3":
            try:
                resultados = executar_processamento(dados)
                print("Processamento concluído!")
            except Exception as e:
                print(f"Erro: {e}")

        elif op == "4":
            if not resultados:
                print("Processe os dados!")
                continue

            res, rec, top, nota = resultados

            print("\n=== RESULTADOS ===")
            for nome, media in res:
                status = "Recuperação" if media < 7 else "Aprovado"
                print(f"{nome}: {media:.2f} ({status})")

            print(f"\nTop Student: {top} ({nota:.2f})")

        elif op == "5":
            if not resultados:
                print("Processe antes!")
                continue

            res, rec, top, nota = resultados
            gerar_relatorio(res, rec, top, nota)
            print("Relatório gerado com sucesso!!")

        elif op == "6":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")
if __name__ == "__main__":
    main()