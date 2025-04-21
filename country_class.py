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

    def set_allFactors(self,newname,newenv,neweconomy,newculture,newhealthcare,neweducation): # Method to set or update all factors for a country at once
        self.__name = newname   # Set the country's name
        self.__environment = newenv   # Set the environment score (0-100)
        self.__economy = neweconomy    # Set the economy score (0-100)
        self.__culture = newculture    # Set the culture score (0-100)
        self.__healthcare = newhealthcare  # Set the healthcare score (0-100)
        self.__education = neweducation   # Set the education score (0-100)

# HappinessMeter Class
class HappinessMeter:  
    def __init__(self):
        self.countries = []    # Starts as an empty list to add countries to

    def add_country(self, country): 
        self.countries.append(country)   # Add a country object to the countries list 
        
    def measure_happiness(self):
        print("Happiness Measurement:")   # Print a heading for the happiness measurement results
        for i in self.countries:          # Retrieve and convert the values of various happiness-related factors
            env = int(i.get_environment())  # Retrieve and convert the (env,eco,cul,health,edu) score to an integer
            eco = int(i.get_economy())
            cul = int(i.get_culture())
            health = int(i.get_healthcare())
            edu = int(i.get_education())
            factors = [env,eco,cul,health,edu]  # Store all factor scores in a list
            happiness = sum(factors) / len(factors)  # Calculate the average score to determine happiness
            print( i.get_name(), ":" , round(happiness, 2) )  # Print the country's name and its happiness score rounded to two decimals

def main():
    meter = HappinessMeter()  # Create an instance of the HappinessMeter class
    num_country = int(input("Enter the number of countries: "))  # Prompt the user to enter the number of countries to evaluate

    for i in range(num_country):  # Loop through each country to collect details
        print("\nEnter details for country " + str(i + 1) + ":")
        name = input("Name: ")
        env = int(input("Environment (0-100): "))
        eco = int(input("Economy (0-100): "))
        cul = int(input("Culture (0-100): "))
        health = int(input("Healthcare (0-100): "))
        edu = int(input("Education (0-100): "))

        country = Country(name, env, eco, cul, health, edu)   # Create a Country object with the provided values
        
        meter.add_country(country)  # Add the country to the HappinessMeter's list

    meter.measure_happiness() # Calculate and display happiness scores for all entered countries


if __name__ == "__main__":
    main()
