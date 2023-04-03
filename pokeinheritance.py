from random import randint, shuffle

class Card():
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f'{self.name}'

class Pokemon(Card):
	def __init__(self, name, health, pokemonType, ability = None):
		super().__init__(name)
		self.health = health
		self.type = pokemonType
		self.type = ability

class Energy(Card):
	def __init__(self, name, symbol):
		super().__init__(name)
		self.symbol = symbol

	def __str__(self):
		return f'{self.name}'

class Trainer(Card):
	def __init__(self, name, trainerType, text, rule):
		super().__init__(name)
		self.type = trainerType
		self.text = text
		self.rule = rule

	def __str__(self):
		return f'{self.name}'

class Player():
	def __init__(self, name, hand):
		self.name = name
		self.hand = hand

	def __str__(self):
		hand = ' + Cards:\n'
		for i in self.hand:
			hand += f'  - {i}\n'
		return f'# Player: {self.name}\n{hand}'

def main():
	pokelist = [
		['Alakazam', 'PSY'],
		['Blastoise', 'WAT'],
		['Chansey', 'NOR'],
		['Charizard', 'FIR'],
		['Clefairy', 'NOR'],
		['Gyarados', 'WAT'],
		['Hitmonchan', 'FIG'],
		['Machamp', 'FIG'],
		['Magneton', 'ELE'],
		['Mewtwo', 'PSY'],
		['Nidoking', 'GRA'],
		['Ninetales', 'FIR'],
		['Poliwrath', 'WAT'],
		['Raichu', 'ELE'],
		['Venusaur', 'GRA'],
		['Zapdos', 'ELE'],
		['Beedrill', 'GRA'],
		['Dragonair', 'NOR'],
		['Dugtrio', 'FIG'],
		['Electabuzz', 'ELE'],
	]

	energylist = [
		'PSY',
		'WAT',
		'NOR',
		'FIR',
		'NOR',
		'WAT',
		'FIG',
	]

	trainerlist = [
		['Clefairy Doll', 'type', 'text', 'rule'],
		['Computer Search', 'type', 'text', 'rule'],
		['Devolution Spray', 'type', 'text', 'rule'],
		['Imposter Professor Oak', 'type', 'text', 'rule'],
		['Item Finder', 'type', 'text', 'rule'],
		['Lass', 'type', 'text', 'rule'],
		['Pokémon Breeder', 'type', 'text', 'rule'],
	]

	pokemonCards = []
	energyCards = []
	trainerCards = []

	for i in pokelist:
		newPokemonCard = Pokemon(i[0], 60, i[1])
		pokemonCards.append(newPokemonCard)
		print(newPokemonCard)

	for i in energylist:
		newEnergyCard = Energy(i + ' Energy', i)
		energyCards.append(newEnergyCard)
		print(newEnergyCard)

	for i in trainerlist:
		newTrainerCard = Trainer(i[0], i[1], i[2], i[3])
		trainerCards.append(newTrainerCard)
		print(newTrainerCard)

	# Create Deck
	deck = pokemonCards + energyCards + trainerCards

	hand1 = []
	for i in range(0,17):
		choice = randint(0, len(deck) - 1) # pick random card from deck
		hand1.append(deck[choice])
		del deck[choice]

	# shuffle remaining cards
	shuffle(deck)
	hand2 = deck

	player1 = Player('Jessie', hand1)
	player2 = Player('James', hand2)

	print() # print line break
	print(player1)
	print(player2)

if __name__ == '__main__':
	main()