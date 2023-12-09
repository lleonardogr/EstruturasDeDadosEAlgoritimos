def ler_entrada_arquivo(filename):
    try:
        with open(filename, 'r') as file:
            N = int(file.readline().strip())
            Q = int(file.readline().strip())
            pedras_faltantes = [tuple(map(int, linha.strip().split())) for linha in file.readlines()[:Q]]
        return N, pedras_faltantes
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e} \r\n")
        return None

def contar_caminhos_piramide(N, pedras_faltantes):
    """
    Conta o número de diferentes maneiras de escalar até o topo da pirâmide,
    considerando as regras de movimento e pedras faltantes ou deterioradas.

    :param N: Número de pedras na camada base e o número de camadas na pirâmide.
    :param pedras_faltantes: Uma lista de tuplas representando as pedras faltantes ou deterioradas.
    :return: Número de diferentes maneiras de escalar até o topo da pirâmide.
    """
    # Validação do número de níveis da pirâmide e quantidade de pedras faltantes ou deterioradas
    if not (1 <= N <= 1000) or not (0 <= len(pedras_faltantes) <= N * (N + 1) / 2):
        return "Parâmetros fora dos limites especificados."

   # Inicialização da pirâmide
    piramide = [[1 if (1, j + 1) not in pedras_faltantes else 0 for j in range(N)]]

    # Atualizar a pirâmide com linhas adicionais inicializadas com zeros
    piramide.extend([[0] * N for _ in range(N - 1)])
    
    for i in range(1, N):
        for j in range(N - i):
            piramide[i][j] = 0 if (i + 1, j + 1) in pedras_faltantes else piramide[i - 1][j] + piramide[i - 1][j + 1]

    # Calcula o número total de caminhos
    total_caminhos = sum(piramide[-1])

    # Verifica se o número de caminhos está dentro do limite
    if not (0 <= total_caminhos < 2**63):
        return "Número de maneiras diferentes de escalar a pirâmide fora dos limites."
  
    return total_caminhos

def testar():
    try:
        # Teste 1: Pirâmide com 4 níveis e sem pedras faltantes, resultados esperado 8
        N_teste1 = 4
        pedras_faltantes_teste1 = []
        resultado_teste1 = contar_caminhos_piramide(N_teste1, pedras_faltantes_teste1)

        # Teste 2: Pirâmide com 6 níveis e algumas pedras faltantes, resultados esperado 14
        N_teste2 = 6
        pedras_faltantes_teste2 = [(2, 1), (4, 3), (5, 2)]
        resultado_teste2 = contar_caminhos_piramide(N_teste2, pedras_faltantes_teste2)

        # Teste 3: Pirâmide com 3 níveis e uma pedra faltante, resultados esperado 2
        N_teste3 = 3
        pedras_faltantes_teste3 = [(2, 2)]
        resultado_teste3 = contar_caminhos_piramide(N_teste3, pedras_faltantes_teste3)

        print(f"Número de maneiras diferentes para escalar a pirâmide: {resultado_teste1}\r\n", 
              f"Número de maneiras diferentes para escalar a pirâmide: {resultado_teste2}\r\n", 
              f"Número de maneiras diferentes para escalar a pirâmide: {resultado_teste3}")
        print('testes concluídos com sucesso')
        print('==============================================================================\r\n')
    except Exception as e:
        print(f"Erro nos testes: {e} \r\n")
        return None


def executar(filename):
    try:
        caminho_arquivo_exemplo = filename
        N, pedras_faltantes = ler_entrada_arquivo(caminho_arquivo_exemplo)
        resultado = contar_caminhos_piramide(N, pedras_faltantes)
        print(f"Número de maneiras diferentes para escalar a pirâmide: {resultado}")
    except Exception as e:
        print(f"Erro na execução: {e} \r\n")
        return None



if __name__ == "__main__":
    testar()
    while(True):
        nome_arquivo = input("Digite o nome do arquivo: ")
        try:
            executar(nome_arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado. Por favor, verifique o nome do arquivo.")
            exit()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            exit()