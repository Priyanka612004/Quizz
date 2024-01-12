print("InstructionsS\nTo Select Option Enter: 1,2,3 or 4 \nTo Skip Question Enter: 0")
q=[["1.Which of the following is Tricontinental Country?","chad", "Chile", "Mali", "Swaziland",2],
      ["2.Famous fast food restaurant company Burger King belongs to which Country?","America", "England", "Turkey", "None of these",1],
      ["3.Office of strategic service (OSS) was old name of which Intelligence agency?","MI6", "CIA", "ISI", "N.O.T",2],
      ["4.The first person to draw the map of earth?","Heraclitus", "phythagoras", "Anaximander", "Thales",3],
      ["5.Who laid first step on the Moon?","LMP Edgar", "CMP Stuart", "Neil Armstrong", "None of them",3],
      ["6.What is the name of Chinese parliament?","National Assembly", "National people s Congress", "Fedral parliament","None",2],
      ["7.Ogaden desert is present in____?","Europe", "Asia", "Africa", "America",3],
      ["8.Capital of America is_____?","Washington Dc", "Alaska", "Hawaii", "California",1],
      ["9.Wadi Rum which resemblance to the surface of Mars is located in____?","Argentina", "Israel", "Jordan", "Egypt",3],
      ["10.Borneo Island is in which Ocean?","Indian Ocean", "Pacific Ocean", "Arctic Ocean", "Atlantic",2]]
m=0
n=0
mu=0
for i in range (0,len(q)):
    print(f"\n{q[i][0]}\n\n1.{q[i][1]}  2.{q[i][2]}\n3.{q[i][3]}  4.{q[i][4]}")
     
    ch=int(input ('enter your answer: '))
    if (ch<5 and ch>0):
        if(ch==q[i][5]) :   
            print('correct answer')
            mu=mu+1
            print('.......................................................................')
        else:        
            print('incorrect answer')
            print('.......................................................................')
    elif (ch==0):
        print('Skipped Question')
        m=m+1
        print('...........................................................................')
    elif(ch>5 or ch<0):
        print('invalid choice')
        n=n+1
        print('...............................................................................')

print('...................................................................................')
print('Total Correct Answers: ',mu)
print('Total Incorrect Answers: ',10-mu-m-n)
print('Skipped Questions: ',m)
print('Invalid Choise: ',n)
print('...................................................................................')
print("Total Marks: 10")
print("Marks Obtained: ",mu)



