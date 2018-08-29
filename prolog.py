global pergunta
lista = []

arquivo = open('file_prolog/prolog.pl', "r")

for pg in arquivo:
    lista.append(pg)


print("\n")
print("\n")
print("***********PROLOG em PYTHON*************")
print("""
    ===================================
            Consultas Disponoveis
            ---------------------
    progenitor(sara, isaque).
    progenitor(abrao, isaque).
    progenitor(abrao, ismael).
    progenitor(isaque, esau).
    progenitor(isaque, jaco).
    progenitor(jaco, jose).
    
    obs:NÃO SE ESQUEÇA DE APLICAR ( ) COM . NO FINAL!
    ===================================
""")


pergunta = str(input("Pergunta (digite 'e' para sair) ?:- "))

if (pergunta in lista):
    print("Sim")
else:
    print("Não")
