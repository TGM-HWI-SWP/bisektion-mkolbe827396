from Aufgabe5 import solver
from Aufgabe6 import solver2
from Aufgabe7 import plotter

import math

def aufgabe9():
    """
    Aufgabe 9: Berechnung der Leitungslänge einer Kettenlinie
    """

    # Funktion aus der Herleitung
    def f(a):
        return a * math.cosh(50 / a) - a - 10

    # Bisektionsverfahren (gleich aufgebaut wie in A5)
    def bisektion(a, b, tol):
        iteration = 0

        while True:
            m = (a + b) / 2
            iteration += 1

            if abs(f(m)) < tol:
                return m, iteration

            if f(a) * f(m) < 0:
                b = m
            else:
                a = m

    # Formel für die Leitungslänge
    def berechne_laenge(a):
        return 2 * a * math.sinh(100 / (2 * a))

    # sinnvolles Intervall
    a_start = 100
    b_start = 150
    tol = 1e-6

    print("\n--- Aufgabe 9 ---")
    print("Berechnung der Leitungslänge einer Kettenlinie")

    print("f(100) =", f(100))
    print("f(150) =", f(150))

    if f(a_start) * f(b_start) < 0:
        print("Zwischenwertsatz anwendbar!")

        radius, iterationen = bisektion(a_start, b_start, tol)
        laenge = berechne_laenge(radius)

        print("\nKrümmungsradius a:", radius)
        print("Leitungslänge l:", laenge, "m")
        print("Iterationen:", iterationen)

    else:
        print("Kein Vorzeichenwechsel!")

if __name__ == "__main__":
    solver()
    solver2()
    plotter()
    aufgabe9()
