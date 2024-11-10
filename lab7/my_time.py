import time

def show_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        res = end_time - start_time
        print('Time: ', res)
        return res
    return wrapper
@show_time
def main():
    def send_message(message):
        pass
    def reply(message):
        print(message)
