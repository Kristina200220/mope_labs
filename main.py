import random
A0 = 3
A1 = 4
A2 = 2
A3 = 1
Ydif = []
Yresult = []
X1 = [random.randrange(0,20,1) for i in range(8)]
X2 = [random.randrange(0,20,1) for i in range(8)]
X3 = [random.randrange(0,20,1) for i in range(8)]
Y = [A0 + A1*X1[i] + A2*X2[i] + A3*X3[i] for i in range(8)]
X01 = (max(X1)+min(X1))/2
X02 = (max(X2)+min(X2))/2
X03 = (max(X3)+min(X3))/2
dX1 = X01-min(X1)
dX2 = X02-min(X2)
dX3 = X03-min(X3)
Xn1 = [round(((X1[i] - X01)/dX1),3) for i in range(8)]
Xn2 = [round(((X2[i] - X02)/dX2),3) for i in range(8)]
Xn3 = [round(((X3[i] - X03)/dX3),3) for i in range(8)]
Yet = A0 + A1*X01 + A2*X02 + A3*X03

def average(number):
    Sum = 0
    for i in number:
        Sum+=i
    Sum = Sum/8
    return Sum
result = average(Y)
for i in range(8):
    difference = Y[i] - result
    Ydif.append(difference)
for d in Ydif:
    if d > 0:
        Yresult.append(d)
    otvet = result + min(Yresult)
print("A0=%s A1=%s A2=%s A3=%s"%(A0, A1, A2, A3))
print("X1: %s"%X1)
print("X2: %s"%X2)
print("X3: %s"%X3)
print("Y: %s"%Y)
print("x0: %s %s %s"%(X01, X02, X03))
print("dx: %s %s %s"%(dX1, dX2, dX3))
print("Xн1: %s"%Xn1)
print("Xн2: %s"%Xn2)
print("Xн3: %s"%Xn3)
print("Yэт: %s"%Yet)
print("Відповідь: %s"%otvet)

