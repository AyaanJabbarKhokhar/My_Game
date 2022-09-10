import random

print("Welcom to best game in the world")
print("You have to cross the river and fight dragon then u can go to castle and find castle")
choices = input("Y ou have 3 choices you can 'swim' take 'boat' 'fly': ")

if choices == "fly":
  print("You crossed the lake: ")
if choices == "swim":
  print("You got eaten by the sea monster: ")
  raise SystemExit
elif choices == "boat":
  print("whale jumped on your boat: ")
  raise SystemExit


hp_list = ["11","20","30","52","25","18","34"]
one_hp = random.choice(hp_list)
two_hp = random.choice(hp_list)
three_hp = random.choice(hp_list)

dragon = int(input(f"You have to fight the dragon you have 4 choices u have to choose your hp '{one_hp}' '{two_hp}' '{three_hp}'"))

dragon_real = 29

if dragon < dragon_real :
  print("You have defeated the dragon :) ")
coins = input("Congradulations u have reached the castle you got 30 coins do u want to open crate? 'yes' or 'no'").lower()
coins_amount = 30


if coins == "yes":
  crate_rewards = ["glacier m4 max (mythic)","pineapple set (legendary)","corn set ()epic","blood raven x-suit (ultimate)","silver","silver","silver""silver","silver","silver"]
  select = random.choice(crate_rewards)
  print(f"Congragulations! you got {select}")
  coins = 0
else:
  print("You have played really well Good Luck!")
  
  