#Code by Jacksper
#Hangman art by Joane G. Stark
GameIsDone = False
hangman =  '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |          |   | 
| |          |   | 
| |          |   |  
| |          |   |   
| |          -----
| |          
| |          
| |          
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .


 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y    |
| |       // |   | 
| |      //  |   |  
| |     ')   |   |   
| |          -----
| |          
| |        
| |          
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .


 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\
| |       // |   | \\
| |      //  |   |  \\
| |     ')   |   |   (`
| |          ||--
| |          || 
| |          || 
| |          || 
| |         / | 
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .


 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\
| |       // |   | \\
| |      //  |   |  \\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .



 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\
| |       // |   | \\
| |      //  |   |  \\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         / | 
""""""""""|_`-'     |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .



 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y    Y\
| |       // |   | \\
| |      //  |   |  \\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''


def displayBoard(hangman, missedletters, correctletters, word):
    global GameIsDone
    print(hangman[len(missedletters)])
    print()

    whoops = ""
    
    for i in range(len(word)):
        if word[i] in correctletters:
            whoops += word[i]
        else:
            whoops += "_"
    
    if "_" not in whoops:
        GameIsDone = True
    #print(GameIsDone)
   
            
    for letter in whoops:
        print(letter, end=' ')
    print()
    print()
  
    print('Missed Letters:', end=' ')
    print(missedletters)
   
    print()
    print()


def getguess(alreadyguessed):
    while not GameIsDone:
        guess = (input("Gimme ya letter mate!"))
        guess = guess.lower()
    
        if len(guess) != 1:
            print('Enter a SINGLE letter')
        elif guess in alreadyguessed:
            print('You already guessed that letter mate')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Guess a LETTER!')
        else:
            return guess

def PlayAgain():
    print('Do you want to play again mate? (y or n)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedletters = ''
correctletters = ''
word = (input("Player 1 what's the word?"))
print("\n" * 50)



                
while not GameIsDone:

    hangman1 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |           `--'
| |            
| |             
| |              
| |            
| |          
| |          
| |          
| |          
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''
    
    hangman2 =  '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |          |   | 
| |          |   | 
| |          |   |  
| |          |   |   
| |          -----
| |          
| |          
| |          
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''

    hangman3 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y    |
| |       // |   | 
| |      //  |   |  
| |     ')   |   |   
| |          -----
| |          
| |        
| |          
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .'''

    hangman4 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   |   |   (`
| |           ---
| |           
| |          
| |          
| |          
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''

    hangman5 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   |   |   (`
| |          ||--
| |          || 
| |          || 
| |          || 
| |           
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''

    hangman6 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''

    hangman7 = '''

 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         / | 
""""""""""|_`-'     |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .'''


    hangman8 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y    Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .'''

    
    displayBoard(hangman, missedletters, correctletters, word)

    guess = getguess(missedletters + correctletters)
    #print("here is the guess: " + guess)
    if guess:
        if guess in word:
            correctletters = correctletters + guess
            print('Correct')
        else:
            missedletters = missedletters + guess + ' '
    foundAllLetters = True
    for i in range(len(word)):
        if word[i] not in correctletters:
            foundAllLetters = False
            break
  
    if guess:
        if len(missedletters) == 2:
            print(hangman1)
        if len(missedletters) == 4:
            print(hangman2)
        if len(missedletters) == 6:
            print(hangman3)
        if len(missedletters) == 8:
            print(hangman4)
        if len(missedletters) == 10:
            print(hangman5)
        if len(missedletters) == 12:
            print(hangman6)
        if len(missedletters) == 14:
            print(hangman7)
        if len(missedletters) == 16:
            print(hangman8)

    if len(missedletters) == 16:
            displayBoard(hangman, missedletters, correctletters, word)
            print('Game Over... No more guesses\nAfter ' ' '+ str(len(missedletters)) + ' ' ' missed guesses and ' + str(len(correctletters)) + ' correct guesses, the word was "' + word + '"')
            GameIsDone = True

   #if "_" not in correctletters:
   # if len(whoops) ==len(word):
   #     print('Nice Job! The word is "' + word + '" You Won!')
   #     GameIsDone = True
    if not guess:
       print('Nice Job! The word is "' + word + '" You Won!')
    
               
 
        
    if GameIsDone:
        if PlayAgain():
            missedletters = ''
            correctletters = ''
            GameIsDone = False
            word = word = (input("Player 1 what's the word?"))
            print("\n" * 50)
        else:
            break 

                
                

    

