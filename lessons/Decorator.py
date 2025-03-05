from datetime import datetime
def run_time(func):
    def wrapper(*arks):
        time_begin = datetime.now()
        result = func(*arks)
        time_end = datetime.now()
        print(time_end - time_begin)
        return result
    return wrapper

@run_time
def my_func():
    for i in range(100000):
     print("hello",i)

#my_func()



my_dict = {}

def cache(func):
        def wrapper(num):
          if(my_dict.get(num)!= None):
              return my_dict.get(num)
          else:
             res = func(num)
             my_dict[num] = res
             return  res
        return wrapper


@run_time
@cache
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_iterative(12308))
print(fibonacci_iterative(12308))

