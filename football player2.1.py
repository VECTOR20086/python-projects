class Player:
    def __init__(self, name, club, age, position):
        self.name = name
        self.club = club
        self.age = age
        self.position = position


try:
    name = input("what is the player name: ")
    club = input("what club does he play for: ")
    age = int(input("age: "))
    position = input("what position does he play in: ")
except:
    print("enter a valid information")
Player1 = Player(name, club, age, position)
print(f"{Player1.name} plays for {Player1.club}, he is {Player1.age} old, and he plays as a {Player1.position} ")
