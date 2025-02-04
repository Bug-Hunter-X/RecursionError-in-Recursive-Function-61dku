def function(x):
    if x == 0:
        return 0
    elif x < 0:
        return 0  # Handle negative inputs to prevent infinite recursion
    else:
        return function(x-1) + x