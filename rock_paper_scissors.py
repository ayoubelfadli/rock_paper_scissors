class rock_paper_scissors :
    
    def __init__(self,g):
        self.A=g
    def fonction(self ):
        g= str(input("enter your choise : rock/paper/scissors : "))
        print("your choise is : ", g)
        import random
        items = ['rock', 'paper', 'scissors']
        rand_item = random.sample(items, 1)
        for item in random.sample(items, 1):
            print ("robot choise is : " , item)

        if g == str("rock") and item == str("scissors"):
            print("you win")
        if g == str("paper") and item == str("rock"):
            print("you win")
        if g == str("scissors") and item == str("peper"):
            print("you win")
        if g == str("scissors") and item == str("rock"):
            print("you lost")
        if g == str("rock") and item == str("paper"):
            print("you lost")
        if g == str("paper") and item == str("scissors"):
            print("you lost")

        if g == str("rock") and item == str("rock"):
            print("try again")


        if g == str("paper") and item == str("paper"):
            print("try again")

        if g == str("scissors") and item == str("scissors"):
            print("try again")
rock_paper_scissors()
rock_paper_scissors.fonction()



    
    







        







from string import*




         

    
