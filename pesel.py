"""
Zadanie 1 - Weryfikacja numeru PESEL

Opis zadania:
- Użytkownik wprowadza numer PESEL (ciąg 11 znaków, zakładamy, że długość jest poprawna).
- Program sprawdza, czy ostatnia cyfra (cyfra kontrolna) jest prawidłowa.
- Reguła: znaleźć w internecie.
- Jeśli ostatnia cyfra zgadza się z obliczoną wartością, funkcja ma zwrócić 1, w przeciwnym wypadku 0.

Przykładowe wejście:
    "97082123152"
Przykładowe wyjście:
    0

Wymagania:
- Implementacja funkcji `verify_pesel(pesel: str) -> int`.
- Użycie algorytmu weryfikacji opisanej powyżej.
"""

def verify_pesel(pesel: str) -> int:
    """
    Weryfikuje numer PESEL.

    Args:
        pesel (str): Numer PESEL w postaci ciągu 11 znaków.

    Returns:
        int: 1 jeśli numer jest poprawny, 0 jeśli nie.
    """
    # Wagi dla cyfr w numerze PESEL
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    # Sprawdzamy, czy długość numeru PESEL to 11 znaków (co już zakładamy w zadaniu)
    if len(pesel) != 11:
        return 0  # Jeśli długość jest nieprawidłowa, zwróć 0

    # Obliczamy sumę kontrolną (pierwsze 10 cyfr z wagami)
    total = 0
    for i in range(10):
        total += int(pesel[i]) * weights[i]

    # Cyfra kontrolna powinna być równa reszcie z dzielenia sumy przez 10
    control_digit = total % 10

    # Porównujemy cyfrę kontrolną z ostatnią cyfrą PESEL
    if control_digit == int(pesel[-1]):
        return 1  # Numer PESEL jest poprawny
    else:
        return 0  # Numer PESEL jest niepoprawny


# Program główny
if __name__ == "__main__":
    pesel_input = input("Wprowadź numer PESEL (11 cyfr): ").strip()  # Pobranie numeru PESEL od użytkownika
    result = verify_pesel(pesel_input)
    print(f"Wynik weryfikacji PESEL: {result}")