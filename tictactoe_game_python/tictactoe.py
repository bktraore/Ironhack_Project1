#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def vizu(gamestate): #vizu use the list gamestate and put the values of this list into 3 new list to make the game look like the tictactoe
    

    global list1
    global list2
    global list3

    list1=["__","__","__"]
    list2=["__","__","__"]
    list3=["__","__","__"]

    for i in gamestate :
        if i[0]=='1':
            list1[0]=i
    
    for i in gamestate :
        if i[0]=='2':
            list1[1]=i

    for i in gamestate :
        if i[0]=='3':
            list1[2]=i

    for i in gamestate :
        if i[0]=='4':
            list2[0]=i

    for i in gamestate :
        if i[0]=='5':
            list2[1]=i

    for i in gamestate :
        if i[0]=='6':
            list2[2]=i

    for i in gamestate :
        if i[0]=='7':
            list3[0]=i

    for i in gamestate :
        if i[0]=='8':
            list3[1]=i

    for i in gamestate :
        if i[0]=='9':
            list3[2]=i       

    #return print("\n",list1,"\n",list2,"\n", list3)
    return list1, list2, list3

#vizu()


# In[ ]:


def transfo(list1, list2 , list3) : #transfo convert the 3 list of vizu into cross or circle depending on the coordinates. If coordinate contain an A it convert it into a circle. Else it convert it into a cross

   #list1=["1B","2A","__"]
   #list2=["4B","5B","6A"]
   #list3=["7B","8A","9A"]

   list4=["_","_","_"]
   list5=["_","_","_"]
   list6=["_","_","_"]

   #list1
   if list1[0][1]=="A":
      list4[0]="O"
   elif list1[0][1]=="B":
      list4[0]="X"

   if list1[1][1]=="A":
      list4[1]="O"
   elif list1[1][1]=="B":
      list4[1]="X"

   if list1[2][1]=="A":
      list4[2]="O"
   elif list1[2][1]=="B":
      list4[2]="X"
   #list2
   if list2[0][1]=="A":
      list5[0]="O"
   elif list2[0][1]=="B":
      list5[0]="X"

   if list2[1][1]=="A":
      list5[1]="O"
   elif list2[1][1]=="B":
      list5[1]="X"

   if list2[2][1]=="A":
      list5[2]="O"
   elif list2[2][1]=="B":
      list5[2]="X"
   #list3
   if list3[0][1]=="A":
      list6[0]="O"
   elif list3[0][1]=="B":
      list6[0]="X"

   if list3[1][1]=="A":
      list6[1]="O"
   elif list3[1][1]=="B":
      list6[1]="X"

   if list3[2][1]=="A":
      list6[2]="O"
   elif list3[2][1]=="B":
      list6[2]="X"

   print("\n",list4,"\n",list5,"\n", list6)
   return("turn is finished")
   
#transfo()


# In[ ]:



def whowon(gamestate): #this function allowed us to determine which player between player A and B is the winner 
    x='Winner is Player A :)'
    y='Winner is Player B :)'
    winner=0
    global end 
    end=False

    L1=[{"1A","2A","3A"},{"4A","5A","6A"},{"7A","8A","9A"},{"1A","4A","7A"},{"2A","5A","8A"},{"3A","6A","9A"},{"1A","5A","9A"},{"3A","5A","7A"}]
    L2=[{"1B","2B","3B"},{"4B","5B","6B"},{"7B","8B","9B"},{"1B","4B","7B"},{"2B","5B","8B"},{"3B","6B","9B"},{"1B","5B","9B"},{"3B","5B","7B"}]
    gamestateset = set(gamestate)

    for s in L1:
        if s.issubset(gamestateset):
            winner=x
            end=True


    for s in L2:
        if s.issubset(gamestateset):
            winner=y
            end=True
            

    return winner,end 

    


 
    


# In[ ]:


#TICTACTOE GAME CODE

print("\n When it will be your turn to play, enter the coodonate of the case basing on :\n")

#those 3 print display the coordinates of each case for the game
print(["1","2","3"])
print(["4","5","6"])
print(["7","8","9"])


coordinates=["1","2","3","4","5","6","7","8","9"] #player will have to enter a coordinates who is in the list 
print(coordinates)
gamestate=[]#this list will contain every plays coordinates
nodouble=[]##this list will contain every plays coordinates


#player A is the first one to play. Its not in the loop because the loop will count 8 turn more than this one. In total we want 9 turn max
A=input("A please play an empty case")
gamestate.append(A+"A")
print("gamestate is",gamestate)
nodouble.append(A)  
vizu(gamestate)
print(transfo(list1, list2, list3))


counter=0

#loop where A and B will play in turn 
while counter<4 : # So the game stop when all the case are full

    B=input("B please play an empty case")   
    while B in nodouble or B not in coordinates:#players can't play in a full case are in a coordinates that does not exit 
        B=input("B played in an occuped case or an invalid case, please play an other case")#if the play of B is not valid he will have to enter a new coordinate while he enter a valid coordinate
    
    print("B play",B,"your play is valid")
    gamestate.append(B+"B")
    nodouble.append(B)
    print("gamestate is ",gamestate)
    
    vizu(gamestate)
    print(vizu(gamestate))
    print(transfo(list1, list2, list3))
    print(whowon(gamestate))
    if end==True:#if there is a winner before the ninth turn, the game stop
        break 
    


#the exact same loop for player A
    A=input("A please play an empty case")   
    while A in nodouble or A not in coordinates:
        A=input("A played in an occuped case or an invalid case, please play an other case")
    
    print("A play",A,"your play is valid")
    gamestate.append(A+"A")
    nodouble.append(A)
    print("gamestate is", gamestate)

    vizu(gamestate)
    print(transfo(list1, list2, list3 ))
    print(whowon(gamestate))
    if end==True:
        break
    
    
    counter=counter+1 #to stop the loop


         









  
   
   

