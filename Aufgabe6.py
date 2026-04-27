def solver2() -> None:
    """
    Führt das Regula-Falsi-Verfahren zur Nullstellensuche aus.

    Der Benutzer gibt die Werte n, a, b und die Toleranz ein.
    Anschließend wird überprüft, ob ein Vorzeichenwechsel im Intervall vorliegt.
    Falls ja, wird die Nullstelle iterativ berechnet.
    """

    # Eingaben mit Fehlerbehandlung
    while True:
        try:
            n = float(input("Wähle eine Zahl n (z.B. 25): "))
            a = float(input("Wähle die untere Intervallgrenze a: "))
            b = float(input("Wähle die obere Intervallgrenze b: "))
            tol = float(input("Wähle die Toleranz (z.B. 0.000001): "))

            # Überprüfung der Eingaben
            if tol <= 0:
                print("Die Toleranz muss größer als 0 sein.")
            elif a >= b:
                print("Es muss gelten: a < b")
            else:
                break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")

    def f(x: float, n: float) -> float:
        """
        Berechnet den Funktionswert f(x) = x^2 - n.

        :param x: Variable x
        :param n: Konstante n
        :return: Funktionswert
        """
        return x**2 - n

    def regula_falsi(
        f, a: float, b: float, tol: float, n: float
    ) -> tuple[float, int]:
        """
        Bestimmt eine Nullstelle mit dem Regula-Falsi-Verfahren.

        :param f: Funktion f(x, n)
        :param a: untere Intervallgrenze
        :param b: obere Intervallgrenze
        :param tol: Toleranz
        :param n: Parameter der Funktion
        :return: (Näherung der Nullstelle, Anzahl der Iterationen)
        """

        c = a  # Startwert
        iteration = 0

        # Iteration solange Funktionswert noch nicht klein genug
        while abs(f(c, n)) > tol:
            iteration += 1

            # Berechnung des neuen Punktes (Regula falsi Formel)
            c = b - (f(b, n) * (b - a)) / (f(b, n) - f(a, n))

            # Falls exakte Nullstelle gefunden
            if f(c, n) == 0:
                return c, iteration

            # Intervall halbieren (ähnlich wie bei Bisektion)
            elif f(a, n) * f(c, n) < 0:
                b = c
            else:
                a = c

        return c, iteration

    # Prüfung auf Vorzeichenwechsel (Zwischenwertsatz)
    if f(a, n) * f(b, n) < 0:
        print("Zwischenwertsatz anwendbar: Es existiert mindestens eine Nullstelle im Intervall.")

        # Aufruf des Verfahrens
        nullstelle, iterationen = regula_falsi(f, a, b, tol, n)

        print("\nNäherung der Nullstelle:", nullstelle)

        # Vergleich mit analytischer Lösung (nur für n >= 0 sinnvoll)
        if n >= 0:
            print("Analytische Lösung:", n**0.5)
            print("Abweichung:", abs(nullstelle - n**0.5))

        print("Anzahl der Iterationen:", iterationen)

    else:
        print("Achtung: Kein Vorzeichenwechsel → Zwischenwertsatz NICHT garantiert!")


# Startpunkt des Programms
if __name__ == "__main__":
    solver2()