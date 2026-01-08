import json

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_alunos = dados["alunos"]

media_idade = 0
total_idade = 0
total_mensalidade = 0

for aluno in lista_alunos:
    total_idade += aluno["idade"]
    total_mensalidade += aluno["mensalidade"]

media_idade = total_idade/len(lista_alunos)

print(media_idade)
print(total_mensalidade)