class Zoo:
    def __init__(self, name_of_the_zoo):
        self.name_of_the_zoo = name_of_the_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.__animals = 0

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            print(f"Mammals in {self.name_of_the_zoo}: {', '.join(self.mammals)}")
        elif species == 'fish':
            print(f"Fishes in {self.name_of_the_zoo}: {', '.join(self.fishes)}")
        elif species == 'birds':
            print(f"Birds in {self.name_of_the_zoo}: {', '.join(self.birds)}")

        print(f"Total animals: {self.__animals}")


name_of_zoo = input()
n = int(input())
zoo = Zoo(name_of_zoo)
for lines in range(1, n+1):
    line = input()
    info = line.split(' ')
    species = info[0]
    name = info[1]

    zoo.add_animal(species, name)

species = input()
zoo.get_info(species)







