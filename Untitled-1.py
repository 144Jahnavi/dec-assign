def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execution {i + 1}:")
                result = func(*args, **kwargs)
            # return result
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Jahnavi")

