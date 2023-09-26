import json

# pessoa = {
#     "nome": "João",
#     "idade": 39,
#     "email": "daniel-paulo.silva@1111.com",
#     "telefone": "1111-1111",
#     "endereco": "Rua 1, 11",
#     "cidade": "São Paulo",
#     "estado": "SP",
#     "numeros preferidos": (1, 2, 3, 4, 5),
#     "programador": True,
#     "linguagens": ["Python", "PowerFX", "C++"],
# }

# with open("pessoa.json", "w") as arquivo:
#     json.dump(pessoa, arquivo, indent=2)


with open ('pessoa.json', 'r') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)