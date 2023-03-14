import json

f = open("TPC3/ptToEnglish.json","r",encoding="utf-8")
file = json.load(f)
f2 = open("TPC3/ptToEnglish.md","w",encoding="utf-8")



content="# Dicionário de medicina Português-Inglês\n\n"
for i in file:
    content+= """### {i}\n""".format(i=i)
    genero = file[i]["Genero"]
    content+= """**Género:** {genero}\n\n""".format(genero=genero)
    if len(file[i]["Sinonimos"]) >0:
        content+= """**Sinónimos:**\n"""
        for j in range(len(file[i]["Sinonimos"])):
            traducao = file[i]["Sinonimos"][j]
            content+= """- {traducao}\n""".format(traducao=traducao)
        content+="\n"


    content+= """**Traduções Inglesas:**\n"""
    for j in range(len(file[i]["English"])):
        traducao = file[i]["English"][j]
        content+= """- {traducao}\n""".format(traducao=traducao)

    content+="\n\n---\n\n"

f2.write(content)
