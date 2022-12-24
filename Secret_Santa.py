import random

#How Many Possibilities Exist in Secret Santa

#setup environment

people = int(input('How many people? ')) 

x = 5000 
picks = []
print("computing...")

while (x > 0):
    if x > 1 and x % 100 == 0 :
        print(x)
    bag = []
    for i in range(people) :
        bag.append(i)

    total_choices = 0


    #each person picks
    this_pick = []
    for person in range(people):
        #first we pick one
        bad_pick = True
        if len(bag)  > 1 :
            while(bad_pick) :
                random_pick = random.randint(0,len(bag)-1)
                #next we check if we picked ourselves
                if (person != bag[random_pick]) :
                    #we didn't picked our selves
                    bad_pick = False
        else :
            random_pick = 0

        pick = bag.pop(random_pick)

        this_pick.append([person,pick])
    #check for duplicates
    original = True 
    if len(picks) > 0 :
        for old_pick in picks :
            match = 0
            for i in range(people) :
                if old_pick[i][1] == this_pick[i][1] :
                    match += 1
            if match == people  :
                original = False
                break
    ##eliminate any where they chose themselves...
    for i in range(people) :
        if this_pick[i][0] == this_pick[i][1] :
            original = False

    if  original :
        picks.append(this_pick)
    x -= 1


for pick in picks :
    print(pick)
print(len(picks))
