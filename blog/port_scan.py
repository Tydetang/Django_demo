from socket import *
import threading

setdefaulttimeout(3)

class MyThread(threading.Thread):

    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args
        self.ip_dict = {}

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            key = self.args[1]
            self.ip_dict[key] = self.result
            return self.ip_dict
            # return self.ip_dict[key]+':'+self.result
        except Exception:
            pass


def foo(host,port):
    s = socket(AF_INET,SOCK_STREAM)
    num = s.connect_ex((host,port))
    if num == 0:
        return 'open'
    s.close()

def main(url,s_p,e_p):
    li = []
    result = {}
    for i in range(int(s_p),int(e_p)):
        t = MyThread(foo,args=(url,int(i)))
        li.append(t)
        t.start()

    for t in li:
        t.join() #主线程比子线程跑的快，会拿不到结果
        result.update(t.get_result())

    return result

