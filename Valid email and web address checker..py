input1=int(input("Enter the number   "))
list1=[]

for item in range(0,input1):
    string= input("Enter your address   ")
    list1.append(string)

domainlist=open('Dlist','r')
Domain=domainlist.read()


for idx,item in enumerate(list1):
    if(item.__contains__('@')):
        email=item
        splitter = email.split('@')
        leftpart = splitter[:1]
        rightpart = splitter[1:]

        DMN = ''
        for i in rightpart:
            for item in i:
                DMN = DMN + item
        D = DMN.split('.')


        def startingChecker(LP):
            for item in LP[0]:
                if (item[0].isnumeric() or item[0].isupper()):
                    return False
                else:
                    return True


        startingChecker(leftpart)


        def domainChecker(RP):

            if (RP[-1] not in Domain):
                return False
            else:
                return True


        domainChecker(D)

        if (startingChecker(leftpart) and domainChecker(D)):
            print('The email address is valid given in line , ', idx+1 )
        else:
            print('The email address is not valid given in line' , idx+1 )
    else:
        web=item
        splitter1 = web.split('.')

        firstpart = splitter1[:1]
        lastpart = splitter1[-1:]


        def startChecker(FP):
            if (FP[0] != 'www'):
                return False
            else:
                return True


        startChecker(firstpart)


        def endChecker(LP):
            if (LP[0] not in Domain):
                return False
            else:
                return True


        endChecker(lastpart)

        if (startChecker(firstpart) and endChecker(lastpart)):
            print('Web address is valid given in line , ', idx+1)
        else:
            print('Web address is not valid given in line', idx+1)