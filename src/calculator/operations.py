import math as m

#simple operations
def add(a):
    return a[0]+a[1]

def sub(a):
    return a[0]-a[1]

def mul(a):
    return a[0]*a[1]

def div(a):
    return a[0]/float(a[1])

def mod(a):
    return a[0]%a[1]

def percentage(a):

    return float(a[0]) / a[1]*100

def mean(a):
    n=len(a)
    sum=multiple_add(a)
    return sum/float(n)


def median(a):
    n=len(a)
    m=n/2

    if(n%2!=0):
        c=a[m]
    else:
        c=(a[m-1]+a[m])/2
    return c
#multiple calculation

def multiple_add(a):
    c=0
    for no in a:
       c += no
    return c

def multiple_sub(a):
    c=0
    for no in a:
        c = no-c
    return c

def multiple_mul(a):
    c=1
    for no in a:
        c = c*no
    return c
def multiple_div(a,no):
    b=[]
    for n in a:
        temp = n/float(no)
        b.append(temp)
    return b

#trignonmetric fonctions
def cos(a):
    return m.cos(a)

def sin(a):
    return m.sin(a)

def tan(a):
    return m.tan(a)

def sec(a):
    return m.acos(a)

def cosec(a):
    return m.asin(a)

def cot(a):
    return m.atan(a)

#squre cube and raise to n

def squre(a):
    return (a*a)

def cube(a):
    return (a*a*a)

def raiseto(x):
    return m.pow(x[0],x[1])

def square_root(a):
    return m.pow(a,1/2)

def cube_root(a):
    return m.pow(a,1/3)

#logrithmic

def log(a):
    return m.log(a)
def logToBase(a): #a[0]=number;a[1]=base
    return m.log(a[0],a[1])
def expo(a):
    return m.exp(a)

#areas
def area_sqaure(side):
    return (side*side)

def area_rectangle(lenght,breadth):
    return (lenght*breadth)

def area_triangle(breadth,hieght):
    return (0.5*breadth*hieght)

def area_circle(radius):
    return(m.pi*radius*radius)

def area_eclipse(longr,shortr):
    return (m.pi*longr*shortr)

def area_polygon(no_side,radius,side):
    return (no_side*side*radius*0.5)

#volumes

def volume_sphere(side):
    vol = 4/3(pow(m.pi,3));
    return vol*m.pow(side,3)

def volume_hemisphere(side):
    vol = 2/3()
    return
def volume_cube(side):
    return pow(side,3)

def volume_cuboid(lenght,breadth,hieght):
    return lenght*breadth*hieght

def volume_cyclinder(radius,hieght):
    return m.pi*radius*radius*hieght

def volume_cone(radius,hieght):
    return m.pi*radius*radius*hieght*1/3

def volume_pyramid(breadth,hieght):
    return 1/3*area_triangle(breadth,hieght)*hieght


