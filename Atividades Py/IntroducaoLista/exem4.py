pokemons = ['Pikachu', 'Mew', 'Abra',
            'Charmander', 'Rayquaza', 'Dragonite', 'Lucario']

print(pokemons, len(pokemons))
#append(valor): adicionar itens no fim da lista
pokemons.append("Mewtwo")
pokemons.append("Articuno")
pokemons.append("Zapdos")
pokemons.append("Moltres")
pokemons.append("Ho-oh")

print(pokemons, len(pokemons))

#insert(indice, valor): adicionar um item atraves de uma posição
pokemons.insert(1, 'Gengar')
print(pokemons, len(pokemons))

#extend([valor, valor, valor]): adicionar multiplos itens
pokemons.extend(['Eeve', 'Charizard', 'Caterpie'])
print(pokemons, len(pokemons))
#pop(index): remover item da lista por base do index
pokemons.pop(3)
print(pokemons, len(pokemons))

#reverse: inverte a ordem orginal da lista
pokemons.reverse()
print(pokemons, len(pokemons))
#sort: Ordenar valores de uma lista no modo crescente(A-Z, 0-n, etc)
pokemons.sort()
print(pokemons, len(pokemons))


#remove(valor): remover um item da lista por base do valor

pokemons.remove("Zapdos")
print(pokemons, len(pokemons))

#del(index): remover item da lista por base do index
del pokemons[1]
print(pokemons, len(pokemons))

#del(index): remover item da lista por base do intervalo de index
del pokemons[1:3] #1 até o 3
print(pokemons, len(pokemons))

#clear(): limpar a lista
pokemons.clear()
print(pokemons, len(pokemons))