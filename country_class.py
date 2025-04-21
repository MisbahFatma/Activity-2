

class Country:      
    def __init__(self, name, environment, economy, culture, healthcare, education):
        self.__name = name
        self.__environment = environment
        self.__economy = economy
        self.__culture = culture
        self.__healthcare = healthcare
        self.__education = education

    # Getters for fields(name, environment, economy, culture, healthcare, education)
    def get_name(self):
        return self.__name

    def get_environment(self):
        return self.__environment

    def get_economy(self):
        return self.__economy

    def get_culture(self):
        return self.__culture

    def get_healthcare(self):
        return self.__healthcare

     def get_education(self):
        return self.__education


   # Setters for fields(name, environment, economy, culture, healthcare, education)

    def set_name(self, newname):
        self.__name = newName
        
    def set_environment(self, newenvironment):
        self.__environment = newenvironment
        
    def set_economy(self, neweconomy):
        self.__economy = neweconomy

    def set_culture(self, newculture):
        self.__culture = newculture
    
    def set_healthcare(self, newhealthcare):
        self.__healthcare = newhealthcare
    
    def set_education(self, neweducation):
        self.__education = neweducation


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
