

class Country:      
    def __init__(self, name, environment, economy, culture, healthcare, education):
        self.__name = name
        self.__environment = environment
        self.__economy = economy
        self.__culture = culture
        self.__healthcare = healthcare
        self.__education = education

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for environment
    def get_environment(self):
        return self.__environment

    def set_environment(self, environment):
        self.__environment = environment

    # Getter and Setter for economy
    def get_economy(self):
        return self.__economy

    def set_economy(self, economy):
        self.__economy = economy

    # Getter and Setter for culture
    def get_culture(self):
        return self.__culture

    def set_culture(self, culture):
        self.__culture = culture

    # Getter and Setter for healthcare
    def get_healthcare(self):
        return self.__healthcare

    def set_healthcare(self, healthcare):
        self.__healthcare = healthcare

    # Getter and Setter for education
    def get_education(self):
        return self.__education

    def set_education(self, education):
        self.__education = education


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
