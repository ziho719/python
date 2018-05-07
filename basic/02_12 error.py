import math

while True:
    try:
        text=input('>')
        if text[0] == 'q':
            break
        x=float(text)
        y=1 / math.log10(x)
        print("1/log10({0}) ={1}".format(x,y))
    except ValueError:
        print( "the value must be greater than 0")
    except ZeroDivisionError as e:
        print("zero division!")
        print(e)
    except Exception:
        print("unexpectied error")  #直接拍enter

