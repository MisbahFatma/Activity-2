

class Country:
    def __init__(self, name, environment, economy, culture, healthcare, education):
        self.name = name
        self.environment = environment
        self.economy = economy
        self.culture = culture
        self.healthcare = healthcare
        self.education = education


   # Setters 
   def set_data(self, name, env, eco, cul, health, edu):
        self.name = name
        self.environment = env
        self.economy = eco
        self.culture = cul
        self.healthcare = health
        self.education = edu

    # Getters
    def get_name(self):
        return self.__name

    def get_factors(self):
        return [self.__environment, self.__economy, self.__culture, self.__healthcare, self.__education]



class HappinessMeter:  
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)    
        
    def measure_happiness(self):
        print("Happiness Measurement:")
        for country in self.countries:
            factors = country.get_factors()
            happiness = sum(factors) / len(factors)
            print( country.get_name(), ":" , round(happiness, 2) )


def main():
    meter = HappinessMeter()
    name_country = int(input("Enter the number of countries: "))

    for i in range(name_country):
        print("\nEnter details for country " + str(i + 1) + ":")
        name = input("Name: ")
        env = int(input("Environment (0-100): "))
        eco = int(input("Economy (0-100): "))
        cul = int(input("Culture (0-100): "))
        health = int(input("Healthcare (0-100): "))
        edu = int(input("Education (0-100): "))

        country = Country()
        country.set_data(name, env, eco, cul, health, edu)
        meter.add_country(country)

    meter.measure_happiness()


if __name__ == "__main__":
    main()
