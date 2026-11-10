class Character():
    def __init__(self, name):
        self.__name = name
        self.__health = 100
        self.__defense = 5

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_defense(self):
        return self.__defense

    def take_damage(self, amount):
        damage = round((amount * 100) / (100 + self.get_defense))


class Warrior(Character):
    def __init__(self, name, health, defense, stregth):
        super().__init__(name, health, defense)
        self.__strength = stregth
   
    def get_health(self):
        return self.__health
    
    def get_defense(self):
        return self.__defense

    def get_strength(self):
        return self.__strength

    def attack(self, target):
        pass

    def take_damage(self, amount):
        pass


class Mage(Character):
    def __init__(self, name, health, defense, mana):
        super().__init__(name, health, defense)
        self.__mana = mana

    def get_health(self):
        return self.__health
    
    def get_defense(self):
        return self.__defense

    def get_mana(self):
        return self.__mana

    def attack(self, target):
        pass

    def take_damage(self, amount):
        pass


class Archer(Character):
    def __init__(self, name, health, defense, arrows):
            super().__init__(name, health, defense)
            self.__arrows = arrows
    
    def get_health(self):
        return self.__health
        
    def get_defense(self):
        return self.__defense
    
    def get_arrows(self):
        return self.__arrows
    
    def attack(self, target):
        pass
    
    def take_damage(self, amount):
        pass
       
   
