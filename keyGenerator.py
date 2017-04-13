#  # #### #   #    #### #### #   #                          
# #  #     # #     #    #    ##  #                          by Kyle Franke
##   ###    #  ### # ## ###  # # #              ###   ##
# #  #      #      #  # #    #  ##         # #  # #    #   (I probably won't
#  # ####   #      #### #### #   #          #   ### # ###     update this)

import random

def keyGen():
    #generates and prints key
    listA = []
    for num in range(10):
        listA.append(str(num)) #list of all numbers 0-9
    listB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    listC = []
    for el in listB:
        listC.append(el.lower()) #use list of upper letters to make lower list
    listAll = listA + listB + listC #list of all characters
    listBC = listB + listC #list of all letters, upper and lower
    string = "!@#$%-^&*()-?<,>."
    string2 = ''
    repAll = ['#', '%', '$', '&', '!', '*', '(', '?', ')', '>', '<', '.']
    repNum = ['@', '^', ',']
    for num in range(17): #generates random key
        if num != 5 and num != 11:
            string2 += listAll[random.randint(0, 61)]
        else:
            string2 += '-'
    for el in repAll: #generates algorithmic key
        rand = random.randint(0, 61)
        string = string.replace(el, listAll[rand])
    for el in repNum:
        rand = random.randint(0, 9)
        string = string.replace(el, listA[rand])
    print("\nNow, press '1' if you want to generate a string based on my",\
          "algorithm,\nor press '2' if you want to generate a completely",\
          "random string.")
    choice = ''
    while choice != '1' and choice != '2': #choose to show random or algorithm
        choice = input("\nWhat's your choice? ")
        if choice == '1':
            print("\nAlgorithmic string:", string)
        elif choice == '2':
            print("\nCompletely random string:", string2)
        else:
            print("\nYou didn't choose '1' or '2'.")
    print("\nKey generated successfully! Now, please go back to the old",\
          "instructions\nwith 1, 2, 3, and 4.")
    
def main():
    #ui
    print("Welcome to Kyle's random string generator!")
    print("\nPress '1' to generate a key, press '2' to view information",\
          "about the generator\nalgorithm, press '3' to view information",\
          "about the generated keys, or press '4'\nto exit.")
    choice = input("\nWhat'll it be, chief? ")
    while choice != '4':
        if choice == '1':
            #calls keygen
            keyGen()
            choice = input("\nWhat's next, boss? ")
        elif choice == '2':
            #prints from text file
            file = open("aboutAlgorithm.txt", 'r')
            for line in file:
                print(line.rstrip("\n"))
            file.close()
            choice = input("\nWhat's next, cap? ")
        elif choice == '3':
            #prints from other text file
            file = open("aboutKeys.txt", 'r')
            for line in file:
                print(line.rstrip("\n"))
            file.close()
            choice = input("\nWhat's next, my dude? ")
        else:
            #not necessary but its good practice to check input
            print("\nOnly type '1', '2', '3', or '4' - refer to instructions if",\
                  "you're confused.")
            choice = input("\nWhat do you want to do, brotherman? ")
    #program exits
    print("\nThanks for trying out my key generator.")

main()
