import matplotlib.pyplot as plt
import  Task1.Perceptron as p

def plotting ():
    X1,X2,X3,X4,ClassName =p.load_data()

    # X1,X2
    setosaX = X1[0:50]
    setosaY = X2[0:50]
    versicolorX = X1[50:100]
    versicolorY = X2[50:100]
    virginicaX = X1[100:150]
    virginicaY = X2[100:150]
    plt.xlabel('X1', fontsize=20)
    plt.ylabel('X2', fontsize=20)
    plt.scatter(setosaX, setosaY)
    plt.scatter(versicolorX, versicolorY)
    plt.scatter(virginicaX, virginicaY)
    plt.show()

    #X1,X3
    setosaX=X1[0:50]
    setosaY=X3[0:50]
    versicolorX=X1[50:100]
    versicolorY=X3[50:100]
    virginicaX=X1[100:150]
    virginicaY=X3[100:150]
    plt.xlabel('X1', fontsize=20)
    plt.ylabel('X3', fontsize=20)
    plt.scatter(setosaX, setosaY)
    plt.scatter(versicolorX,versicolorY)
    plt.scatter(virginicaX,virginicaY)
    plt.show()

    #X1,X4
    setosaX = X1[0:50]
    setosaY = X4[0:50]
    versicolorX = X1[50:100]
    versicolorY = X4[50:100]
    virginicaX = X1[100:150]
    virginicaY = X4[100:150]
    plt.xlabel('X1', fontsize=20)
    plt.ylabel('X4', fontsize=20)
    plt.scatter(setosaX, setosaY)
    plt.scatter(versicolorX, versicolorY)
    plt.scatter(virginicaX, virginicaY)
    plt.show()

    #X2,X3
    setosaX = X2[0:50]
    setosaY = X3[0:50]
    versicolorX = X2[50:100]
    versicolorY = X3[50:100]
    virginicaX = X2[100:150]
    virginicaY = X3[100:150]
    plt.xlabel('X2', fontsize=20)
    plt.ylabel('X3', fontsize=20)
    plt.scatter(setosaX, setosaY)
    plt.scatter(versicolorX, versicolorY)
    plt.scatter(virginicaX, virginicaY)
    plt.show()

    # X2,X4
    setosaX = X2[0:50]
    setosaY = X4[0:50]
    versicolorX = X2[50:100]
    versicolorY = X4[50:100]
    virginicaX = X2[100:150]
    virginicaY = X4[100:150]
    plt.xlabel('X2', fontsize=20)
    plt.ylabel('X4', fontsize=20)
    plt.scatter(setosaX, setosaY)
    plt.scatter(versicolorX, versicolorY)
    plt.scatter(virginicaX, virginicaY)
    plt.show()

    # X3,X4
    setosaX = X3[0:50]
    setosaY = X4[0:50]
    versicolorX = X3[50:100]
    versicolorY = X4[50:100]
    virginicaX = X3[100:150]
    virginicaY = X4[100:150]
    plt.xlabel('X3', fontsize=20)
    plt.ylabel('X4', fontsize=20)
    plt.scatter(setosaX, setosaY)
    plt.scatter(versicolorX, versicolorY)
    plt.scatter(virginicaX, virginicaY)
    plt.show()
plotting()