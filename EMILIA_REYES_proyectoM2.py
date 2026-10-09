# ============================================================
# FUNDAMENTOS DE PYTHON
# Producto terminado - Modulo 2
# Retos integrados: Longitud de palabras y Cuadrantes
# Semanas 5, 6 y 7
# ============================================================

# COLECCIONES DEL PROGRAMA

# Lista para guardar todas las palabras ingresadas.
historial_palabras = []

# Diccionario para identificar los cuatro cuadrantes.
cuadrantes = {
    1: "Cuadrante I",
    2: "Cuadrante II",
    3: "Cuadrante III",
    4: "Cuadrante IV"
}


# ============================================================
# RETO 1: LONGITUD DE PALABRAS
# ============================================================

def reto_longitud():
    """Solicita una palabra y valida que tenga de 4 a 8 letras."""

    print("\n--- RETO 1: LONGITUD DE PALABRAS ---")

    while True:
        palabra = input(
            "Ingresa una palabra de entre 4 y 8 letras: "
        ).strip()

        # Guardamos cada intento en la lista.
        if palabra:
            historial_palabras.append(palabra)

        # Validamos que el usuario haya escrito algo.
        if not palabra:
            print("Error: no puedes dejar el campo vacio.")
            continue

        # Verificamos que solo contenga letras.
        if not palabra.isalpha():
            print("Error: ingresa solamente letras.")
            continue

        longitud = len(palabra)

        # Aplicamos la logica condicional del reto.
        if 4 <= longitud <= 8:
            print(f"Palabra correcta: {palabra}")
            print(f"Longitud: {longitud} letras.")
            print("La palabra cumple con el rango solicitado.")
            break
        else:
            print(
                f"Error: la palabra tiene {longitud} letras."
            )
            print("Intenta nuevamente con otra palabra.")


# ============================================================
# RETO 2: CALCULO DE CUADRANTES
# ============================================================

def obtener_coordenada(nombre):
    """Solicita una coordenada numerica diferente de cero."""

    while True:
        try:
            coordenada = float(
                input(f"Ingresa la coordenada {nombre}: ")
            )

            # El cero no pertenece a ninguno de los cuadrantes.
            if coordenada == 0:
                print(
                    "Error: la coordenada no puede ser cero."
                )
                continue

            return coordenada

        except ValueError:
            print(
                "Error: debes ingresar un numero valido."
            )


def reto_cuadrantes():
    """Determina el cuadrante a partir de las coordenadas X y Y."""

    print("\n--- RETO 2: CALCULO DE CUADRANTES ---")

    # Solicitamos coordenadas validas mediante un ciclo.
    x = obtener_coordenada("X")
    y = obtener_coordenada("Y")

    # Identificamos el cuadrante segun los signos.
    if x > 0 and y > 0:
        numero_cuadrante = 1
    elif x < 0 and y > 0:
        numero_cuadrante = 2
    elif x < 0 and y < 0:
        numero_cuadrante = 3
    else:
        numero_cuadrante = 4

    # Consultamos el nombre en el diccionario.
    nombre_cuadrante = cuadrantes[numero_cuadrante]

    print(f"\nCoordenada X: {x}")
    print(f"Coordenada Y: {y}")
    print(f"Resultado: {nombre_cuadrante}")


# ============================================================
# FUNCION ADICIONAL: MOSTRAR HISTORIAL DE PALABRAS
# ============================================================

def mostrar_historial():
    """Muestra las palabras almacenadas en la lista."""

    print("\n--- HISTORIAL DE PALABRAS ---")

    if not historial_palabras:
        print("Todavia no has ingresado ninguna palabra.")
    else:
        for indice, palabra in enumerate(
            historial_palabras, start=1
        ):
            print(f"{indice}. {palabra}")

        print(
            f"Total de palabras registradas: "
            f"{len(historial_palabras)}"
        )


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal():
    """Permite ejecutar los retos desde un menu."""

    while True:
        print("\n" + "=" * 42)
        print("       PRODUCTO TERMINADO")
        print("       FUNDAMENTOS DE PYTHON")
        print("=" * 42)
        print("1. Reto de longitud de palabras")
        print("2. Reto de calculo de cuadrantes")
        print("3. Mostrar historial de palabras")
        print("4. Salir del programa")
        print("=" * 42)

        opcion = input("Selecciona una opcion (1-4): ").strip()

        if opcion == "1":
            reto_longitud()
        elif opcion == "2":
            reto_cuadrantes()
        elif opcion == "3":
            mostrar_historial()
        elif opcion == "4":
            print("\nGracias por utilizar el programa.")
            print("Programa finalizado correctamente.")
            break
        else:
            print(
                "Opcion no valida. Selecciona un numero del 1 al 4."
            )


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    menu_principal()