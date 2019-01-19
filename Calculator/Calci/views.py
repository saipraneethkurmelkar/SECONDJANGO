from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests,"Calci/home.html")



def calc(requests):
    field1=int(requests.GET['field1'])
    field2 =int(requests.GET['field2'])
    operation=requests.GET['optradio']
    result=0
    if operation=='+':
        result= field1 + field2
    if operation=='-':
        result=field1 - field2
    if operation=='*':
        result=field1 * field2
    if operation=='/':
        result=field1 / field2
    return render(requests,"Calci/calc.html",{'result':result})






