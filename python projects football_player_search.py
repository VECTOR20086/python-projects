players = ["messi", "embappe", "yamal", "vinicius"]
player1 = {
    "name": "messi",
    "age": 39,
    "club": "inter miami"
}
player2 = {
    "name": "embappe",
    "age": 27,
    "club": "real madrid"
}
players_info = {
    "messi": player1,
    "embappe": player2
}
player = input("enter a player : ")
if player in players_info:
    selected_player = players_info[player]
    print("player found")
else:
    print("player not found")
while True:
    information = input("what information do you want?: ")
    if information == "quit":
        print("Good bye")
        break
    try:
        print(selected_player[information])
    except KeyError:
        print("information not found")
