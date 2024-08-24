
from random import choice
from tkinter import*

rps = ["Rock","Paper","Scissor"]
def play(event):
    
    computer = choice(rps)

    player = event.widget.cget("text")
    playerLabel =Label( frame3,text= player,bg="red", relief=SUNKEN, borderwidth=5,font=("comicsansms 40 bold") )
    playerLabel.grid(row=0,column=0)
    computerLabel =Label( frame3,text=computer,bg="red", relief=SUNKEN, borderwidth=5,font=("comicsansms 40 bold") )
    computerLabel.grid(row=0,column=1)


vanshi_vats=Tk()
#Width X height
vanshi_vats.geometry("850x600")
vanshi_vats.title("Rock Paper Scissor")

frame1 = Frame(vanshi_vats)
frame1.pack()

titlelabel = Label( frame1, text="Rock Paper Scissors",font=("comicsansms 30 bold"))
titlelabel.pack()

frame2 = Frame(vanshi_vats , bg="red")
frame2.pack()
 
playerLabel =Label( frame2,text="Player:_______",bg="red", relief=SUNKEN, borderwidth=5,font=("comicsansms 40 bold") )
playerLabel.grid(row=0,column=0)

computerLabel =Label( frame2,text="Computer:_______",bg="red", relief=SUNKEN, borderwidth=5,font=("comicsansms 40 bold") )
computerLabel.grid(row=0,column=1)

frame3=Frame(vanshi_vats,bg= "red")
frame3.pack()

playerLabel =Label( frame3,text="_______",bg="red", relief=SUNKEN, borderwidth=5,font=("comicsansms 40 bold") )
playerLabel.grid(row=0,column=0)

computerLabel =Label( frame3,text="_______",bg="red", relief=SUNKEN, borderwidth=5,font=("comicsansms 40 bold") )
computerLabel.grid(row=0,column=1)

frame4=Frame(vanshi_vats,bg="skyblue")
frame4.pack()
b1=Button(frame4 , text="Rock", bg="Orange", relief=RAISED, borderwidth=5,font=("comicsansms 40 bold") )
b1.pack()
b1.bind("<Button-1>",play)

b2=Button(frame4 , text="Paper", bg="Orange", relief=RAISED, borderwidth=5,font=("comicsansms 40 bold") )
b2.pack()
b2.bind("<Button-1>",play)

b3=Button(frame4 , text="Scissor", bg="Orange", relief=RAISED, borderwidth=5,font=("comicsansms 40 bold") )
b3.pack()
b3.bind("<Button-1>",play)
frame4.pack()

frame5 =Frame(vanshi_vats, bg="Yellow")
frame5.pack()
Winnerlabel =Label(frame5, text=" Winner", relief=SUNKEN, borderwidth=5,font=("Ariel",40))
Winnerlabel.pack()  

vanshi_vats.mainloop()