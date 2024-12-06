import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Função que testa um proxy e retorna o resultado
def test_proxy(proxy):
    try:
        parts = proxy.split(":")
        if len(parts) != 4:
            return proxy, "invalid"

        ip, porta, usuario, senha = parts
        formatted_proxy = f"http://{usuario}:{senha}@{ip}:{porta}"
        proxies = {
            "http": formatted_proxy,
            "https": formatted_proxy,
        }

        test_url = "http://httpbin.org/ip"
        response = requests.get(test_url, proxies=proxies, timeout=5)

        if response.status_code == 200:
            return proxy, "functional"
    except requests.exceptions.RequestException:
        pass

    return proxy, "discardable"

def main():
    # Lê os proxies do arquivo original
    with open('all_proxys.txt', 'r') as file:
        proxies_list = [proxy.strip() for proxy in file.readlines()]

    # Inicializa arquivos para escrita
    with open('funcionais.txt', 'a') as func_file, \
         open('descartaveis.txt', 'a') as desc_file, \
         open('testadas.txt', 'a') as tested_file:

        # Usa ThreadPoolExecutor para processamento paralelo
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(test_proxy, proxy): proxy for proxy in proxies_list}

            for future in tqdm(as_completed(futures), total=len(futures), desc="Testando Proxies"):
                proxy, status = future.result()

                # Escreve o proxy no arquivo correspondente
                tested_file.write(proxy + '\n')  # Todos os proxies testados
                if status == "functional":
                    func_file.write(proxy + '\n')  # Proxies funcionais
                elif status == "discardable":
                    desc_file.write(proxy + '\n')  # Proxies descartáveis

    # Limpa o arquivo original
    open('all_proxys.txt', 'w').close()  # Sobrescreve o arquivo para esvaziá-lo

if __name__ == "__main__":
    main()
