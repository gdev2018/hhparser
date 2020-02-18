import time

def my_timer(f):
    def tmp(*args, **kwargs):
        start_time=time.time()
        result=f(*args, **kwargs)
        delta_time=time.time() - start_time
        print ('Время выполнения функции {}' .format(delta_time))
        return result

    return tmp


@my_timer
def my_sum(x, y, z):
    return x + y + z

print (my_sum(4, 5, 7))