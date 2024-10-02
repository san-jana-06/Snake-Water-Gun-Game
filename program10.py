'''1 for snake
-1 for water
0 for gun'''
import random
dict={1:"snake",-1:"water",0:"gun"}
computer_dicison=random.choice(list(dict.keys()))
user_dicison=int(input("your choice:"))
print(f"user_dicison={dict[user_dicison]}")
print(f"computer choice:{dict[computer_dicison]}")
# if(computer_dicison== user_dicison):
#     print("tie game") 
# #else
if(computer_dicison==1 and user_dicison==-1):
    print("computer wins")
elif(computer_dicison==1 and user_dicison==0):
    print("you win")
if(computer_dicison==-1 and user_dicison==0):
    print("computer wins")
elif(computer_dicison==-1 and user_dicison==1):
    print("you wins")
if(computer_dicison==0 and user_dicison==1):
    print("computer wins")
elif(computer_dicison==0 and user_dicison==-1):
    print("you wins")
else:
    print("its tie")
        