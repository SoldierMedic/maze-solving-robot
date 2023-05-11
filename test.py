
def checkSpaces():
    return [0,1,1,0]


if len([index for index, value in enumerate(checkSpaces()) if value == 1]) > 1:
    print("split")
else:
    print('no split')