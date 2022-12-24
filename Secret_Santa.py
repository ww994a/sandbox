import random

print ('''How Many Possibilities Exist in a Secret Santa Drawing
--William Wilson

A slip of paper is put into a hat for each member. 
Members take turns drawing, they can not draw them-
selves. If a member draws themself they draw does
not count.

In this simulation you choose the number of people
and the number of times to run the simulation.
The program outputs each unique draw as an array,
where each person is numbered starting at index 0,
as well as the total number of possibilities.
''')

#setup environment

people = int(input('How many people? ')) 
iterations  = int(input('Number of simulations? ')) 

picks = []

print("computing...")

#run the simulation
while (iterations > 0):
    #print an update as to how many iterations are left
    if iterations  > 1 and iterations % 100 == 0 :
        print(iterations)

    #Each iteration we create a new bag
    bag = []
    for i in range(people) :
        bag.append(i)


    #each person picks
    this_pick = []
    for person in range(people):

        #first we pick one
        if len(bag)  > 1 :
                random_pick = random.randint(0,len(bag)-1)
        else :
            random_pick = 0

        pick = bag.pop(random_pick)
        this_pick.append([person,pick])

    #check for duplicates
    original = True 

    if len(picks) > 0 :
        for old_pick in picks :
            match = 0

            #here we see if our pick has already been counted
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

    ##if it pasts our tests we add it to the list
    if  original :
        picks.append(this_pick)
    iterations -= 1


for pick in picks :
    #print each possibility on a seperate line
    print(pick)

#Print Total possibilities
print("Total: "+str(len(picks)))
