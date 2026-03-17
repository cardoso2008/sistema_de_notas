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