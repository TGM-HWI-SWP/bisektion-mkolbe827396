

def solver():
    # =========================
    # Eingabe der Parameter
    # =========================

    # Endlosschleife, um gültige Nutzereingaben sicherzustellen
    while True:
        try:
            # Einlesen einer Zahl n (für die später die Wurzel berechnet wird)
            n: float = float(input("Wähle eine Zahl n (z.B. 25): "))
            
            # Untere Intervallgrenze
            a: float = float(input("Wähle die untere Intervallgrenze a: "))
            
            # Obere Intervallgrenze
            b: float = float(input("Wähle die obere Intervallgrenze b: "))
            
            # Toleranz für die Abbruchbedingung der Bisektion
            tol: float = float(input("Wähle die Toleranz (z.B. 0.000001): "))
            
            # Wenn alles erfolgreich war → Schleife beenden
            break

        except ValueError:
            # Falls Eingabe keine Zahl war
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")


    # =========================
    # Definition der Funktion
    # =========================

    def f(x: float, n: float) -> float:
        """
        Berechnet den Funktionswert der Gleichung f(x) = x^2 - n.

        Diese Funktion wird verwendet, um die Nullstelle zu bestimmen,
        was der Quadratwurzel von n entspricht.

        :param x: Aktueller x-Wert
        :param n: Konstante, deren Wurzel gesucht wird
        :return: Funktionswert an der Stelle x
        """
        return x**2 - n


    # =========================
    # Bisektionsverfahren
    # =========================

    def bisektion(f, a: float, b: float, tol: float, n: float) -> float:
        """
        Führt das Bisektionsverfahren zur Nullstellensuche durch.

        Das Verfahren halbiert iterativ das Intervall [a, b],
        in dem sich eine Nullstelle befindet, bis die gewünschte
        Genauigkeit (tol) erreicht ist.

        Voraussetzung:
        f(a) und f(b) müssen unterschiedliche Vorzeichen haben.

        :param f: Funktion, deren Nullstelle gesucht wird
        :param a: Untere Intervallgrenze
        :param b: Obere Intervallgrenze
        :param tol: Toleranz für die Genauigkeit
        :param n: Parameter für die Funktion f
        :return: Näherung der Nullstelle
        """

        # Startwert: Mittelpunkt des Intervalls
        m: float = (a + b) / 2

        # Iteration, solange der Funktionswert noch nicht klein genug ist
        while abs(f(m, n)) > tol:

            # Neue Mitte berechnen
            m = (a + b) / 2

            # Falls exakte Nullstelle gefunden (sehr selten bei floats)
            if f(m, n) == 0:
                return m

            # Prüfen, in welchem Teilintervall die Nullstelle liegt
            elif f(a, n) * f(m, n) < 0:
                # Nullstelle liegt zwischen a und m → b verschieben
                b = m
            else:
                # Nullstelle liegt zwischen m und b → a verschieben
                a = m

        # Rückgabe der approximierten Nullstelle
        return m


    # =========================
    # Hauptprogramm
    # =========================

    # Überprüfung des Zwischenwertsatzes:
    # Es muss ein Vorzeichenwechsel im Intervall vorliegen
    if f(a, n) * f(b, n) < 0:
        print("Zwischenwertsatz anwendbar: Es existiert mindestens eine Nullstelle im Intervall.")

        # Aufruf des Bisektionsverfahrens
        nullstelle: float = bisektion(f, a, b, tol, n)

        # Ausgabe der berechneten Näherung
        print("\nNäherung der Nullstelle:", nullstelle)

        # Vergleich mit analytischer Lösung (Quadratwurzel)
        print("Analytische Lösung:", n**0.5)

    else:
        # Kein Vorzeichenwechsel → keine Garantie für Nullstelle
        print("Achtung: Kein Vorzeichenwechsel → Zwischenwertsatz NICHT garantiert!")

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    solver()