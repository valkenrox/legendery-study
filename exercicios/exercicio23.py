# copy, sorted, produtos.sort
import copy as co
import pprint as pp
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



novos_produtos = co.deepcopy(produtos)

novos_produtos.append({'nome': 'Produto 6', 'preco': 10.00})
novos_produtos.append({'nome': 'Produto 7', 'preco': 121.20})

juros_produtos1 = [
    {**novos_produtos, 'preco':round(novos_produtos['preco'] * 1.1, 2)}
    for novos_produtos in novos_produtos
]
# pp.pprint(novos_produtos)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos.sort(key=lambda produto: produto["nome"], reverse=True)
pp.pprint(produtos)


produtos_ordenados_por_nome = co.deepcopy(produtos)
produtos_ordenados_por_nome.append({'nome': 'Produto 6', 'preco': 10.00})
produtos_ordenados_por_nome.append({'nome': 'Produto 7', 'preco': 121.20})
pp.pprint(produtos_ordenados_por_nome)



# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos.sort(key=lambda produto: produto["preco"])
pp.pprint(produtos)
print()

produtos_ordenados_por_preco = co.deepcopy(produtos)
produtos_ordenados_por_preco.append({'nome': 'Produto 9', 'preco': 96.00})
produtos_ordenados_por_preco.append({'nome': 'Produto 10', 'preco': 464.20})
pp.pprint(produtos_ordenados_por_preco)