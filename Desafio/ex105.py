def notas(*n, sit=False):
    """
    notas(*n, sir=False)

        --> Funcao para analisar notas de Alunos.
        :param n: Notas dos alunos (aceita varias).
        :param sit: Valor opocional, indica se deve ou não adicionar a situação.
        :param return: Dicionario com várias informações sobre a turma.
    """
    notas = dict()
    # Adicionar valores no dicionario
    notas = dict()
    notas["total"] = len(n)
    notas["mai"] = max(n)
    notas["men"] = min(n)
    notas["media"] = sum(n) / len(n)
    # Identificar situação 
    if 8 > notas["media"] >= 5:
        situacao = "RAZOÁVEL"
    elif notas["media"] < 5:
        situacao = "RUIM"
    else:
        situacao = "BOA"
    if  sit:
        notas["situação"] = situacao
    # Retornar
    return notas

# Main Program
resp = notas(10, 8, sit=True)  
print(resp)