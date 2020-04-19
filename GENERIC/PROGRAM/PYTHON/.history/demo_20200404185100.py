# Default
# def interest(p,r,t):
#     return p*r

# print(interest(5,t=1000,r=8))

# def grp(p,*no,r=5):
#     return no

# print(grp("grp-name",1,2,3,4,6,7))



def check_loss(game_history,game_points,total):
    if game_history[1] == 0:
        game_points[1] -= 1
    else:
        loss_points = game_history[1] * 2
        game_points[1] -= loss_points

    total = game_points[0] + game_points[1] + game_points[2]

game_history = [4,0,2]
game_points  = [12,-4,2]
total = 0
check_loss(game_history, game_points, total)
game_history = [5,2,2]
check_loss(game_history, game_points, total)
print(total,game_points)