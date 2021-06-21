class City:
    def __init__(self,name,population,area) -> None:
        self.name = name
        self.population = population
        self.area = area
    
    def __str__(self) -> str:
        info = "{0} has a population of {1} and is {2} square km.".format(self.name,str(self.population),str(self.area)) 
        return info

    def density(self):
        dens = float(f'{self.population/self.area:.2f}')
        return dens
        
        
        
class Country:
    def __init__(self,name,cities=[]) -> None:
        self.name = name
        self.cities = cities

    def num_cities(self):
        length = len(self.cities)
        return length

    def total_population(self):
        population = 0
        for i in range(len(self.cities)):
            population += self.cities[i].population
        self.population = population
        return population

    def total_area(self):
        area = 0
        for i in range(len(self.cities)):
            area += self.cities[i].area
        self.area = area
        return area

    def density(self):
        dens = float(f'{self.population/self.area:.2f}')
        return dens

    def __str__(self):
        info = ""
        for i in range(len(self.cities)):
            info += "{0} has a population of {1} and is {2} square km. ".format(self.cities[i].name,str(self.cities[i].population),str(self.cities[i].area))
        return info
        
        
ct1 = City('Seoul',9776000,605)
ct2 = City('Busan',3429000,770)
ct3 = City('Incheon',2923000,1063)
ct4 = City('LA',3967000,1302)
print(ct1)
print(ct2)
print(ct3)
print(ct4)
print(ct1.density())
print(ct2.density())
print(ct3.density())
print(ct4.density())
print("=======================")

korea = Country('Korea',[ct1,ct2,ct3])
usa = Country('USA')
print(korea.num_cities())
print(korea.total_population())
print(korea.total_area())
print(korea.density())
print(korea)

usa.cities = [ct4]
print(usa.num_cities())
print(usa.total_population())
print(usa.total_area())
print(usa.density())
print(usa)
