from tkinter import *
from Task1 import Algorithm as alg
from Task1 import Perceptron as p
import tkinter.messagebox as message

obj = Tk()
obj.geometry("750x380")
m = PhotoImage(file = "ba2.png")
C = Canvas(obj, bg="blue", height=700 , width = 700)
bac=PhotoImage(file = "ba2.png")
photoimage= bac.subsample(-1,2)
background_label = Label(obj, image=m)
background_label.place(x=0, y=0, relwidth= 1, relheight=1)
############################ feature & optionmenue

#############################
def run_Bexit():
    bas = vbai.get()
    activation=vAct.get();
    epo = scale_epoc.get()
    rat = scale_learnrate.get()/1000
    numHidden=text1.get();
    numHidden=int(numHidden)
    t=text2.get()
    numNodes = t.split(',')
    for i in range (len(numNodes)):
        numNodes[i]=int(numNodes[i])
    tst = alg.MLP(numHidden, numNodes, epo, rat, bas, activation)
    tst.back_propagation()
    accurcy,ConfusionMatrix=tst.test()



    ob = Toplevel()
    ob.geometry("750x380")
    m1 = PhotoImage(file="neural network.png")
    C = Canvas(ob, bg="blue", height=700, width=700)
    background = Label(ob, image=m)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    bac = PhotoImage(file="ba.png")
    photoim = bac.subsample(-1, 2)

    var1 = StringVar()
    lab1 = Label(ob, textvariable=var1, font=('calibri', 20,'bold italic'))
    var1.set("accuracy")
    lab1.place(x=50, y=100)

    var2 = StringVar()
    lab2 = Label(ob, textvariable=var2, font=('calibri', 15,'bold italic'))
    var2.set("Correct items in class 1")
    lab2.place(x=50, y=150)

    var3 = StringVar()
    lab3 = Label(ob, textvariable=var3, font=('calibri', 15,'bold italic'))
    var3.set("Correct items in class 2")
    lab3.place(x=50, y=200)

    var4 = StringVar()
    lab4 = Label(ob, textvariable=var4, font=('calibri', 15 ,'bold italic'))
    var4.set("Correct items in class 3")
    lab4.place(x=50, y=250)
    ##############################
    res1 = accurcy
    res2 = ConfusionMatrix[0][0]
    res3 = ConfusionMatrix[1][1]
    res4=ConfusionMatrix[2][2]

    var1result = StringVar()
    rlab1 = Label(ob, textvariable=var1result)
    var1result.set(str(res1)+"%")
    rlab1.place(x=270, y=100,height=35)

    var2result = StringVar()
    rlab2 = Label(ob, textvariable=var2result)
    var2result.set(res2)
    rlab2.place(x=270, y=150,height=30)

    var3result = StringVar()
    rlab3 = Label(ob, textvariable=var3result)
    var3result.set(res3)
    rlab3.place(x=270, y=200,height=30)

    var4result = StringVar()
    rlab4 = Label(ob, textvariable=var4result)
    var4result.set(res4)
    rlab4.place(x=270, y=250,height=30)
    ###########################################


#################################

############################
photoimage1= bac.subsample(2,2)
lrate = StringVar()
lratel2 = Label(obj, textvariable=lrate  ,font = ('calibri', 14, 'bold italic'),compound = CENTER)
lrate.set("learning rate")
lratel2.place(x=30, y=320)
scale_learnrate = Scale(obj, from_=0, to=100, orient=HORIZONTAL)
scale_learnrate.set(0)
scale_learnrate.place(x=150 ,y= 320)
###################################
epoc = StringVar()
epocl3 = Label(obj, textvariable=epoc , font = ('calibri', 15, 'bold italic')  ,compound = CENTER )
epoc.set("Epocs")
epocl3.place(x=30, y=270)
scale_epoc = Scale(obj, from_=0, to=1000,orient=HORIZONTAL)
scale_epoc.set(0)
scale_epoc.place(x=150 ,y= 270)
######################################
vbai = StringVar()
bail4 = Label(obj, textvariable=vbai ,  font = ('calibri', 15, 'bold italic'),compound = CENTER)
vbai.set("bais")
bail4.place(x=30, y=205)
###########################
vbai = IntVar()
radiobutton1 = Radiobutton(obj,text="yes",variable=vbai, value=0)
radiobutton2 = Radiobutton(obj,text="No",variable=vbai, value=1)
radiobutton1.place(x = 150, y = 205)
radiobutton2.place(x = 150 , y = 235)

###########################
act = StringVar()
actl = Label(obj, textvariable=act ,  font = ('calibri', 15, 'bold italic'),compound = CENTER)
act.set("Activation Fn")
actl.place(x=30, y=140)
###########################
vAct = IntVar()
radiobutton3 = Radiobutton(obj,text="Sigmoid",variable=vAct, value=0)
radiobutton4 = Radiobutton(obj,text="Hyperbolic",variable=vAct, value=1)
radiobutton3.place(x = 150, y = 140)
radiobutton4.place(x = 150 , y = 170)
###############################
hidden = StringVar()
heddenNo = Label(obj, textvariable=hidden ,  font = ('calibri', 15, 'bold italic'),compound = CENTER)
hidden.set("No of Hedden layers")
heddenNo.place(x=300, y=290)
######
text1=Entry(obj)
text1.place(x=490,y=290,height=30)

###############################
nodes = StringVar()
nodesNo = Label(obj, textvariable=nodes ,  font = ('calibri', 15, 'bold italic'),compound = CENTER)
nodes.set("No of Neurons layers")
nodesNo.place(x=300, y=330)
######
text2=Entry(obj)
text2.place(x=490,y=330,height=30)
####################################
select = StringVar()
selectLable = Label(obj, textvariable=select ,  font = ('Tempus Sans ITC', 15, 'bold italic'),compound = CENTER)
select.set("Please select Back Propagation Parameters")
selectLable.place(x=200, y=40)

B5 = Button(obj,text = "Train" ,  font = ('calibri', 20, 'bold italic' ) ,height=30,width=100 ,  image = photoimage ,compound = CENTER,command=run_Bexit )
B5.place(x=600, y=200)
################

def run_Bwellcom():
    B4.destroy()

Image4 = PhotoImage(file ="neural network.png")
B4 = Button(obj,image =Image4  ,height=380,width=750 ,command=run_Bwellcom )
B4.place(x=0, y=0)

obj.mainloop()