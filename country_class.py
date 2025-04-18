

class Country:
    def __init__(self, name, environment, economy, culture, healthcare, education):
        self.name = name
        self.environment = environment
        self.economy = economy
        self.culture = culture
        self.healthcare = healthcare
        self.education = education

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
