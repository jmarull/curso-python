
def calcular(a: float, b: float, operacion: str) -> float:
    """
    Devuelve el resultado de la operación indicada.

    Parámetros:
        a (float)
        b (float)
        operacion (str)

    Devuelve:
        float
    """
    match operacion:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "**":
            return a ** b
        case "%":
            return a % b
        case "/":
            if b == 0:
                raise ValueError("No se puede dividir entre cero")
            return a / b
        case _:
            raise ValueError("Operación no válida")     


def main():
    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        op = input("Operación: ")

        print(calcular(a, b, op))

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()