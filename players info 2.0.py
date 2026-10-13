class Player:
    def __init__(self, name, club, age, position):
        self.name = name
        self.club = club
        self.age = age
        self.position = position


name = input("what's the player name: ")
club = input("club: ")
age = int(input("age: "))
position = input("what position: ")
player1 = Player(name, club, age, position)
print(f"{player1.name} playes for {player1.club} and is {player1.age} years old and he plays as a {player1.position}")
name2 = input("Second player name: ")
club2 = input("club2: ")
age2 = int(input("age2: "))
position2 = input("what position: ")
player2 = Player(name2, club2, age2, position2)
print(f"{player2.name} playes for {player2.club} and is {player2.age} years old and he playes as a {player2.position}")
