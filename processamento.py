def gerar_relatorio(resultados, recuperacao, top_student, maior_media):
    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE DESEMPENHO\n" + "="*25 + "\n")
        for nome, media in resultados:
            f.write(f"{nome}: {media:.2f}\n")
        
        f.write("\nRecuperação:\n" + ", ".join(recuperacao) if recuperacao else "Nenhum")
        f.write(f"\n\nMelhor Aluno: {top_student} ({maior_media:.2f})")

res, rec, top, nota = processar_alunos(dados_tratados)
gerar_relatorio(res, rec, top, nota)