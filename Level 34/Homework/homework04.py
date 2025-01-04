def points(games):
    total_points = 0
    
    for game in games:
        x, y = map(int, game.split(":")) 
        if x > y:
            total_points += 3  # Win
        elif x == y:
            total_points += 1  # Tie
        
    return total_points