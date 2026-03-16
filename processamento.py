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