def activity1 ():
    print("Hello World")
def activity2 ():
    name =input("What is your name .? ")
    print("Hi", name , "welcome to the Matrix")
def activity3 (): 
    print("Happy\n\t\tMonday") 
    print("\tBSIT 1A\n From DLL") 
    print("The Quick Brown Fox  \rJumps Over \t\nThe Lazy Dog.")
def activity4 ():
    name = input("Enter a string -> ")
    print("Your name has ", len(name)," characters")
def activity5 ():
    something = eval(input("Input something (1-1000) --> "))
    print("The data type of something is",type(something))
    answer = 6 + something
    print("the answer is ", answer)
def activity6 ():
    n1 = eval(input("Enter the first number : ")) 
    n2 = eval(input("Enter the second number : ")) 

    sum = n1 + n2
    dif = n1 - n2
    pro = n1 * n2
    quo = n1 / n2

    print("\nThe sum of", n1, "and", n2, "is", sum)
    print("The difference of", n1, "and", n2, "is", dif)
    print("The product of", n1, "and", n2, "is", pro)
    print("The quotient of", n1, "and", n2, "is", quo)
    print(n1, "exponent by", n2, "is", n1 ** n2)
    print("The remainder of", n1, "and", n2, "is", n1 % n2)
    print("The floor division of", n1, "and", n2, "is", n1 // n2) 	
def activity7 ():
    a = 5

    print("the value of a is ", a)

    a += 5

    print("the value of a is ", a)

    a = a + 5
    a += 3
    a += 8
    a *= 2
    a -= 3
def activity8 ():
    amount = 600
    withdrawal = 300

    print(amount == withdrawal)

    x = 2
    y = 4

    print(x < y)
def activity9 ():
    username = "kayle"
    password = "mississippi"

    print (username == 'kayle')
    print((username == 'kayle') and (password == 'mississippi'))
    print((username == 'kayle') or (password == 'mississippi'))
    print(not((username == 'kayle') or (password == 'mississippi')))
def activity10 ():
    
    name = input("please input your name > ")
    isStudent = input("Are you a student (Yes/No) ")
    fare = eval(input("bayad "))

    if isStudent.lower() == "yes" :
    	discount = fare * .2
    	new_fare = fare - discount
    	print("hi", name, "student discount is ", discount," Discounted fare is ", new_fare )
    else: 

    	print("Sorry ", name," you are not eligible for student discount")
def activity11 ():
    temp = eval(input("Enter temperature --> "))

    if temp >= 1 and temp <= 20:
	    print("Temperature outside is cold")
    elif temp >= 21 and temp <= 30:
	    print("Temperature outside is lukewarm")
    elif temp >= 31 and temp <= 40:
	    print("Temperature outside is warm")
    elif temp >= 41 and temp <= 50:
	    print("Temperature outside is hot")
    if temp >= 50: 
	    print("Temperature outside is boiling hot")

    else:
	    print("invalid Temperature")
def activity12 ():
    for x in range (1, 11, 1,):
        print(x, "hahahaha")
def activity13 ():
    num = 0
    for w in range(1, 11):
        w = eval(input("Enter a number"))
        num += w
        print(" num", num)
def activity14 ():
    for heads in range(20, 0, -1):
        print(heads)
def activity15 ():
    end = 0

    for w in range(1,11):
        num = eval(input("Input a number:"))
        if num % 2 == 1:
            end += num
    print(f"The summation of all number is {end}")
def activity16 ():
    for w in range(1,11):
	    print(w,end="\n")
def activity17 ():
    for q in range(1,11):
	    for w in range(1,11):
	    	print(w,end=" ")
	    print()
def activity18 ():
    for w in range(1,11,1):
        for e in range(1, w, 1):
            print(e, end=' ')
        print()
def activity19 ():
    for q in range(1,11,1):
        for w in range(1, q, 1):
            print("*", end=' ')
        print()
def activity20 ():
    for q in range(1,11):
        for w in range(1,q,1):
            print("#",end=" ")
        for e in range(10,q,-1):
            print("*",end=" ")
        print()    
def activity21 ():
    #washing machine cleaning
    #(pass) dummy code

    smelly = True
    while smelly == True:
        confirm = input("Do you want to continue washing the clothes? (yes, no)").lower()

        if confirm == 'yes':
            print("continue the cycling")
            continue
        elif confirm == 'no' :
            print("cycling stop")
            break
        else:
            print("Invalid Input")
            continue
def activity22 ():
    import random
    num = random.randint(1,10)
    GuessNum = 0
    idk = True

    while idk == True:
        inp = int(input("Guess a number between 1-10 :"))
        GuessNum += 1

        if inp == num:
            print("Congrats you guess Right!")
            print(f"the right random number is {num} :> ")
            print(f"it took you {GuessNum} tries ")
            break

        else:
            print("Wrong Guess Try Again.")
def activity23 ():
    brands = ['Shellby','Aston Martin', 'Maserati', 'Ford', 'Dodge']

    brands.sort()
    print(brands)
    brands.reverse()
    print(brands)
    brands.append('ferrari')
    print(brands)
    brands.pop()
    print(brands)
    brands.append('ferrarri')
    print(brands)
    for q in brands:
        print(f"{q}, 2025")

    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("\n")

    full_name = 'Ken Joshua Pasamba'
def activity24_1 ():

    inject("Garrick")
    inject("Mctavish")
    inject("Riley")
    summation(3)
    summation(5)
def activity24 ():
    
    #creating functions
    #keyword, def = define
    #code REUSABILITY

    def inject(name):
        print(f"Hello {name}, How are you? ")

    inject("Garrick")
    inject("Mctavish")
    inject("Riley")


    def summation(x):
        sum = 0
        for q in range(x, 0, -1):
                sum += q
        print(f" The sum of {x} is {sum}")
def activity25_1 ():
    def activity1():
        name = input("What is youre name: ")
        print("hi", name ,"welcome to the matrix")

    def activity2():
       age = eval(input("What is youre age: "))
def activity25 ():

    name = input("hi, What is your name->")

    print(f"welcome {name}, to my Compiler Program")

    isContinue = True

    while isContinue == True:
        print("select a Program")
        print("A - Activity1\nB - Activity2\nC - Activity15\n E - Exit")

        choose = input("what program / code would you like to run ->").lower()

        if choose == 'a':
            activity1()
            continue
        elif choose == 'b':
            activity2()
            continue
        elif choose == 'c':
            pass
            continue
        elif choose == 'e':
            print("system exit")
            break
        else:
            print("invalid choice")
def activity26 ():
    programming_language = ['Python',"TurboC",'C++','JavaScript','Perl','Java']

    programming_language2 = {'easy':'Python','medium':'TurboC','intermidiate':'C++','hard':'JavaScript','verry hard':'Perl','pray':'Java'}

    print(programming_language2['easy'])
def activity27 ():
    print("Adding Data to Dictionary ->")
    print(" ========================== ")
    proceed = True

    empty_dictionary = {}

    def print_anime():
        for anime in empty_dictionary.values():
            print (f"Anime name -- {anime}")
    
    while proceed == True:
        keys = input("Input anime Name ->")
        values = input("Enter   -> ")

        empty_dictionary [keys] = values

        choice = input("Would you like to continue adding anime (y/n)").lower ()

        if choice == 'y' :
            print("Continuing ... ")
            continue
        elif choice == 'n' :
            print("program stops")
            break
        else:
            print("Invalid Input")
            continue
def activity28 ():
    # Introduction
    # in your cmd type
    #"pip install venv"
    #"pip install pygame"

    # importing libraries
    import pygame
    import time
    import random

    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('GeeksforGeeks Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                    random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):
    
        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)
        
        # create the display surface object 
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)
        
        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()
        
        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():
    
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)
        
        # creating a text surface on which text 
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        
        # create a rectangular object for the text 
        # surface object
        game_over_rect = game_over_surface.get_rect()
        
        # setting position of the text
        game_over_rect.midtop = (window_x/2, window_y/4)
        
        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        
        # after 2 seconds we will quit the program
        time.sleep(2)
        
        # deactivating pygame library
        pygame.quit()
        
        # quit the program
        quit()


    # Main Function
    while True:
        
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two 
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                            random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)

    game_loop()
def code_challenge1 ():
    name = input("what is your name .?")

    print("\t\t\t\t\t*\n\t\t\t\t*\t\t*\n\t\t\t*\t\t\t\t*\n\t\t*\t\t\t\t\t\t*\n\t*\t\t\t\tHi\t\t\t\t*\n\t\t*\t\t\t", name, "\t\t*\n\t\t\t*\t\t\t\t*\n\t\t\t\t*\t\t*\n\t\t\t\t\t*")
def code_challenge2 ():
    dell = eval(input("Enter amount to deposit: "))

    n1 = dell // 1000
    dell = dell % 1000

    n2 = dell // 500
    dell = dell % 500

    n3 = dell // 200
    dell = dell % 200

    n4 = dell // 100
    dell = dell % 100

    n5 = dell // 50
    dell = dell % 50

    n6 = dell // 20
    dell = dell % 20

    n7 = dell // 10 
    dell = dell % 10

    n8 = dell // 5 
    dell = dell % 5

    n9 = dell // 1
    dell = dell % 1

    print("\tHere is Breakdown:")
    print("\tPh-\t", n1, "\t\t-1000")
    print("\tPh-\t", n2, "\t\t-500")
    print("\tPh-\t", n3, "\t\t-200")
    print("\tPh-\t", n4, "\t\t-100")
    print("\tPh-\t", n5, "\t\t-50")
    print("\tPh-\t", n6, "\t\t-20")
    print("\tPh-\t", n7, "\t\t-10")
    print("\tPh-\t", n8, "\t\t-5")
    print("\tPh-\t", n9, "\t\t-1")
def code_challenge3 ():

    username = "kayle"
    password = "mississippi"

    user = input("Enter username:")
    pwd = input("Enter password:")

    if user == username and pwd == password :
        print("Access Granted")
    else:
        print("Access Denied")
def code_challenge4 ():
    num = eval(input("Enter number:"))
    if num % 2 == 0 :
        print( num , "even")
    else:
        print(num , "odd")
def code_challenge5 ():
    print("Welcome to the manga recommender!")
    print("pls insert your preference to find your manga")

    Genre = input(" What is prefered genre? (shonen, slice of life, mecha):")
    Duration = input(" what duration should the manga be? (short, medium, long):")
    Time = input("Which year? (2000s, 2010s):")

    if Genre == 'shonen' and Duration == 'short' and Time == '2000':
        print("The manga recommend for this is 'Yu Yu Hakusho' ")
    elif Genre == 'shonen' and Duration == 'short' and Time == '2010':
        print("The manga recommend for this is 'Bamboo Blade' ")
    elif Genre == 'shonen' and Duration == 'medium' and Time == '2000':
        print("The manga recommend for this is 'Rurouni Kenshin' ")
    elif Genre == 'shonen' and Duration == 'medium' and Time == '2010':
        print("The manga recommend for this is 'Blue Exorcist' ")
    elif Genre == 'shonen' and Duration == 'long' and Time == '2000':
        print("The manga recommend for this is 'One Piece' ")
    elif Genre == 'shonen' and Duration == 'long' and Time == '2010':
        print("The manga recommend for this is 'Fairy Tail' ")

    if Genre == 'slice of life' and Duration == 'short' and Time == '2000':
        print("The manga recommended for this is 'Yotsuba&!' ")
    elif Genre == 'slice of life' and Duration == 'short' and Time == '2010':
        print("The manga recommended for this is 'Barakamon' ")
    elif Genre == 'slice of life' and Duration == 'medium' and Time == '2000':
        print("The manga recommended for this is 'Honey and Clover' ")
    elif Genre == 'slice of life' and Duration == 'medium' and Time == '2010':
        print("The manga recommended for this is 'March Comes in Like a Lion' ")
    elif Genre == 'slice of life' and Duration == 'long' and Time == '2000':
        print("The manga recommended for this is 'Aria' ")
    elif Genre == 'slice of life' and Duration == 'long' and Time == '2010':
        print("The manga recommended for this is 'Silver Spoon' ")

    if Genre == 'mecha' and Duration == 'short' and Time == '2000':
        print("The manga recommended for this is 'RahXephon' ")
    elif Genre == 'mecha' and Duration == 'short' and Time == '2010':
        print("The manga recommended for this is 'ID-0' ")
    elif Genre == 'mecha' and Duration == 'medium' and Time == '2000':
        print("The manga recommended for this is 'Zegapain' ")
    elif Genre == 'mecha' and Duration == 'medium' and Time == '2010':
        print("The manga recommended for this is 'Knights of Sidonia' ")
    elif Genre == 'mecha' and Duration == 'long' and Time == '2000':
        print("The manga recommended for this is 'Getter Robo Saga' ")
    elif Genre == 'mecha' and Duration == 'long' and Time == '2010':
        print("The manga recommended for this is 'Valvrave the Liberator' ")

    else:
        print("Invalid input. I can only provide this at the moment (shonen, slice of life, mecha)")
def code_challenge6 ():
    num = eval(input("input number - "))

    result = 1
    for n in range(num, 0, -1):
        #print(n)
        result *= n

    print("The factorial is ",result)
def code_challenge7 ():
    print("ODD NUMBER SUMMATION")

    odd_num = 0
    for x in range(1, 11, 1):
        num = eval(input("Please input a number-> "))
        if num % 2 != 0:
            odd_num += num
    print("The total sum of all the odd number is--> ", odd_num)
def code_challenge8 ():
    print("Welcome to multiplication table maker:")
    num = eval(input("Enter a number: "))

    for n in range (1, 11):
        result = num * n
        print(F"{num}x{n} = {result}")
def code_challenge9 ():
    print("Welcome to countdown simulator:")
    time = int(input("Enter a number for countdown:"))

    for n in range (time, 0, -1):
        print(n)
    print("Liftoff!")
def code_challenge10 ():
    print("\t\t", end= "     *")
    for x in range(1,12,1):
        for y in range(12,x,-1):
            print(" ", end=' ')
        for z in range(1,x,1):
            print("*", end=" ")
        for t in range(1,x,1):
            print("*", end=" ")
        print()
def code_challenge11 ():

        print("\t\t", end="     *")
        for x in range(1,12,1):
            for y in range(12,x,-1):
                print(" ", end=' ')
            for z in range(1,x,1):
                print("*", end=" ")
            for t in range(1,x,1):
                print("*", end=" ")
            print()
        for x in range(1,12,1):
            for y in range(1,x,1):
                print(" ", end=' ')
            for z in range(12,x,-1):
                print("*", end=" ")
            for t in range(12,x,-1):
                print("*", end=" ")
            print()
        print("\t\t" "     *")

def code_challenge12 ():
    for i in range(1, 7, 1):  
        for x in range(7,i,-1):
            print(" ", end=" ")
        for y in range(i,0,-1):
            print(y, end=" ")
        for z in range(2,i+1,1):
            print(z, end=" ")
        print()
def code_challenge13 ():
    for x in range(1,6,1):
        for i in range(1,11,1):
            print(" ",end=" ")
        for a in range(5,x,-1):
            print(" ",end=" ")
        for b in range(1,x,1):
            print("*",end=" ")
        for c in range(x,2,-1):
            print("*",end=" ")
        print()
    for x in range(1,4,1):
        for i in range(1,12,1):
            print(" ",end=" ")
        for a in range(1,x,1):
            print(" ",end=" ")
        for b in range(4,x,-1):
            print("*",end=" ")
        for c in range(3,x,-1):
            print("*",end=" ")
        print()
    for x in range(1,11,1):
        for s in range(1,5,1):
            print(" ",end=" ")
        for a in range(10,x,-1):
            print(" ",end=" ")
        for b in range(0,x,1):
            print("*",end=" ")
        for c in range(x,1,-1):
            print("*",end=" ")
        print()
    for x in range(1,13,1):
        for a in range(14,x,-1):
            print(" ",end=" ")
        for b in range(0,x,1):
            print("*",end=" ")
        for c in range(x,1,-1):
            print("*",end=" ")
        print()
    for x in range(1,15,1):
        for c in range(14,x,-1):
            print(" ",end=" ")
        for a in range(0,x,1):
            print("*",end=" ")
        for b in range(x,1,-1):
            print("*",end=" ")
        print()

    for x in range(1,10,1):
        for a in range(1,11,1):
            print(" ",end=" ")
        for b in range(1,8,1):
            print("*",end=" ")
        print()
def code_challenge14 ():
    #Odd number compiler
    #while Loop

    name = input("Please put your name: \t") 
    print("+++++++++++++++++++++++++++++")
    print("Odd number compiler, type '0' to terminate the loop")

    sum = 0
    odd = ""
    tuloy = True

    while tuloy == True:
        num = eval(input("Please input a number --> "))
    
        if num % 2== 1:
            print("Odd number detected")
            odd += str(num) + ","
            sum += num
            continue
        elif num == 0:
            print("loop terminated")
            break
        else:
            if num % 2 == 0:
                print("Even number, skipping ... ")
            else:
                print("Invalid Number")
                continue

    print(f"Hi {name}, The sum of all od number is {sum} ")
    print(f"All the odd numbers you input is {odd}")
def code_challenge15 ():
    #anime watchlist maker
    #while loop


    animelist = []
    proceed = True
    print("--Welcome to Anime watch list--")
    print("--Enter 'close' to stop listing--")

    while proceed == True:
        anime = input("Input your desired anime: ")

        if anime.lower() == "close":
            print("--Your watchlist has been updated--")
            break

        animelist.append(anime)
        print(f"{anime} (has been added to your watch list)")

    for i in animelist:
        print(f"- {i}")
def code_challenge16 ():

    import os
    import json
    os.system('cls') #To clear the menu when putted something
    diction = {} #empty dictionary

    while True: 
        print("Select From options Below\nA - Add Information\nB - Print all\nc - Search Information\nd - Delete Information\ne - To Edit File\nF - Export Data\nG - Import Data\nP - Exit") #Menu List

        new = input("Typing...       ").lower() #lower so the putted letter can be lower case or upper case

        if new == "a":
            print("Adding Information")
            ky = input("Key to call for the Information: ")
            fname = input("Input Student First Name: ")
            lname = input("Input Student Last Name: ")
            course = input("Input Course: ")
            email = input("Input Student Email: ")

            diction[ky] = [fname,lname,course,email] #It will add multiple data to the dictionary 
            print("Data saved")
            os.system('cls')
            continue
        elif new == "c":
            os.system('cls')
            srch = input("key of the information: ")

            for a in diction.keys():# for q in diction(): #Search, For loop will help us connect to the dictionary
                if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
                    print("record Found")
                
                    print("Record Info")
                    print("--------------------------")
                    for y in diction[srch]:
                        print(f": {y}")
                    print("--------------------------")
                else:
                    print("Information not Found")  
                break
            continue
        elif new == "b":
            os.system('cls')
            for a,p in diction.items(): #for loop it will manage all the information in the dictioanary
                print(f"STUDENTS ID {a}: STUDENT RECORD {p}") #it will now print all the items in dictionary
            continue
        elif new == "d":
            os.system('cls')
            print("Delete existing record")
            srch = input("key of the information: ")
            if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
                

                print("Record deleted")
                print("--------------------------")
                for i in diction[srch]:
                        print(f": {i}")

                diction.pop(srch)
                print("Record deleted")
            else:
                print("Information cannot found") 
            continue
        elif new == "e":
            os.system('cls')
            print("Record Modification")
            
            srch = input("key of the information: ")

            for a in diction[srch]:
                        print(f": {a}")

            
            fname = input("Input Student First Name: ")
            lname = input("Input Student Last Name: ")
            course = input("Input Course: ")
            email = input("Input Student Email: ")

            diction[srch][0] = fname
            diction[srch][1] = lname
            diction[srch][2] = course
            diction[srch][3] = email

            print("Data Updated")

            continue
        elif new == "f":
            os.system('cls')
            with open("diction.json","w") as new_file:
                json.dump(diction,new_file, indent=4)
                print("Data Exported")
            continue
        elif new == "g":
            os.system('cls')
            with open("diction.json","r") as new_file:
                diction_json = json.load(new_file)

            diction = diction_json
            print("Data Imported")

            continue
        elif new == "p":
            print("Exiting")
            break
        else:
            print("Invalid Input")
        


