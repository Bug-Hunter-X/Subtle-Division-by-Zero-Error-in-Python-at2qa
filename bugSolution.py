def function_with_uncommon_error(a, b):
    if b == 0:
        return a  # Return a if b is zero
    elif a == 0:
        return b
    else:
        return a / b

result = function_with_uncommon_error(5, 0) 