##基本有序适用
list=[2,4,6,7,8,9,11,13,15,19,22,30]
def func1(list,a):

    ##查找中间位置下标
    left=0
    right=len(list)-1
    mid=(left+right)//2
    print(mid)
    #中间的值
    b=list[mid]
    print(b)
    while left<=right:
        if a==b:
            print("找到该数字")
            break
        elif a>b:
            print("在后半段查找")
            left=mid+1

        elif a<b:
            print("在前半段查找")
            right=mid-1

        mid=(left+right)//2
        print("新的中间位置下表为", mid)
        b=list[mid]
        print("新的中间位置数为",b)
    if left>right:
        print("没有找到该数字")
func1(list=list,a=19)