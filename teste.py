import random
def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    soma = sum((10 - i) * cpf[i] for i in range(9))
    digito1 = 11 - (soma % 11)
    cpf.append(digito1 if digito1 < 10 else 0)
    
    soma = sum((11 - i) * cpf[i] for i in range(10))
    digito2 = 11 - (soma % 11)
    cpf.append(digito2 if digito2 < 10 else 0)
    
    return "{}.{}.{}-{}".format(
        ''.join(map(str, cpf[:3])),
        ''.join(map(str, cpf[3:6])),
        ''.join(map(str, cpf[6:9])),
        ''.join(map(str, cpf[9:]),
    ))
for a in range(5):
    print(gerar_cpf())