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
        self.coded = multiplicacion(self.key, txt)
        return self.coded
    
    def decipher(self, message = None):
        if not self.key:
            return
        if not self.adjkey:
            self.adjkey = inversa_gj(self.key)

        return multiplicacion(self.adjkey,message if message else self.coded)
    
    def getCoded(self):
        return self.coded

def determinante_gauss(matriz:list[list]):
    matriz = gauss(matriz)
    determinante = 1
    for x in range(len(matriz)):
        determinante *= matriz[x][x] 
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
    return cols == rows

def inversa_gj(matriz:list[list]):
    if determinante_gauss(matriz) == 0:
        return 0
    if not cuadrada(matriz):
        return -1
    matriz = [matriz[x].copy() for x in range(len(matriz))]

    for r in range(len(matriz)):
        row =  matriz[r]
        for n in range(len(row)):
            row.append(1 if r == n else 0)

    extendida = gauss_jordan(matriz)
    inversa = []
    for row in extendida:
        inversa.append(row[int(len(row)/2):])

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
    for times in range(len(a)):
        # Valor en cada columna segun fila
        for x in range(len(a[0])):
            val_a = a[times][x]
        # Valor en cada fila de b segun columna
            for y in range(len(b[0])):
                val_b = b[x][y]
                res[times][y] += val_a * val_b
    return res

def gauss_jordan(eqs:list[list]):
    matriz = [eqs[x].copy() for x in range(len(eqs))]

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
            
    #return matriz


    return matriz

def gauss(matriz:list[list]):
    matriz = [matriz[x].copy() for x in range(len(matriz))]
    for row in range(0, len(matriz)):
        pivot = matriz[row]
        for x in range(row+1, len(matriz)):
            multiplier = ((matriz[x][row] * (1 if matriz[x][row] > 0 else -1))/(pivot[row] * (1 if pivot[row] > 0 else -1))) * (1 if matriz[x][row]/pivot[row] < 0 else -1)
            for y in range(len(matriz[x])):
                matriz[x][y] += multiplier * pivot[y]
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
    transpuesta = [[0 for rows in range(len(matriz))].copy() for cols in range(len(matriz[0]))]
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            transpuesta[y][x] = matriz[x][y]
    return transpuesta
            
def orden(matriz:list[list]):
    return len(matriz), len(matriz[0])

def markov(tabla:list[list], probabilidades:list[list], periodos:int, transponer:bool=True):
    transicion = transpuesta(tabla) if transponer else tabla
    for p in range(periodos):
        probabilidades = multiplicacion(transicion, probabilidades)
    return probabilidades

def suma(a:list[list], b:list[list]):
    if orden(a) != orden(b):
        return
    matriz_suma = [[0 for rows in range(len(a[0]))].copy() for cols in range(len(a))]
    n=-1
    for i in range(0,len(a),1):
        n =  n + 1
        f=a[i]
        r=b[i]
        t=matriz_suma[i]
        for y in range(0,len(f),1):
            t[y] = f[y] + r[y]
    return matriz_suma

def resta(a:list[list], b:list[list]):
    if orden(a) != orden(b):
        return
    matriz_resta = [[0 for rows in range(len(a[0]))].copy() for cols in range(len(a))]
    n=-1
    for i in range(0,len(a),1):
        n+=1
        f=a[n]
        r=b[n]
        t=matriz_resta[n]
        for y in range(0,len(f),1):
            t[y] = f[y] - r[y]
    return matriz_resta

def producto_punto(a:list[list],b:list[list]):
    if orden(b) != orden(a):
        return
    producto = 0
    for i in range(0,len(a)):

        for y in range(0,len(a[i]),1):
            producto += (a[i][y] * b[i][y])
    return producto

def magnitud(x, y):
    mag = ((y**2)+(x**2))**0.5
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

        angulo = math.atan((y/x))
        angulo = angulo * 180/math.pi
        return angulo

def componentes(magnitud, angulo):
    componentex = magnitud * math.cos(angulo * math.pi/180)
    componentey = magnitud * math.sin(angulo * math.pi/180)

    componentes = [componentex, componentey]

    return componentes