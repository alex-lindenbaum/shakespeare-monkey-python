import random

def randomElement(arr, lower=0, upper='ARR_LENGTH'):
    # Picks from [lower, upper]
    if upper == 'ARR_LENGTH':
        upper = len(arr) - 1

    index = random.randint(lower, upper)
    return arr[index]