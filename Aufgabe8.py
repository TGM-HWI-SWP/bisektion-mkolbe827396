def p4(x):
    """
    Polynom aus der Aufgabenstellung:
    P4(x) = 2x + x^2 + 3x^3 - x^4
    """
    return 2*x + x**2 + 3*x**3 - x**4


def bisektion_poly(a, b, tol):
    """
    Bisektionsverfahren für das Polynom
    """

    iteration = 0

    while True:
        m = (a + b) / 2
        iteration += 1

        # Abbruchbedingung
        if abs(p4(m)) < tol:
            return m, iteration

        # Intervall anpassen
        if p4(a) * p4(m) < 0:
            b = m
        else:
            a = m


def main():
    # Vorgegebenes Intervall (mit Vorzeichenwechsel)
    a = 3
    b = 4

    print("Intervall: [3, 4]")
    print("P4(3) =", p4(3))
    print("P4(4) =", p4(4))

    if p4(a) * p4(b) < 0:
        print("\nZwischenwertsatz anwendbar!")

        # Test 1
        print("\n=== Test mit ε = 10^-2 ===")
        x1, it1 = bisektion_poly(a, b, 0.01)
        print("Nullstelle:", x1)
        print("Iterationen:", it1)

        # Test 2
        print("\n=== Test mit ε = 10^-8 ===")
        x2, it2 = bisektion_poly(a, b, 10**-8)
        print("Nullstelle:", x2)
        print("Iterationen:", it2)

    else:
        print("Kein Vorzeichenwechsel!")


if __name__ == "__main__":
    main()