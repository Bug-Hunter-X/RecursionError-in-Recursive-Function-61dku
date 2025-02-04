def function(x):
    if x == 0:
        return 0
    else:
        return function(x-1) + x