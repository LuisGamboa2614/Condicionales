a=int(input("Escriba su edad: "))
b=int(input("Escriba la edad de su mamá: "))
c=float(input("Escriba su calificación: "))
d=float(input("Escriba su calificación: "))
e=(input("Escriba que color prefiere entre azul y rojo: "))
f=(input("Escriba en que color esta el semáforo: "))
if (a<18):
    print(f"Usted es menor de edad con {a}")
if (b>18):
    print(f"Su mamá es mayor de edad con {b} años")
if (c>=3):
    print(f"Usted paso la materia con {c}")
if (d<=2.9):
    print("Usted esta en riesgo de reprobar con ",d)
if (e=="rojo"):
    print("Luis también prefiere el ",e)
if (f!="verde"):
    print("Usted no puede seguir si esta en ",f)