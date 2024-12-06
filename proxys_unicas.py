def comparar_arquivos(arquivo1, arquivo2, arquivo_saida):
    # Lê o conteúdo dos arquivos e transforma em conjuntos
    with open(arquivo1, 'r') as file1, open(arquivo2, 'r') as file2:
        conteudo1 = set(file1.read().splitlines())
        conteudo2 = set(file2.read().splitlines())

    # Identifica os elementos únicos
    unicos = conteudo1.symmetric_difference(conteudo2)  # Elementos exclusivos a cada conjunto

    # Escreve os elementos únicos no arquivo de saída
    with open(arquivo_saida, 'w') as saida:
        for elemento in sorted(unicos):  # Ordenado para facilitar leitura, se necessário
            saida.write(elemento + '\n')

    print(f"Arquivo com elementos únicos salvo em: {arquivo_saida}")


# Exemplo de uso:
#comparar_arquivos('arquivo1.txt', 'arquivo2.txt', 'elementos_unicos.txt')




def remover_repetidos(arquivo_entrada, arquivo_saida):
    # Lê o conteúdo do arquivo e transforma em um conjunto para remover duplicados
    with open(arquivo_entrada, 'r') as entrada:
        conteudo = entrada.read().splitlines()

    # Remove duplicados preservando a ordem de aparição
    elementos_unicos = list(dict.fromkeys(conteudo))

    # Escreve os elementos únicos no arquivo de saída
    with open(arquivo_saida, 'a') as saida:
        for elemento in elementos_unicos:
            saida.write(elemento + '\n')

    print(f"Arquivo sem duplicatas salvo em: {arquivo_saida}")


# Exemplo de uso:
remover_repetidos('proxy_antigas.txt', 'antigas_unicos.txt')
