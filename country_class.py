"""
This python file works as a Happiness Index Measurement System, by taking user input for a country's
name, then ratings of Environment, Economy, Culture, Healthcare and Education from 0 to 100.
"""
# Country Class
class Country:      
    __slots__=['__name','__environment','__economy','__culture','__healthcare','__education']
    # __ = Private fields
    
    def __init__(self, name, environment, economy, culture, healthcare, education):
        self.__name = name
        self.__environment = environment
        self.__economy = economy
        self.__culture = culture
        self.__healthcare = healthcare
        self.__education = education

    # Getters/Accessors for fields (name, environment, economy, culture, healthcare, education):
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


   # Setters/Mutators for fields(name, environment, economy, culture, healthcare, education)

    def set_name(self, newname):
        self.__name = newname
        
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

    def set_allFactors(self,newname,newenv,neweconomy,newculture,newhealthcare,neweducation):
        self.__name = newname
        self.__environment = newenv
        self.__economy = neweconomy
        self.__culture = newculture
        self.__healthcare = newhealthcare
        self.__education = neweducation

# HappinessMeter Class
class HappinessMeter:  
    def __init__(self):
        self.countries = []    # Starts as an empty list to add countries to

    def add_country(self, country):
        self.countries.append(country)    
        
    def measure_happiness(self):
        print("Happiness Measurement:")
        for i in self.countries:
            env = int(i.get_environment())
            eco = int(i.get_economy())
            cul = int(i.get_culture())
            health = int(i.get_healthcare())
            edu = int(i.get_education())
            factors = [env,eco,cul,health,edu]
            happiness = sum(factors) / len(factors)
            print( i.get_name(), ":" , round(happiness, 2) )

def main():
    meter = HappinessMeter()
    num_country = int(input("Enter the number of countries: "))

    for i in range(num_country):
        print("\nEnter details for country " + str(i + 1) + ":")
        name = input("Name: ")
        env = int(input("Environment (0-100): "))
        eco = int(input("Economy (0-100): "))
        cul = int(input("Culture (0-100): "))
        health = int(input("Healthcare (0-100): "))
        edu = int(input("Education (0-100): "))

        country = Country(name, env, eco, cul, health, edu)
        
        meter.add_country(country)

    meter.measure_happiness()


if __name__ == "__main__":
    main()
