class Person(object):
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

class Population(object):
    def __init__(self, person_list):
        self.persons = []
        self.population_changes = {}
        self.population_by_year = {}
        self.add_people(person_list)

    def add_people(self, person_list):
        for person in person_list:
            self.persons.append(person)
            self.update_population_changes(person)
        self.update_population()

    def update_population_changes(self, person):
        if person.birth in self.population_changes:
            self.population_changes[person.birth] += 1
        else:
            self.population_changes[person.birth] = 1

        if person.death in self.population_changes:
            self.population_changes[person.death] -= 1
        else:
            self.population_changes[person.death] = -1

    def update_population(self):
        #print sorted(self.population_changes.keys())
        population = 0
        for year in sorted(self.population_changes.keys()):
            population += self.population_changes[year]
            self.population_by_year[year] = population


test_list = [ [1950, 1960],
              [1950, 1962],
              [1951, 1961],
              [1952, 1962], ]

person_list = [Person(x, y) for x, y in test_list]
test_population = Population(person_list)

for person in test_population.persons:
    print person.birth, person.death
for year in sorted(test_population.population_changes.keys()):
     print year, test_population.population_changes[year], test_population.population_by_year[year]
