def android_3(func):
    def wrapper(*args,**kwargs):
        print("executing android_3")
        result = func(*args,**kwargs)
        print("executed android_3")
        return result
    return wrapper
def android_4(func):
    def wrapper(*args,**kwargs):
        print("Executing android_4")
        result = func(*args,**kwargs)
        print("Executed android_4")
        return result
    return wrapper

 
@android_4
@android_3
# @dec_func
def add(x,y):
    return x + y

print(add(5,6))