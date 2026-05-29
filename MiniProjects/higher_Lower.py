import os
import random
import game_art
import game_database

score = 0
print(game_art.game_logo)

def display_accountinfo(account):
      name = account["name"]
      description = account["description"]
      country = account["country"]
      return (f"{name} , a {description} , from {country}")

def check_answer(guess,follower_count_1,follower_count_2):
      if follower_count_1 < follower_count_2:
            if guess ==1:
                  return False
            else:
                  return True
      else:
            if guess == 1 :
                  return True
            else:
                  return False
            
account_2 = random.choice(game_database.data)

contiue_flag = True
while contiue_flag:
      account_1 = account_2
      account_2 = random.choice(game_database.data)
      
      while account_2 == account_1:
            account_2 = random.choice(game_database.data)


      print(f"Compare 1: {display_accountinfo(account_1)}")
      print(game_art.vs_logo)
      print(f"Compare 2: {display_accountinfo(account_2)}")
      
      guess = int(input("Who has more follwers? Type 1 or 2 :"))
      
      follower_count_1 = account_1["follower_count"]
      follower_count_2 = account_2["follower_count"]
      
      is_correct = check_answer(guess,follower_count_1,follower_count_2)
      
      
      os.system("cls")
      if is_correct == True:
            score += 1
            print(f"you are right . Tour score is {score}")
      else:
            print(f"you are wrong . Your final score is {score}")
            contiue_flag = False