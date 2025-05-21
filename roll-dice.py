import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll


while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
        
            break
        else:
            print("Must be 2 - 4 players.")
    else:
       print("Invalid, Try again!")
       
max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_index in range(players):
        print("\nplayer ", player_index + 1 ,"turn has just started!\n")
        print("your total score is: ",players_scores[player_index],"\n")
        current_score = 0
    
        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done! ")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a: ", value)
                
            print("Your score is: ",current_score)
            
        players_scores[player_index] += current_score
        print("Your total score is" ,players_scores[player_index])
        
    max_score = max(players_scores)
    winning_index = players_scores.index(max_score)
    print("player number " , winning_index + 1, "is the winner with a score of:", max_score)

