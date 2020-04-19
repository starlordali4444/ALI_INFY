
# def check_loss(game_history,game_points,total):
#     if game_history[1] == 0:
#         game_points[1] -= 1
#     else:
#         loss_points = game_history[1] * 2
#         game_points[1] -= loss_points

#     total = game_points[0] + game_points[1] + game_points[2]
# game_history = [4,0,2]
# game_points  = [12,-4,2]
# total = 0
# check_loss(game_history, game_points, total)
# game_history = [5,2,2]
# check_loss(game_history, game_points, total)
# print(total,game_points)

# result=0
# def find_sum(num1,num2):
#     if(num1!=num2):
#         result=num1+num2
#     else:
#         result=2*(num1+num2)
# find_sum(3,4)
# print(result)
# find_sum(5,5)
# print(result)

# def find_avg(list_num):
#     result_sum=0
#     for num in list_num:
#         result_sum+=num
#     result_avg=result_sum/len(list_num)
# find_avg([5,8,5])
# print(result_avg)

def func(word, char="A"):
    if(char=="A"):
        return len(word[1:])
    elif(char=="B"):
        return len(word[2:])
    else:
        return len(word)

print(func("Apple","A"),end=" ")
print(func("Apple","B"),end=" ")
print(func("Apple"),end=" ")
print(func("Apple","C"),end=" ")
