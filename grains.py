def square(number):
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
        
    else:
        return 1 << (number - 1)

def total():
    return (2 << 63) - 1 
