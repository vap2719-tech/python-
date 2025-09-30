import random
word_list = ["apple","bannana","mango","goa"]
lives=6
#print(word_list)
rand_list = random.choice(word_list) 
print(rand_list)
display=[]
for letter in rand_list:  #for i in range(len(rand_list))   
    display += '_'
print(display)
game_over=False
while not game_over:
    guess_word=input("guess letter is :").lower()
    for position in range(len(rand_list)):
        letter = rand_list[position]
        if letter == guess_word:
           display[position]=guess_word
    print(display)       

    if guess_word not in rand_list:
        lives -=1
        if lives == 0:
            game_over = True     
            print("you lose! 😒 !")
    if '_' not in display:
        game_over=True
        print("you win! 😍 !")        