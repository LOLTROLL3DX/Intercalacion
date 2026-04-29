import time
import os

def counting_sort_por_digito(arr, exp):
    """
    Ordenamiento por conteo auxiliar que ordena según el dígito
    representado por 'exp' (1 → unidades, 10 → decenas, etc.)
    """
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10  # dígitos del 0 al 9

    # Contar ocurrencias del dígito actual
    for i in range(n):
        digito = (arr[i] // exp) % 10
        conteo[digito] += 1

    # Acumular posiciones
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir array de salida (de derecha a izquierda para estabilidad)
    for i in range(n - 1, -1, -1):
        digito = (arr[i] // exp) % 10
        salida[conteo[digito] - 1] = arr[i]
        conteo[digito] -= 1

    # Copiar resultado al array original
    for i in range(n):
        arr[i] = salida[i]


def radix_sort(arr):
    """
    Radix Sort LSD (Least Significant Digit).
    Ordena de menor a mayor procesando dígito por dígito.
    """
    maximo = max(arr)

    # Iterar por cada posición de dígito mientras exista
    exp = 1
    while maximo // exp > 0:
        counting_sort_por_digito(arr, exp)
        exp *= 10

    return arr


def leer_datos(ruta):
    """Lee el archivo .txt y retorna una lista de enteros."""
    with open(ruta, "r") as f:
        return [int(linea.strip()) for linea in f if linea.strip()]


def main():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos.txt")

    print("Leyendo datos...")
    datos = leer_datos(ruta)
    print(f"Total de números cargados: {len(datos)}")

    # Medir tiempo en milisegundos
    inicio = time.perf_counter()
    datos_ordenados = radix_sort(datos)
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000
    print(f"Ordenamiento completado en: {tiempo_ms:.2f} ms")
    print(f"Primeros 10 valores: {datos_ordenados[:10]}")
    print(f"Últimos  10 valores: {datos_ordenados[-10:]}")


if __name__ == "__main__":
    main()