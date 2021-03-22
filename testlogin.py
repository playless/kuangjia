
#创建测试类
class TestLogin:
    #定义属性
    def __init__(self,username,password):
        self.username=username
        self.password=password
    #定义方法
    def test_login(self):
        print(self.username)
class TestZhuCe(TestLogin):
    def __init__(self,username,password,email):
        TestLogin.__init__(self,username,password)
        #定义子类的属性
        self.email=email

if __name__ == '__main__':
    userame="potato"
    password="123456"
    email="2222@qq.com"
    t=TestZhuCe(userame,password,email)
    print(t.username)
    t.test_login()