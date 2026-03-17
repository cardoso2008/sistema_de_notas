notas_alunos = [("Guilherme", [10, 9.5, 6.5, 10, 5.5, 8],
                 "Lucas", [9, 6.5, -50, 6, 10, 8],
                 "Otávio", [6, 5.5, 38, 2, 0, 4.5],
                 "Rodrigo", [7, 9.5, 8, 9.0, 6, 10],
                 "Fernando", [10, 10, 9.5, 9, 8.5, 10],
                 "Jéssica", [9, 8.5, 9.5, "iurfgw", 8, 5])]

def tratar_notas(lista_notas):
    resultado = {}
    
    dados = lista_notas[0]

    for i in range(0, len(dados), 2):
        nome = dados[i]
        notas_sujas = dados[i+1]
        notas_limpas = []
        
        for nota in notas_sujas:
            try:
                valor = float(nota)
                if 0 <= valor <= 10:
                    notas_limpas.append(valor)
            except (ValueError, TypeError): #trata strings
                continue
        
        resultado[nome] = notas_limpas
            
    return resultado
                 
def calcular_media(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)
  
def processar_alunos(dados_tratados):
    resultados = []
    recuperacao = []
    maior_media = -1
    top_student = ""

    for nome, notas in dados_tratados.items():
        media = calcular_media(notas)
        resultados.append((nome, media))

        if media < 7:
            recuperacao.append(nome)

        if media > maior_media:
            maior_media = media
            top_student = nome

    return resultados, recuperacao, top_student, maior_media

medias, em_recuperacao, melhor_aluno, nota_top = processar_alunos(dados_limpos)

def gerar_relatorio(resultados, recuperacao, top_student, maior_media):
    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE DESEMPENHO\n" + "="*25 + "\n")
        for nome, media in resultados:
            f.write(f"{nome}: {media:.2f}\n")
        
        f.write("\nRecuperação:\n" + ", ".join(recuperacao) if recuperacao else "Nenhum")
        f.write(f"\n\nMelhor Aluno: {top_student} ({maior_media:.2f})")

res, rec, top, nota = processar_alunos(dados_tratados)
gerar_relatorio(res, rec, top, nota)
