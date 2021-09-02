

def uppercase_decorator(function):
    def decorator(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        value = function(args, kwargs)
        return value.upper()

    return decorator
