import random

def forwardMultiplyGate(x, y):
    return x * y

print forwardMultiplyGate(-2, 3);


def simpleTraining():
    x = -2
    y = 3
    best_out = float("-inf")
    tweak_amount = 0.001

    for i in range(0, 100):
        x_try = x + tweak_amount * (random.random() * 2 - 1)
        y_try = y + tweak_amount * (random.random() * 2 - 1)
        out = forwardMultiplyGate(x_try, y_try)
        if out > best_out:
            best_out = out
            best_x = x_try; best_y = y_try


    print best_x, best_y
    print forwardMultiplyGate(x_try, y_try)

simpleTraining()



