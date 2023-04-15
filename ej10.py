# Devuelve un diccionario donde la clave es el nombre del alumno y el valor es una lista con sus notas
def generarEstructura(nombres, notas1, notas2):

    # Devuelve una lista de nombres
    def generarListaDeNombres(nombres):
        # Devuelve un string cambiando los caracteres indicados por espacios           
        def reemplazarCaracteresPorEspacios(texto, caracteres):
            for caracter in caracteres:
                texto = texto.replace(caracter, ' ')
            return texto
        
        # Devuelve una lista de nombres a partir de otra, cada nombre es pasado a minuscula y capitaliza la  primera palabra
        def estilizarNombres(lista):
            return list(map(lambda nombre: nombre.lower().capitalize(), lista))

        return estilizarNombres(reemplazarCaracteresPorEspacios(nombres, "',").split())
    
    datos = zip(generarListaDeNombres(nombres), notas1, notas2)
    return {dato[0]: [dato[1], dato[2]] for dato in datos}
 



# Devuelve un diccionario con clave "nombre del alumno" y valor "promedio"
def calcularPromedioEstudiantes(alumnos):
    promedios = {}

    for alumno in alumnos:
        total = 0
        for nota in alumnos[alumno]:
            total += nota
        promedios[alumno] = total / len(alumnos[alumno])

    return promedios




# Devuelve el promedio general del curso
def calcularPromedioGeneralCurso(alumnos):
    promedios = calcularPromedioEstudiantes(alumnos)
    return sum(promedios.values()) / len(promedios)




# Devuelve un diccionario con el alumno con la nota promedio mas alta
def devolverEstudiantePromedioMasAlto(alumnos):
    maxProm = -1
    estudiante = {}

    alumnos = calcularPromedioEstudiantes(alumnos)
    for alumno in alumnos:
        if(alumnos[alumno] > maxProm):
            maxProm = alumnos[alumno]
            estudiante = {alumno: alumnos[alumno]}

    return estudiante




# Devuelve un diccionario con el alumno con la nota mas baja
def devolverEstudianteNotaMasBaja(alumnos):
    minNota = 1000
    estudiante = {}

    for alumno in alumnos:
        for nota in alumnos[alumno]:
            if(nota < minNota):
                minNota = nota
                estudiante = {alumno: minNota}

    return estudiante


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

# Punto A
estructura = generarEstructura(nombres, notas_1, notas_2)
print(estructura, '\n')

# Punto B
dictPromedios = calcularPromedioEstudiantes(estructura)
for nombre in dictPromedios:
    print(f'El promedio del alumno {nombre} es: {dictPromedios[nombre]}')

# Punto C
print(f'\nEl promedio general del curso es {calcularPromedioGeneralCurso(estructura)}')

# Punto D
print(f'\nEl alumno con el promedio mas alto es {devolverEstudiantePromedioMasAlto(estructura)}')

# Punto E
print(f'\nEl alumno con la nota mas baja es {devolverEstudianteNotaMasBaja(estructura)}')