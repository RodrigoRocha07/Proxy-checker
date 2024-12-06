import os
import random
import json

# Caminhos dos arquivos
proxy_file_path = os.path.join(os.path.dirname(__file__), 'proxy_antigas.txt')
used_proxy_file_path = os.path.join(os.path.dirname(__file__), 'proxy_testada.txt')
proxy_output_file_path = os.path.join(os.path.dirname(__file__), 'chrome_proxy_extension', 'current_proxy.json')

# Função para ler proxies do arquivo
def read_proxies():
    with open(proxy_file_path, 'r', encoding='utf-8') as file:
        proxies = file.read().splitlines()
    return [p for p in proxies if p]  # Remove linhas vazias

# Função para escrever proxies usados no arquivo
def write_used_proxy(proxy):
    with open(used_proxy_file_path, 'a', encoding='utf-8') as file:
        file.write(proxy + '\n')

# Função para remover proxy usado do arquivo original
def remove_used_proxy(proxy):
    proxies = read_proxies()
    proxies = [p for p in proxies if p != proxy]
    with open(proxy_file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(proxies) + '\n')

# Função para obter um proxy aleatório e atualizar os arquivos
def get_random_proxy():
    proxies = read_proxies()
    if not proxies:
        print('///////////////////////////////////////_')
        print('                  Não existem mais proxys disponiveis.')
        print('///////////////////////////////////////_')
        return None

    random_proxy = random.choice(proxies)
    
    write_used_proxy(random_proxy)
    remove_used_proxy(random_proxy)

   #print('Selected Proxy:', random_proxy)

    parts = random_proxy.split(":")
    proxy_details = {
        'host': parts[0],
        'port': int(parts[1]),
        'username': parts[2],
        'password': parts[3]
    }

  




    if proxies:
        with open(proxy_output_file_path, 'w', encoding='utf-8') as file:
            json.dump(proxy_details, file, indent=2)
        return random_proxy





if __name__ == '_main_':
    get_random_proxy()