import math


def getMultiElmt(modular, startNum):

    #created a list with element 1 in there alredy
    #as there will be 1 any mutiplicative group
    list = []
    condition = False
    primeNums = [2,3,5,7,11,13,17,23]

    for index in range(startNum, modular):

        #for i in range(0, len(primeNums)):

        if (findGcd(modular,index) == 1):
            condition = True
        else:
            condition = False
            i = len(primeNums)


        if(condition):
            list.append(index)

    return list


def findGcd(a,b):
    if (b == 0):
        return a
    else:
        return findGcd(b, a % b)


def getOrd(list, modular):
    ordList = []
    counter = 0;
    condition = True
    temp = 0
    for index in range(0, len(list)):

       while True:
           if(counter == 0 ):
               counter += 1
               temp = list[index]
           else:
               temp = (temp * list[index]) % modular

               if(temp == list[index]):
                    break
               else:
                   counter +=1

       ordList.append(counter)
       counter = 0


def getBinary(n):
    binaryVal = []
    print("Binary Value of", n, end=" is: ")

    while(n > 0):
        if(n%2 == 0):
            binaryVal.append(0)
        else:
            binaryVal.append(1)

        n = int(n / 2)

    binaryVal.reverse()
    print(binaryVal)
    binaryVal.append(-1)
    return binaryVal


def sqAndMul(counter, x, exp, mod, r, binaryValue):

    if(binaryValue[counter] == -1):
        return r

    r = (r*r)%mod
    if(binaryValue[counter] == 1):
        r = (r * x)%mod
        counter += 1
        return sqAndMul(counter, x, exp, mod, r, binaryValue)
    else:
        counter += 1
        return sqAndMul(counter, x, exp, mod, r, binaryValue)


def main():

    use = int(input("Enter 1 to use it for Multiplicative group"
                "\n      2 to find result using square and multiply method. "))
    if(use == 1):
        modular = int(input("Enter a modular or p (Zp): "))
        startNum = int(input("Start group from 0 or 1? "))

        list = getMultiElmt(modular, startNum)
        print("Elements in group Z",modular,": ", list, sep="")
        print("modular is: ", modular)

        getOrd(list, modular)
        print(list)
    else:
        print('********(base^exponent) mod moular********')
        x = int(input("Base(α): "))
        beta = int(input("Exponent(ß): "))
        mod = int(input("Modular(p): "))

        #getting the value of exponent (x)
        exp = int(math.log(beta)/math.log(x))

        print("\nResults:--------------------------")
        binaryValue = getBinary(exp)

        a = sqAndMul(0, x, exp, mod, 1, binaryValue)

        print(x, "^", exp, " mod ", mod, " = ", a, " mod ", mod,sep="")

if __name__ == '__main__':
    main()
