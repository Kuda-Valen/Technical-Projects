def battery (a):
    charged = 100
    percent = True

    left = charged - a

    if left < 0:
        percent = True
    else:
        percent = False

    return percent
