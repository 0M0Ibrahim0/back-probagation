import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
def Preprocssing (Class1,Class2,feature1,feature2,epochs ,learning_Rate,bias):

        #extract classes & features
        X1,X2,X3,X4,ClassName=load_data()
        X_Dictionary={"X1":X1,"X2":X2,"X3":X3,"X4":X4}
        ClassName1=[]
        ClassName2=[]
        feature1_C1=[]
        feature2_C1=[]
        feature1_C2=[]
        feature2_C2=[]
        for i in range (len(ClassName)) :
                if ClassName[i]==Class1:
                        ClassName1.append(-1);
                        feature1_C1.append(X_Dictionary[feature1][i])
                        feature2_C1.append(X_Dictionary[feature2][i])
                if ClassName[i]==Class2:
                        ClassName2.append(1);
                        feature1_C2.append(X_Dictionary[feature1][i])
                        feature2_C2.append(X_Dictionary[feature2][i])

        #split traning & test
        X1_trainC1, X1_testC1,X2_trainC1, X2_testC1, y_trainC1, y_testC1 =train_test_split(feature1_C1,feature2_C1, ClassName1, test_size=0.40,shuffle=True)
        X1_trainC2, X1_testC2,X2_trainC2, X2_testC2, y_trainC2, y_testC2 =train_test_split(feature1_C2,feature2_C2, ClassName2, test_size=0.40,shuffle=True)

        x1,x2,y=shuffle(X1_trainC1+X1_trainC2,X2_trainC1+X2_trainC2,y_trainC1+y_trainC2)

        weights=perceptron(x1,x2,y,epochs,learning_Rate,bias)

        #draw line
        draw_line(feature1_C1,feature2_C1,feature1_C2,feature2_C2,weights)

        #evaluation & test
        ConfusionMatrix, accurcy=evaluation(X1_testC1+X1_testC2 ,X2_testC1+X2_testC2 ,y_testC1+y_testC2,weights)

        return ConfusionMatrix, accurcy
def Show ():
        plt.show()

def load_data():
        X1 = []
        X2 = []
        X3 = []
        X4 = []
        ClassName = []

        file_name = open("E:\\books\\last year\\ANN\\Labs\\Lab3\\Task\\Task1\\IrisData.txt", "r")
        file_name.readline();
        for line in file_name:
                split_line = line.split(",")
                X1.append(float(split_line[0]))
                X2.append(float(split_line[1]))
                X3.append(float(split_line[2]))
                X4.append(float(split_line[3]))
                c=split_line[4].split("\n");
                ClassName.append(c[0])
        return X1,X2,X3,X4,ClassName

def perceptron (feature1 , feature2 ,y,epochs ,learning_Rate,bias):
        w1 = np.random.uniform(-1, 1)
        w2 = np.random.uniform(-1, 1)
        if bias=="yes":
                b=np.random.uniform(-1, 1)
                Weights = [b,w1, w2]
        else:
                Weights = [w1, w2]
        for j in range (epochs):
                for i in range (len(feature1)):
                        input_vector=[feature1[i],feature2[i]]
                        if bias=="yes":
                                input_vector =[ 1, feature1[i],feature2[i]]
                        signum_value=sum(np.multiply(input_vector,Weights))
                        expected_y= signum (signum_value)
                        loss=y[i]-expected_y
                        Weights=Weights+(np.multiply(learning_Rate*loss,input_vector))
        return Weights

def signum(signum_value):
        if signum_value<0 :
                return -1
        if signum_value>=0:
                return 1
def draw_line (Class1_x,Class1_y,Class2_x,Class2_y,weights):
        b=0
        if len(weights)==3:
                y=np.multiply((-weights[1]/weights[2]),Class1_x )-(weights[0]/weights[2])
        else:
                y = np.multiply((-weights[0] / weights[1]),Class1_x)
        plt.scatter(Class1_x, Class1_y)
        plt.scatter(Class2_x, Class2_y)
        plt.xlabel('feature1', fontsize=20)
        plt.ylabel('feature2', fontsize=20)
        plt.plot(Class1_x, y, color='red', linewidth=3)
def test (feature1_sample , feature2_sample ,weights):
        input_vector = [feature1_sample, feature2_sample]
        if len(weights)>2:
                input_vector = [1, feature1_sample, feature2_sample]
        signum_value=sum(np.multiply(input_vector,weights))
        expected_class=signum(signum_value)
        return expected_class
def evaluation (feature1_test,feature2_test,actualOut_test,weights):
        negative=0
        postive=0
        for i in range (len(actualOut_test)):
                expected_class = test(feature1_test[i],feature2_test[i],weights)
                if actualOut_test[i]!=expected_class:
                        if expected_class==1:
                                negative+=1
                        else:
                                postive+=1
        ConfusionMatrix =[[(len(actualOut_test)/2)-negative , negative],
                          [  postive,(len(actualOut_test)/2)-postive]]
        s=(len(actualOut_test)/2)
        accurcy=((s-postive +s-negative)/len(actualOut_test))*100
        print(ConfusionMatrix)
        return ConfusionMatrix ,accurcy

#Preprocssing("Iris-setosa","Iris-versicolor","X1","X2",1000,0.2,"yes")