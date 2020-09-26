def notas(*n, sit=False):
    notas = dict()
    for v in n:
        notas["total"] = len(n)
        mai = v
        if v > mai:
            notas["maioe"] = mai
    return notas

# Main Program
resp = notas(5.5, 2.5, 1.5)  
print(resp)