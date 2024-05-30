print('''
       ______
   _.-':::::::`.
   \::::::::::::`.-._
    \:::''   `::::`-.`.
     \         `:::::`.\
      \          `-::::`:
       \______       `:::`.
       .|_.-'__`._     `:::\
      ,'`|:::|  )/`.     \:::
     /. -.`--'  : /.\     ::|
     `-,-'  _,'/| \|\\    |:|
      ,'`::.    |/>`;'\   |:|
      (_\ \:.:.:`((_));`. ;:|
      \.:\ ::_:_:_`-','  `-:|
       `:\\|     SSt:
          )`__...---'
          
''')
print("Welcome to Treasure Island, Mateys!")
print("Your mission is to find me treasure...")
print("You've crossed a fork in the trail.") 
first_trap = str(input("Do you go left or right? ")).lower()
if first_trap != 'left':
          print("Oh no! you fell into a large hole. Game over! Try again next time, matey!")
else:
          second_trap = str(input("You came across a large river and the waters are rough. Do you swim or wait? ")).lower()
          if second_trap != 'wait':
                    print("Blimey! You've come under attack by angry trout! Game over for you, bucko!")
          else:
                    print("You're at the door of an abandoned castle with 3 doors.")
                    third_trap = str(input("Which door do you choose to open? Red, Blue or Yellow? ")).lower()
                    if third_trap == 'red':
                              print("You've fallen in a pit of fire and it burns. Game over!")
                    elif third_trap == 'blue':
                              print("You've opened the door of the Beast. He's very hungry. Game over!")
                    elif third_trap == 'yellow':
                              print("Huzzah! You found me treasure!")
                    else:
                              print("Game over, matey. Har har har...")
