
"""
Zadanie 2 - Nawiasy

Opis zadania:
- Zweryfikuj, czy podany ciąg znaków zawiera poprawne nawiasy.
- Każdemu otwartemu nawiasowi '(' powinien odpowiadać nawias zamykający ')'.
- Jeśli nawiasy się zgadzają, funkcja ma zwrócić True, w przeciwnym wypadku False.
- Rozpatrujemy wyłącznie nawiasy okrągłe.

Przykładowe wejścia (True):
    "( if ( zero ? x ) max (/ 1 x ))"
    "I told ( that its not ( yet ) done ). (42)"
Przykładowe wejścia (False):
    ":-)"
    "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))"
    "())(("

Wymagania:
- Implementacja funkcji `check_parentheses(s: str) -> bool`.
- Użycie stosu do weryfikacji poprawności nawiasów.
"""

def check_parentheses(s: str) -> bool:
    """
    Sprawdza, czy w ciągu znaków 's' nawiasy okrągłe są poprawnie sparowane.

    Args:
        s (str): Ciąg znaków do analizy.

    Returns:
        bool: True jeśli nawiasy są poprawne, False w przeciwnym wypadku.
    """
    stack = []  # Stos do przechowywania otwartych nawiasów

    # Przechodzimy przez wszystkie znaki w ciągu
    for char in s:
        if char == '(':
            stack.append(char)  # Dodajemy nawias otwierający na stos
        elif char == ')':
            if not stack:  # Jeśli stos jest pusty, to nie ma nawiasu do zamknięcia
                return False
            stack.pop()  # Usuwamy nawias otwierający z stosu

    # Jeśli stos jest pusty, oznacza to, że wszystkie nawiasy zostały poprawnie sparowane
    return len(stack) == 0


# Przykładowe wywołanie:
if __name__ == "__main__":
    n = int(input("Podaj liczbę przykładów do sprawdzenia: "))

    for i in range(n):
        example = input(f"Wprowadź przykład {i+1}: ")
        result = check_parentheses(example)
        print(f"{example} -> {result}")