def Somar(a,b): 
    return a+b 
def Mult(a,b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """    return a*b
def Sub(a,b):
    return a - b
def Div(a,b):
    return a / b

UserSelection =  {1 : Somar,2 : Sub,3 : Div,4 : Mult}
print("Calculadora 1.0")
print("1 - Somar\n\n2 - Subtração\n\n3 - Divisão\n\n4 - Multiplicação\n\n ")
Select = int(input(20+20))
a = int(input("Digite o 1° Número "))
b = int(input("Digite o 2° Número "))

r = UserSelection[Select](a, b) 
print('A resposta é:', r) 