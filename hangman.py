import random

print('''
       {}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}
       {}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}
       {}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}
       {}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}  {{{}
       {}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {}\n''')
# Dictionary containing words and their clues
words={'COMPUTER':['Important machine used in our daily life','Your favourite subject'],'TRUCK':['Used to carry large stuff','Horn OK Please'],'CUPBOARD':['used to store items','also used for hiding people']}

hangman=['''
      -------
      |     |
      |     @
      |    /|\\  You lose
      |     |
      |    / \\
      |
      |
______|_______''',
'''
      -------
      |     |
      |     @
      |    /|
      |     |
      |    / \\
      |
      |
______________''',
'''
      -------
      |     |
      |     @
      |     |
      |     |
      |    / \\ 
      |
      |
______________''',
'''
      -------
      |     |
      |     @
      |     | 
      |     |
      |    / 
      |
      |
______________''',
'''
      -------
      |     |
      |     @
      |     | 
      |     |
      |    
      |
      |
______________''',
'''
      -------
      |     |
      |     @
      |     
      |     
      |    
      |
      |
______________''',
'''
      -------
      |     |
      |     
      |     
      |     
      |    
      |
      |
______________
''']


# Selecting a word from the dictionary and printing hint
word=random.choice(list(words))
hint=words[word]
print("First Hint :",hint[0])
print("")

# Creating a list to store found letters (initialising with '_')

found=[]
for i in word:
      found.append("_")

# Printing Status of guessed letters and lives (currently no letters found and 5 lives remaining)

lives=6

for i in found:
      print(i,end=" ")
else:
      print("\t\tLives =",lives)
      print(hangman[lives])
      print("")

# Guessing letters (Infinite loop breaks when lives=0 / all letters found)


count=0
while True:
      
      letter=input("Guess letter : ").upper()

      # Checking for letter and flag=true if found
      
      for i in range(len(word)):
            flag=False
            if letter==word[i]:
                  flag=True
                  break
            
      # Printing message if letter found or not and decrementing life if not found
      # Giving second hint if first try
      # Also if on last life, printing you lose message and breaking loop

      if(letter in found):
            print("You already found that letter -_-")
            print("")
      elif(flag==True):
            found[i]=word[i]
            print("You found a letter !")
            print("")
      elif(lives!=1):
            lives-=1
            print("Please try again !")
            print(hangman[lives])
            print("")
            count+=1
            if(count==1):
                  print("Second Hint :",words[word][1])
            
      else:
            print(hangman[0])
            break
      
      # Printing Status of guessed letters and lives

      for i in found:
            print(i,end=" ")
      else:
            print("\t\tLives =",lives)
            print("")

      # Printing win message and breaking loop (if found list = list of letters of word)
      if(found==list(word)):
            print("You Win!!!")
            break
    
