from tkinter import *
from Task1 import Perceptron as p
import tkinter.messagebox as message

obj = Tk()
obj.geometry("800x800")
m = PhotoImage(file = "background1.png")
C = Canvas(obj, bg="blue", height=700 , width = 700)
bac=PhotoImage(file = "ba.png")
photoimage= bac.subsample(-1,2)
background_label = Label(obj, image=m)
background_label.place(x=0, y=0, relwidth= 1, relheight=1)
############################ feature & optionmenue
fet1 = StringVar()
Ifet1lable = Label(obj, textvariable=fet1 ,font =  ('calibri', 20, 'bold') , image = photoimage ,compound = CENTER)
fet1.set("feature1 " )
Ifet1lable.place(x=130, y=500)
variable1 = StringVar(obj)
option = ["X1", "X2", "X3" ,"X4"]
optionmenu1 = OptionMenu(obj,variable1, *option)
optionmenu1.place(x=270 , y= 500)
fet2 = StringVar()
Ifet2lable = Label(obj,textvariable=fet2,font = ('calibri', 20, 'bold') , image = photoimage ,compound = CENTER)
fet2.set("feature2 ")
Ifet2lable.place(x=410, y=500)
variable2 = StringVar(obj)
option2 = ["X1", "X2", "X3" ,"X4"]
optionmenu2 = OptionMenu(obj,variable2, *option2)
optionmenu2.place(x=550 , y= 500)
#############################
def run_Bexit():
    f1 = variable1.get()
    f2 = variable2.get()
    if f1 == variable2.get():
        message.showinfo("some thing wrong", "You can't select the same Feature,Run Again")
    bas = v.get()
    if bas == 1:
        bas = "yes"
    elif bas == 2:
        bas = "no"
    epo = scale_epoc.get()
    rat = scale_learnrate.get()/1000
    if  x == "" :
        clas1 ="Iris-versicolor"
        clas2="Iris-virginica"
    elif x1 =="":
        clas1="Iris-setosa"
        clas2 = "Iris-virginica"
    elif x2 == "":
        clas1 = "Iris-setosa"
        clas2 = "Iris-versicolor"
    ConfusionMatrix, accurcy=p.Preprocssing(clas1, clas2, f1, f2, epo, rat, bas)

    ob = Toplevel()
    ob.geometry("400x400")
    m1 = PhotoImage(file="background1.png")
    C = Canvas(ob, bg="blue", height=700, width=700)
    background = Label(ob, image=m)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    bac = PhotoImage(file="ba.png")
    photoim = bac.subsample(-1, 2)

    var1 = StringVar()
    lab1 = Label(ob, textvariable=var1, font=('calibri', 20))
    var1.set("accuracy")
    lab1.place(x=50, y=100)

    var2 = StringVar()
    lab2 = Label(ob, textvariable=var2, font=('calibri', 15))
    var2.set("Wrong item in class 1")
    lab2.place(x=50, y=150)

    var3 = StringVar()
    lab3 = Label(ob, textvariable=var3, font=('calibri', 15))
    var3.set("Wrong item in class 2")
    lab3.place(x=50, y=200)

    ##############################
    res1 = accurcy
    res2 = ConfusionMatrix[0][1]
    res3 = ConfusionMatrix[1][0]
    var1result = StringVar()
    rlab1 = Label(ob, textvariable=var1result)
    var1result.set(str(res1)+"%")
    rlab1.place(x=250, y=100)

    var2result = StringVar()
    rlab2 = Label(ob, textvariable=var2result)
    var2result.set(res2)
    rlab2.place(x=250, y=150)

    var3result = StringVar()
    rlab3 = Label(ob, textvariable=var3result)
    var3result.set(res3)
    rlab3.place(x=250, y=200)

    ###########################################
    def B1():
        p.Show()

    Buttonshow = Button(ob, text="show plot ", font=('calibri', 15, 'bold'), command=B1)
    Buttonshow.place(x=260, y=300)

#################################
def run_B1():
    c1 = StringVar()
    I = Label(obj, textvariable=c1 )
    c1.set("Iris-setosa")
    I.place(x=70, y=450)
    global x
    x=1

Image1 = PhotoImage(file = "Setosa.png")
B = Button(obj,image =Image1  ,height=200,width=200 ,command=run_B1 )
B.place(x=50, y=200)
x=""
x1=""
x2=""
#############################
def run_B2():
    c2 = StringVar()
    I2 = Label(obj, textvariable=c2 )
    c2.set("Iris-versicolor")
    I2.place(x=350, y=450)
    global x1
    x1=1
Image2 = PhotoImage(file = "Versicolor.png")
B2 = Button(obj,image =Image2  ,height=200,width=200 ,command=run_B2 )
B2.place(x=300, y=200)
####################################
def run_B3():
    c3 = StringVar()
    I3 = Label(obj, textvariable=c3 )
    c3.set("Iris-virginica")
    I3.place(x=550, y=450)
    global x2
    x2=1

Image3 = PhotoImage(file = "Virginica.png")
B3 = Button(obj,image =Image3  ,height=200,width=200 ,command=run_B3 )
B3.place(x=550, y=200)
###############################
Iris_Flower  = StringVar()
Iris= Label(obj, textvariable=Iris_Flower , font = ('calibri', 20, 'bold')  )
Iris_Flower.set("Please select 2 Iris Flower for trining  ")
Iris.place(x=210, y=120)
############################
photoimage1= bac.subsample(2,2)
lrate = StringVar()
lratel2 = Label(obj, textvariable=lrate  ,font = ('calibri', 14, 'bold'),  image = photoimage ,compound = CENTER)
lrate.set("learning rate")
lratel2.place(x=70, y=570)
scale_learnrate = Scale(obj, from_=0, to=100, orient=HORIZONTAL)
scale_learnrate.set(0)
scale_learnrate.place(x=70 ,y= 630)
###################################
epoc = StringVar()
epocl3 = Label(obj, textvariable=epoc , font = ('calibri', 15, 'bold') ,  image = photoimage1 ,compound = CENTER )
epoc.set("Epocs")
epocl3.place(x=380, y=570)
scale_epoc = Scale(obj, from_=0, to=1000,orient=HORIZONTAL)
scale_epoc.set(0)
scale_epoc.place(x=380 ,y= 630)
######################################
bai = StringVar()
bail4 = Label(obj, textvariable=bai ,  font = ('calibri', 15, 'bold') ,  image = photoimage1 ,compound = CENTER)
bai.set("bais")
bail4.place(x=600, y=570)
###########################
v = IntVar()
radiobutton1 = Radiobutton(obj,text="yes",variable=v, value=1)
radiobutton2 = Radiobutton(obj,text="No",variable=v, value=2)
radiobutton1.place(x = 670 , y = 570)
radiobutton2.place(x = 670 , y = 595)
###########
B5 = Button(obj,text = "Train" ,  font = ('calibri', 20, 'bold' ) ,height=30,width=100 ,  image = photoimage ,compound = CENTER,command=run_Bexit )
B5.place(x=630, y=650)
################
def run_Bwellcom():
    B4.destroy()

Image4 = PhotoImage(file = "back .png")
B4 = Button(obj,image =Image4  ,height=790,width=800 ,command=run_Bwellcom )
B4.place(x=0, y=0)

obj.mainloop()