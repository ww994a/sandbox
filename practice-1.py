#Create program to input names and alphabatize them

names = []
while True:
    Name = input('Input a name (done to finish):')
    if Name == "done" :
        break
    names.append(Name)

def allCaps(e) :
    return e.capitalize()

names.sort(key=allCaps)
for text in names :
    print (text)

