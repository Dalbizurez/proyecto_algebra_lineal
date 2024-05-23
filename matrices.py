import math

pasos = []

def steps():
    return pasos

def clean_steps():
    global pasos
    pasos = []

class Cipher:
    def __init__(self,  key:list[list]= None) -> None:
        self.key = key
        self.adjkey = None
        self.coded = None

    def setKey(self, key:list[list]):
        self.key = key
        self.adjkey = inversa_gj(key)

    def code(self, txt:list[list]):
        if not self.key:
            return
# Pasos
        pasos.append("Matriz a codificar")
        pasos.append("\n".join(str(x) for x in txt))
        pasos.append("\n")
        pasos.append("Matriz clave")
        pasos.append("\n".join(str(x) for x in self.key))
        pasos.append("\n")
        self.coded = multiplicacion(self.key, txt)
# Pasos
        pasos.append("Matriz codificada")
        pasos.append("\n".join(str(x) for x in self.coded))
        pasos.append("\n")
        return self.coded
    
    def decipher(self, message = None):
        if not self.key:
            return
        message = message if message else self.coded
# Pasos
        pasos.append("Matriz a decodificar")
        pasos.append("\n".join(str(x) for x in message))
        pasos.append("\n")
        pasos.append("Para obtener la matriz original multiplicamos la matriz codificada por la matriz inversa de la clave")
        if not self.adjkey:
            self.adjkey = inversa_gj(self.key)
# Pasos
        pasos.append("Matriz inversa de la clave")
        pasos.append("\n".join(str(x) for x in self.adjkey))
        pasos.append("\n")
        return multiplicacion(self.adjkey,message)
    
    def getCoded(self):
        return self.coded

def determinante_gauss(matriz:list[list]):
    matriz = gauss(matriz)
# Pasos
    pasos.append("Matriz escalonada por Gauss")
    pasos.append("\n".join(str(x) for x in matriz))
    pasos.append("\n")
    determinante = 1
    pasos.append("Para obtener el determinante multiplicamos los valores de la diagonal principal")
    txt = ""
    for x in range(len(matriz)):
        txt += f"{matriz[x][x]} * "
        determinante *= matriz[x][x]
    pasos.append(txt[:-2])
    pasos.append("\n") 
    return determinante

def determinante(matriz:list[list]):
    matriz = [matriz[x].copy() for x in range(len(matriz))]
    for x in range(len(matriz)-1):
        matriz.append(matriz[x])
        
    determinante = 0
    times = int((len(matriz)+ (1 if len(matriz) % 2 == 1 else 0))/2)
    for x in range(times):
        pos = 1
        neg = 1
        for y in range(len(matriz[0])):
            pos *= matriz[x+y][y] 
            neg *= matriz[x+y][-y] 
        determinante += pos
        determinante -= neg

    return determinante

def cuadrada(matriz:list[list]):
    cols = len(matriz[0])
    rows = len(matriz)
# Pasos
    pasos.append("Matriz")
    pasos.append("\n".join(str(x) for x in matriz))
    pasos.append("\n")
    pasos.append(f"Filas: {rows}")
    pasos.append(f"Columnas: {cols}")
    pasos.append("Si son iguales la matriz es cuadrada")
    pasos.append(f"Resultado: {cols == rows}")
    pasos.append("\n")

    return cols == rows

def inversa_gj(matriz:list[list]):
    if determinante_gauss(matriz) == 0:
        return 0
    if not cuadrada(matriz):
        return -1
    matriz = [matriz[x].copy() for x in range(len(matriz))]

# Pasos
    pasos.append("Matriz original")
    pasos.append("\n".join(str(x) for x in matriz))
    pasos.append("\n")
    pasos.append("Matriz identidad")
    pasos.append("\n".join(str(x) for x in [[1 if x == y else 0 for y in range(len(matriz))] for x in range(len(matriz))]))
    pasos.append("\n")
    pasos.append("Matriz extendida")

    for r in range(len(matriz)):
        row =  matriz[r]
        for n in range(len(row)):
            row.append(1 if r == n else 0)

# Pasos
    pasos.append("\n".join(str(x) for x in matriz))
    pasos.append("\n")

    extendida = gauss_jordan(matriz)
    inversa = []
    for row in extendida:
        inversa.append(row[int(len(row)/2):])

# Pasos
    pasos.append("Matriz inversa")
    pasos.append("\n".join(str(x) for x in inversa))

    return inversa
    for eq in range(0, len(matriz)):
        pivot = matriz[eq]
        for x in range(eq+1, len(matriz)):
            multiplicador1 = pivot[eq] * (1 if pivot[eq] > 0 else -1)

            multiplicador2 = (matriz[x][eq] * (1 if matriz[x][eq] > 0 else -1)) * (1 if matriz[x][eq] * pivot[eq] < 0 else -1)

            for y in range(len(matriz[x])):
                matriz[x][y] *= multiplicador1
                sumando = pivot[y] * multiplicador2
                matriz[x][y] += sumando

    for eq in range(len(matriz)-1, -1, -1):
        pivot = matriz[eq]
        variable = eq
        constant = -1
        if pivot[eq] != 1 and pivot[eq] != 0:
            val =  pivot[eq]
            for x in range(len(pivot)):
                pivot[x] /= val
        for x in range(eq-1, -1, -1):
            multiplicador1 = pivot[eq] * (1 if pivot[eq] > 0 else -1)

            multiplicador2 = (matriz[x][eq] * (1 if matriz[x][eq] > 0 else -1)) * (1 if matriz[x][eq] * pivot[eq] < 0 else -1)

            for y in range(len(matriz[x])):
                matriz[x][y] *= multiplicador1
                sumando =  pivot[y] * multiplicador2
                matriz[x][y] += sumando

    
    return matriz   

def multiplicacion(a:list[list], b:list[list]):
    if len(a[0]) != len(b):
        return
    res = [[0 for cols in range(len(b[0]))].copy() for rows in range(len(a))]
# Pasos
    pasos.append("Matriz A")
    pasos.append("\n".join(str(x) for x in a))
    pasos.append("\n")
    pasos.append("Matriz B")
    pasos.append("\n".join(str(x) for x in b))
    pasos.append("\n")

    for times in range(len(a)):
        # Valor en cada columna segun fila
# Pasos
        pasos.append(f"Multiplicamos la fila {a[times]}")
        for x in range(len(a[0])):
            val_a = a[times][x]
# Pasos 
            pasos.append(f"por la columna {x} de B")
        # Valor en cada fila de b segun columna
            for y in range(len(b[0])):
                val_b = b[x][y]
                res[times][y] += val_a * val_b
# Pasos
                pasos.append(f"C[{times}][{y}] += {val_a} * {val_b}")

# Pasos
        pasos.append("\n")
    pasos.append("Matriz Resultante")
    pasos.append("\n".join(str(x) for x in res))
    pasos.append("\n")
    return res

def gauss_jordan(eqs:list[list]):
    matriz = [eqs[x].copy() for x in range(len(eqs))]

# Pasos
    pasos.append("Matriz a realizar Gauss-Jordan")
    pasos.append("\n".join(str(x) for x in matriz))

    for eq in range(0, len(matriz)):
        pivot = matriz[eq]
# Pasos
        pasos.append(f"\nFila {eq+1} es el pivote")
        pasos.append(f"\n{pivot}")
        pasos.append("\n")
        for x in range(eq+1, len(matriz)):
            multiplicador1 = pivot[eq] * (1 if pivot[eq] > 0 else -1)

            multiplicador2 = (matriz[x][eq] * (1 if matriz[x][eq] > 0 else -1)) * (1 if matriz[x][eq] * pivot[eq] < 0 else -1)

# Pasos
            pasos.append(f"\n{multiplicador1}*f{x+1} + ({multiplicador2})*f{eq+1}")
            for y in range(len(matriz[x])):
                matriz[x][y] *= multiplicador1
                sumando = pivot[y] * multiplicador2
                matriz[x][y] += sumando
# Pasos         
            pasos.append("\n".join(str(x) for x in matriz))
            pasos.append("\n")
    for eq in range(len(matriz)-1, -1, -1):
        pivot = matriz[eq]
# Pasos
        pasos.append(f"\nFila {eq+1} es el pivote")
        pasos.append(f"\n{pivot}")
        pasos.append("\n")
        variable = eq
        constant = -1
        if pivot[eq] != 1 and pivot[eq] != 0:
# Pasos
            pasos.append(f"\n{1/pivot[eq]}*f{eq+1}")
            val =  pivot[eq]
            for x in range(len(pivot)):
                pivot[x] /= val
# Pasos
            pasos.append("\n".join(str(x) for x in matriz))
        for x in range(eq-1, -1, -1):
            multiplicador1 = pivot[eq] * (1 if pivot[eq] > 0 else -1)

            multiplicador2 = (matriz[x][eq] * (1 if matriz[x][eq] > 0 else -1)) * (1 if matriz[x][eq] * pivot[eq] < 0 else -1)
# Pasos
            pasos.append(f"\n{multiplicador1}*f{x+1} + ({multiplicador2})*f{eq+1}")
            for y in range(len(matriz[x])):
                matriz[x][y] *= multiplicador1
                sumando =  pivot[y] * multiplicador2
                matriz[x][y] += sumando
# Pasos
            pasos.append("\n".join(str(x) for x in matriz))
            pasos.append("\n")
            
    #return matriz


    return matriz

def gauss(matriz:list[list]):

    matriz = [matriz[x].copy() for x in range(len(matriz))]
# Pasos
    pasos.append("Matriz a realizar Gauss")
    pasos.append("\n".join(str(x) for x in matriz))
    for row in range(0, len(matriz)):
        pivot = matriz[row]
# Pasos
        pasos.append(f"\nFila {row+1} es el pivote")
        pasos.append(f"\n{pivot}")
        pasos.append("\n")
        for x in range(row+1, len(matriz)):
            multiplier = ((matriz[x][row] * (1 if matriz[x][row] > 0 else -1))/(pivot[row] * (1 if pivot[row] > 0 else -1))) * (1 if matriz[x][row]/pivot[row] < 0 else -1)
# Pasos
            pasos.append(f"\n{multiplier}*f{x+1} + f{row+1}")
            for y in range(len(matriz[x])):
                matriz[x][y] += multiplier * pivot[y]
# Pasos
        pasos.append("\n".join(str(x) for x in matriz))
        pasos.append("\n")
    return matriz
#region
def gauss_eq(eqs:list[list]):
    matriz = [eqs[x].copy() for x in range(len(eqs))]
    
    pasos = []
    pasos.append("Matriz original")
    pasos.append("\n".join(str(x) for x in matriz))

    for eq in range(0, len(matriz)):
        pivot = matriz[eq]
        for x in range(eq+1, len(matriz)):
            multiplicador1 = pivot[eq] * (1 if pivot[eq] > 0 else -1)

            multiplicador2 = (matriz[x][eq] * (1 if matriz[x][eq] > 0 else -1)) * (1 if matriz[x][eq] * pivot[eq] < 0 else -1)

            pasos.append(f"\n{multiplicador1}*f{x+1} + ({multiplicador2})*f{eq+1}")

            for y in range(len(matriz[x])):
                matriz[x][y] *= multiplicador1
                sumando = pivot[y] * multiplicador2
                matriz[x][y] += sumando

            pasos.append("\n".join(str(x) for x in matriz))
   
    for f in matriz:
        ecuaciones = ""
        ecuaciones += "+".join(f" {f[x]}a{x+1} " for x in range(len(f)-1))
        ecuaciones += f"= {f[-1]}"
        pasos.append(ecuaciones)
    resultados = []
    for f in range(len(matriz)-1,-1, -1):
        pasos.append(f"a{f+1}: ")
        constante = matriz[f][-1]
        operacion = f"\t{constante}"
        for r in range(len(resultados)):
            operacion += f" + ({matriz[f][-(r+2)]} * {resultados[r]})"
            constante -= matriz[f][-(r+2)]*resultados[r]
        pasos.append(operacion)
        pasos.append(f"\t{constante}/{matriz[f][f]}")
        pasos.append(f"\t{constante/matriz[f][f]}")
        resultados.append(constante/matriz[f][f])
    resultados.reverse()
    pasos.append("\n".join(f"a{x+1} = {resultados[x]}" for x in range(len(resultados))))

    return matriz
#endregion    
def resultado(matriz:list[list]):
    resultados = []
    for f in range(len(matriz)-1,-1, -1):
        
        constante = matriz[f][-1]
        for r in range(len(resultados)):
            constante -= matriz[f][-(r+2)]*resultados[r]
        resultados.append(constante/matriz[f][f])
    resultados.reverse()
    return resultados

def transpuesta(matriz:list[list]):
# Pasos
    pasos.append("Matriz original")
    pasos.append("\n".join(str(x) for x in matriz))
    pasos.append("\n")

    transpuesta = [[0 for rows in range(len(matriz))].copy() for cols in range(len(matriz[0]))]
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            transpuesta[y][x] = matriz[x][y]
# Pasos
    pasos.append("Matriz transpuesta")
    pasos.append("\n".join(str(x) for x in transpuesta))
    pasos.append("\n")
    return transpuesta
            
def orden(matriz:list[list]):
# Pasos
    pasos.append("Matriz")
    pasos.append("\n".join(str(x) for x in matriz))
    pasos.append("\n")
    pasos.append(f"Orden: {len(matriz)}x{len(matriz[0])}")
    return len(matriz), len(matriz[0])

def markov(tabla:list[list], probabilidades:list[list], periodos:int, transponer:bool=True):
# Pasos
    if transponer:
        pasos.append("Matriz de Probabilidades")
        pasos.append("\n".join(str(x) for x in tabla))
        pasos.append("\n")
    transicion = transpuesta(tabla) if transponer else tabla
    pasos.append("Matriz de transicion")
    pasos.append("\n".join(str(x) for x in transicion))
    pasos.append("\n")
    pasos.append("Probabilidades iniciales")
    pasos.append("\n".join(str(x) for x in probabilidades))
    pasos.append("\n")
    for p in range(periodos):
        probabilidades = multiplicacion(transicion, probabilidades)
        pasos.append(f"Periodo {p+1}")
        pasos.append("\n".join(str(x) for x in probabilidades))
        pasos.append("\n")
    return probabilidades

def suma(a:list[list], b:list[list]):
    if orden(a) != orden(b):
        return
    matriz_suma = [[0 for rows in range(len(a[0]))].copy() for cols in range(len(a))]
# Pasos
    pasos.append("Matriz A")
    pasos.append("\n".join(str(x) for x in a))
    pasos.append("\n")
    pasos.append("Matriz B")
    pasos.append("\n".join(str(x) for x in b))
    pasos.append("\n")

    n=-1
    for i in range(0,len(a),1):
        n =  n + 1
        f=a[i]
        r=b[i]
        t=matriz_suma[i]
        for y in range(0,len(f),1):
# Pasos
            pasos.append(f"C[{i}][{y}] = {f[y]} + {r[y]}")
            t[y] = f[y] + r[y]
# Pasos
    pasos.append("Matriz Resultante")
    pasos.append("\n".join(str(x) for x in matriz_suma))
    pasos.append("\n")
    return matriz_suma

def resta(a:list[list], b:list[list]):
    if orden(a) != orden(b):
        return
    matriz_resta = [[0 for rows in range(len(a[0]))].copy() for cols in range(len(a))]
# Pasos
    pasos.append("Matriz A")
    pasos.append("\n".join(str(x) for x in a))
    pasos.append("\n")
    pasos.append("Matriz B")
    pasos.append("\n".join(str(x) for x in b))
    pasos.append("\n")

    n=-1
    for i in range(0,len(a),1):
        n+=1
        f=a[n]
        r=b[n]
        t=matriz_resta[n]
        for y in range(0,len(f),1):
# Pasos
            pasos.append(f"C[{n}][{y}] = {f[y]} - {r[y]}")
            t[y] = f[y] - r[y]
# Pasos
    pasos.append("Matriz Resultante")
    pasos.append("\n".join(str(x) for x in matriz_resta))
    pasos.append("\n")
    return matriz_resta

def producto_punto(a:list[list],b:list[list]):
    if orden(b) != orden(a):
        return
    producto = 0
# Pasos
    pasos.append("Vector A")
    pasos.append("\n".join(str(x) for x in a))
    pasos.append("\n")
    pasos.append("Vector B")
    pasos.append("\n".join(str(x) for x in b))
    pasos.append("\n")
    txt = "Resultado: "
    
    for i in range(0,len(a)):
        for y in range(0,len(a[i]),1):
# Pasos
            txt += f"{a[i][y]} * {b[i][y]} +"
            producto += (a[i][y] * b[i][y])
    pasos.append(txt[:-1])
    pasos.append("\n")
    pasos.append(f"Resultado: {producto}")
    pasos.append("\n")
    return producto

def magnitud(x, y):
# Pasos
    pasos.append("Vector")
    pasos.append(f"({x}, {y})")
    pasos.append("\n")
    pasos.append("Magnitud")
    pasos.append(f"sqrt({x}^2 + {y}^2)")
    pasos.append("\n")
    mag = ((y**2)+(x**2))**0.5
# Pasos
    pasos.append(f"Magnitud: {mag}")
    return mag

def angulo(x, y):
    if x == 0:
        r = 'Error'
        return r
    else :
        if x < 0 and y < 0:
            x = x * (-1)
            y = y * (-1)
        elif x < 0:
            x = x * (-1)
        elif y < 0:
            y = y * (-1) 
# Pasos
        pasos.append("Vector")
        pasos.append(f"({x}, {y})")
        pasos.append("\n")
        pasos.append("Angulo")
        pasos.append(f"tan^-1({y}/{x})")
        angulo = math.atan((y/x))
        angulo = angulo * 180/math.pi
# Pasos
        pasos.append(f"Angulo: {angulo}")

        return angulo

def componentes(magnitud, angulo):
# Pasos
    pasos.append("Vector")
    pasos.append(f"Magnitud: {magnitud}")
    pasos.append(f"Angulo: {angulo}")
    pasos.append("\n")
    componentex = magnitud * math.cos(angulo * math.pi/180)
    componentey = magnitud * math.sin(angulo * math.pi/180)
# Pasos
    pasos.append("Componentes")
    pasos.append(f"Componente en x: {componentex}")
    pasos.append(f"Componente en y: {componentey}")
    pasos.append("\n")
    componentes = [componentex, componentey]

    return componentes