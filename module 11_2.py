import inspect

def introspection_info(obj):
    return {
        'type': type(obj),
        'attributes': dir(obj),
        'module': inspect.getmodule(obj)
    }

number_info = introspection_info(42)
print(number_info)
