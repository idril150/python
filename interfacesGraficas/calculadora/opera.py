def calculos(a,b,op):
    match op:
        case "+":
            print(f"{a}+{b}")
            return a+b
        case "-":
            print(f"{a}-{b}")
            return a-b
        case "*":
            print(f"{a}*{b}")
            return a*b
        case "/":
            print(f"{a}/{b}")
            return a/b
        case "**":
            print(f"{a}**{b}")
            return a**b

def calculo(buss,opc):
    a=buss.pop(0)
    b=opc.pop(0)
    vuelta=1
    cal=calculos(a,buss[0],b)
    for op in opc:
        cal=calculos(cal,buss[vuelta],op)
        vuelta+=1
    return cal