for i in range(1,10):
    for j in range(1,i+1):
        #\t 制表符，格式字节宽度一样  \n 换行符
        print(j,"*",i,"=",j * i,"\t",end='    ')
    print('')


