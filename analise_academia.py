import json

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_alunos = dados["alunos"]

media_idade = 0
total_idade = 0
total_frequencia = 0
total_mensalidade = 0
quantidade_aluno_plano = {}
frequencia_total_plano = {}

for aluno in lista_alunos:
    total_idade += aluno["idade"]
    total_mensalidade += aluno["mensalidade"]

    plano = aluno["plano"]
    frequencia = aluno["frequencia_mensal"]
    
    if plano in frequencia_total_plano:
        frequencia_total_plano[plano] += frequencia
    else:
        frequencia_total_plano[plano] = frequencia
    
    if plano in quantidade_aluno_plano:
        quantidade_aluno_plano[plano] += 1
    else:
        quantidade_aluno_plano[plano] = 1
    
    total_frequencia += frequencia
media_idade = total_idade/len(lista_alunos)

# 2
print(total_mensalidade)
# 3
print(media_idade)
# 4
print(frequencia_total_plano)
# 5
print(quantidade_aluno_plano)
# 6
print(total_frequencia)

for plano in frequencia_total_plano:
    porcentagem = (frequencia_total_plano[plano]/total_frequencia)*100

    print(plano, porcentagem)