def fat(num):
    if num == 0:
        return 1
    else:
        return num * fat(num-1)
fat(5)


def soma_aritimedica(num):
    if num == 1:
        return 1
    else:
        return num + fibonnaci(num -1)

soma_aritimedica(7)

def fibonnaci(num):
    if num == 1:
        return num
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)

fibonnaci(10)
