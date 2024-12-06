import re

# Texto do documento
texto = """
"""


pattern = r"(\d+\.\d+\.\d+\.\d+:\d+:\S+:\S+)"
resultados = re.findall(pattern, texto)

# Exibir os resultados
for proxy in resultados:
    print(proxy)
