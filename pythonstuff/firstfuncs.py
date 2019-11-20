#Functions exercise

def double_it(number):
    return number * 2

#Hypotenuse function

def calc_hypo(a,b) :
    if type(a) not in (int,float) or type(b) not in (int,float) :
        print("not float or integer")
    if a <= 0 or b <= 0 :
        print("Bad argument")
        return False
    c = (a**2 + b**2)**0.5
    return c 




