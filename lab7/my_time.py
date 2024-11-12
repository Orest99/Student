import time
def show_time(func):
    def wrapper(bot,message,text,buttons):
        t1 = time.time()
        res = func(bot,message,text,buttons)
        t2 = time.time()
        result = t2-t1
        print('Time: ',result)
        return res
    return wrapper

