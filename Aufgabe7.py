import matplotlib.pyplot as plt
import numpy as np


def plotter():
    """
    Hauptfunktion für Aufgabe 7.
    Führt die grafische Darstellung des Bisektionsverfahrens aus.
    """

    def f(x, n):
        """
        Mathematische Funktion:
        f(x) = x^2 - n

        :param x: Eingabewert (kann Zahl oder Array sein)
        :param n: Konstante
        :return: Funktionswert
        """
        return x**2 - n

    def bisektion_plot(a: float, b: float, tol: float, n: float):
        """
        Führt das Bisektionsverfahren durch und speichert alle Zwischenwerte.

        :param a: untere Intervallgrenze
        :param b: obere Intervallgrenze
        :param tol: gewünschte Genauigkeit
        :param n: Parameter der Funktion
        :return: (Nullstelle, Liste der Näherungen, Liste der Fehler)
        """

        m_werte = []   # Liste für alle Näherungswerte m
        fehler = []    # Liste für die Fehler |f(m)|

        while True:
            # Mittelpunkt des Intervalls berechnen
            m = (a + b) / 2

            # Werte speichern (für Diagramme)
            m_werte.append(m)
            fehler.append(abs(f(m, n)))

            # Abbruchbedingung: Funktionswert ist klein genug
            if abs(f(m, n)) < tol:
                break

            # Entscheidung: In welcher Intervallhälfte liegt die Nullstelle?
            if f(a, n) * f(m, n) < 0:
                b = m  # Nullstelle liegt links
            else:
                a = m  # Nullstelle liegt rechts

        return m, m_werte, fehler

    def plot_aufgabe7(a: float, b: float, n: float, m_werte: list, fehler: list):
        """
        Erstellt die drei geforderten Diagramme:
        1. Funktion + Iterationen
        2. Fehlerverlauf
        3. Entwicklung der Lösung

        :param a: untere Intervallgrenze
        :param b: obere Intervallgrenze
        :param n: Parameter der Funktion
        :param m_werte: Liste der Näherungen
        :param fehler: Liste der Fehlerwerte
        """

        # x-Werte im Intervall erzeugen
        x = np.linspace(a, b, 100)

        # Funktionswerte berechnen
        y = f(x, n)

        # -------------------------------
        # Diagramm 1: Funktion + Iterationen
        # -------------------------------
        plt.figure(figsize=(10, 5))

        # Funktion plotten
        plt.plot(x, y, label="f(x) = x² - n")

        # x-Achse einzeichnen
        plt.axhline(0, color="black")

        # Iterationspunkte auf der Funktion anzeigen
        plt.scatter(
            m_werte,
            f(np.array(m_werte), n),
            color="red",
            label="Iterationen"
        )

        plt.title("Funktion und Iterationen (Bisektion)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid()
        plt.show()

        # -------------------------------
        # Diagramm 2: Fehler pro Iteration
        # -------------------------------
        plt.figure()

        plt.plot(fehler, marker="o")

        plt.title("Fehler pro Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("|f(m)|")

        plt.grid()
        plt.show()

        # -------------------------------
        # Diagramm 3: Entwicklung der Lösung
        # -------------------------------
        plt.figure()

        plt.plot(m_werte, marker="o")

        plt.title("Näherung der Lösung")
        plt.xlabel("Iteration")
        plt.ylabel("m")

        plt.grid()
        plt.show()

    def main():
        """
        Hauptprogramm:
        - Eingaben lesen
        - Zwischenwertsatz prüfen
        - Bisektion ausführen
        - Ergebnisse und Diagramme anzeigen
        """

        try:
            # Benutzereingaben
            n = float(input("Wähle eine Zahl n (z.B. 25): "))
            a = float(input("Wähle die untere Intervallgrenze a: "))
            b = float(input("Wähle die obere Intervallgrenze b: "))
            tol = float(input("Wähle die Toleranz (z.B. 0.000001): "))

            # Eingabeprüfung
            if tol <= 0:
                print("Die Toleranz muss größer als 0 sein.")
                return

            if a >= b:
                print("Es muss gelten: a < b.")
                return

            # Zwischenwertsatz prüfen
            if f(a, n) * f(b, n) < 0:
                print("Zwischenwertsatz anwendbar!")

                # Bisektion durchführen
                nullstelle, m_werte, fehler = bisektion_plot(a, b, tol, n)

                print("\nNäherung der Nullstelle:", nullstelle)

                # Vergleich mit analytischer Lösung
                if n >= 0:
                    print("Analytische Lösung:", n**0.5)
                    print("Abweichung:", abs(nullstelle - n**0.5))

                print("Anzahl der Iterationen:", len(m_werte))

                # Diagramme anzeigen
                plot_aufgabe7(a, b, n, m_werte, fehler)

            else:
                print("Kein Vorzeichenwechsel → Verfahren nicht anwendbar!")

        except ValueError:
            print("Ungültige Eingabe!")

    # Programm starten
    main()


# Einstiegspunkt
if __name__ == "__main__":
    plotter()