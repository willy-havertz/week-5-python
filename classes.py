# Assignment 1: Design Your Own Class

class Superhero:
    def __init__(self, name, alias, power):
        self.name = name
        self.alias = alias
        self.power = power
    
    def introduce(self):
        """Prints an introduction for the superhero."""
        print(f"I am {self.alias}, also known as {self.name}. My power is {self.power}!")
    
    def use_power(self):
        """Simulates the superhero using their power."""
        print(f"{self.alias} uses their power: {self.power}!")


# Subclass using inheritance to add more specific behavior.
class LegendarySuperhero(Superhero):
    def __init__(self, name, alias, power, origin_story):
        super().__init__(name, alias, power)
        self.origin_story = origin_story
    
    def tell_origin(self):
        """Prints the origin story of the legendary superhero."""
        print(f"My origin story: {self.origin_story}")


# Activity 2: Polymorphism Challenge

class Car:
    def move(self):
        """Defines how a Car moves."""
        print("Driving")


class Plane:
    def move(self):
        """Defines how a Plane moves."""
        print("Flying")


class Boat:
    def move(self):
        """Defines how a Boat moves."""
        print("Sailing")


def main():
    # Test Assignment 1: Superhero classes
    print("=== Superhero Demonstration ===")
    hero = Superhero("Peter Parker", "Spider-Man", "Spider Sense")
    hero.introduce()
    hero.use_power()

    legendary_hero = LegendarySuperhero("Bruce Wayne", "Batman", "Martial Arts", 
                                          "Tragic past in Gotham City that fuels his fight against crime")
    legendary_hero.introduce()
    legendary_hero.use_power()
    legendary_hero.tell_origin()
    
    # Test Activity 2: Polymorphism demonstration
    print("\n=== Polymorphism Challenge ===")
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()  # Each vehicle class implements move() differently

if __name__ == "__main__":
    main()
