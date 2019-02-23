import random

Question_List = [
                "Against which team did Parvez Rasool make his ODI debut for India in June 2014?" ,
                "Which national park was named so because the local Maharaja relocated ten villages from the area and declared it a hunting preserve?" ,
                "Which of these Indian athletes refused to accept the bronze medal awarded to her after a controversial bout in the Asian Games?" ,
                "In which American city is the famous indoor stadium Madison Square Garden located?" ,
                "Which of the following is called ‘falak’ in Arabic?" ,
                "Which of these is not a traditional dish in the multi-course meal Wazwaan?" ,
                "Which song did Kavi Pradeep compose to pay homage to the martyrs of the Indo-China war?" ,
                "The symbol of which arithmetic operation also resembles a letter of the English Alphabet?" ,
                "Which Mughal emperor was the grandson of Jahangir?"

]


Options_List = [
                ["Sri Lanka", "Zimbabwe", "Bangladesh", "Pakistan"] ,
                ["Dachigam", "Kaziranga" , "Hazaribagh" , "Ranthambore"] ,
                ["Annu Rani" , "Shiva Thapa" , "L Sarita Devi" , "Devendra Singh Laishram"] ,
                ["San Francisco" , "New York City" , "Washington DC" , "Los Angeles"] ,
                ["Earth" , "Moon" , "Water", "Sky"] ,
                ["Gushtaba" , "Roghan Josh" , "Murgh Mosallam" , "Tabak Maaz"] ,
                ["Ab Tumhare Hawale Watan" , "Mere Desh ki Dharti" , "Apni Azadi Ko Hum" , "Aye Mere Watan ke Logon"] ,
                ["Addition" , "Multiplication" , "Division" , "Subtraction"] ,
                ["Shah Alam" , "Aurangzeb" , "Bahadur Shah" , "Shah Jahan"]
]

Answers_List = [2,0,2,1,3,2,3,1,1]

def lifeline(opt_num):
    while True:
        opt = random.randint(0,3)
        if(opt_num != opt):
            break
    return opt

print("$ WELCOME TO KBC $")
print("You can ask for lifeline : 50-50 by entering 5050")
i = 0
help_counter = 0
while(i<len(Question_List)):
    print(Question_List[i])
    print()
    print("Your options are : ")
    for j in range(0, len(Options_List[i])):
        print(str(j+1)+" : "+Options_List[i][j])
    answer = input("Enter your answer : ")
    print()
    if(answer ==  '5050' and help_counter != 0):
        print("***SORRY, YOU CAN USE LIFELINE ONLY ONCE***")
        print()
        continue
    if(answer.isdigit()!=True):
        print("You cannot enter alphabets or special characters. Only numbers are allowed\n")
        continue
    else:
        answer = int(answer)
    if(answer not in [1, 2, 3, 4, 5050]):
        print("Wrong Input\nPlease choose 1 , 2 , 3 or 4")
        continue
        print()
    else:
        if((answer-1) == Answers_List[i]):
            print("RIGHT ANSWER")
            print()
        elif((answer==5050)):
            help_counter+=1
            o = lifeline(Answers_List[i])
            print(Question_List[i])
            print()
            opt_list = [Answers_List[i], o]
            extra = opt_list[:]
            random.shuffle(opt_list)

            flag = 0
            for m in range(0, len(opt_list)):
                if(opt_list[m]==extra[0]):
                    flag = m

            for k in range(0, len(opt_list)):
                print(str(k+1)+" : "+Options_List[i][opt_list[k]])
            answer = int(input("Enter your answer : "))
            print()
            if((answer-1)!=flag):
                print("WRONG ANSWER\nGAME OVER")
                break
            i+=1
            continue

            if(i==8):
                print("**Congratulations**\n**YOU WON**")
        else:
            print("WRONG ANSWER\nGAME OVER")
            break
            print()
    i+=1
