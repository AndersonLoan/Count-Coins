# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Loan
# Section: 574
# Assignment: 11.2
# Date: 10 10 22
#

gamereader = open('game.txt','r')
lst1 = []
coins = 0
for nextline in gamereader:
    lst1.append(nextline)

for i in range(len(lst1)):
    if lst1[i][0] == 'c':
        if lst1[i][5] == '+':
            with open("coins.txt",'w') as coinwriter:
                coinwriter.write(lst1[i][6:(len(lst1[i]))])
        elif lst1[i][5] == "-":
            with open("coins.txt",'w') as coinwriter:
                coinwriter.write(lst1[i][5:(len(lst1[i]))])            
    elif lst1[i][0] == 'j':
        if lst1[i][5] == '+':
            i = lst1[i][6:(len(lst1[i])-2)]
        elif lst1[i][5] == "-":
            i = lst1[i][5:(len(lst1[i])-2)]
with open("coins.txt",'r') as coinwriter:
    for coincounter in coinwriter:
        coins += int(coincounter)
print(f"Total coins are {coins}")
gamereader.close() 


