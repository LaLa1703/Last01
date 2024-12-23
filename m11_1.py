import sys

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['class'] = obj.__class__.__name__
    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
    info['methods'] = [func for func in dir(obj) if callable(getattr(obj, func))]
    info['is_instance'] = isinstance(obj, type)
    info['module'] = obj.__module__ if hasattr(obj, '__module__') else None

    return info

number_info = introspection_info(42)
print(number_info)
