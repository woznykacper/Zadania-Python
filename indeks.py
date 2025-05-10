<<<<<<< HEAD
import string

def clean_text(text: str) -> list[str]:
    """
    Funkcja oczyszcza tekst z interpunkcji i zamienia wszystkie litery na małe.
    """
    # Usuwamy interpunkcję i zamieniamy na małe litery
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Zwracamy listę wyrazów
    return text.split()
"""
Zadanie 3 - Indeksowanie dokumentów

Opis zadania:
- Wejście:
    * Pierwsza linia: liczba dokumentów do przetworzenia (n).
    * Kolejne n linii: dokumenty (każdy dokument to wielowyrazowy ciąg znaków).
    * Następna linia: liczba zapytań (m).
    * Kolejne m linii: zapytania (każdy zapytanie to pojedynczy wyraz).
- Wyjście:
    * m linii, z których każda zawiera listę numerów dokumentów, w których wystąpił wyraz z zapytania.
    * Każda lista jest posortowana według częstości wystąpienia zapytania w danym dokumencie (od największej do najmniejszej).
    * W przypadku równych częstości, lista może być posortowana malejąco wg numeru dokumentu (opcjonalnie).
    * Jeśli słowo nie wystąpiło w żadnym dokumencie, zwróć pustą listę.

Przykładowe wejście:
    3
    Your care set up, do not pluck my care down.
    Your care set up, do not pluck my care down.
    Your care is gain of care when new care is won.
    2
    care
    is

Przykładowe wyjście:
    [1, 2, 0]
    [2, 1]

Wymagania:
- Implementacja funkcji `index_documents(documents: list[str], queries: list[str]) -> list[list[int]]`.
- Przetwarzanie tekstu – można użyć podziału na wyrazy, ignorując interpunkcję i wielkość liter.
- Obliczenie liczby wystąpień danego wyrazu w każdym dokumencie.
- Dla każdego zapytania, zwrócenie posortowanej listy indeksów dokumentów.
"""


def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
    # Oczyszczamy dokumenty
    cleaned_documents = [clean_text(doc) for doc in documents]

    results = []
    # Dla każdego zapytania
    for query in queries:
        query = query.lower()  # Zmieniamy zapytanie na małe litery
        document_count = []

        # Liczymy wystąpienia zapytania w każdym dokumencie
        for idx, doc in enumerate(cleaned_documents):
            count = doc.count(query)  # Liczymy wystąpienia zapytania w dokumencie
            if count > 0:
                document_count.append((count, idx))

        # Sortujemy po liczbie wystąpień malejąco, a potem po indeksie dokumentu rosnąco
        document_count.sort(key=lambda x: (-x[0], x[1]))

        # Zbieramy tylko indeksy dokumentów
        result = [idx for _, idx in document_count]
        results.append(result)

    return results


# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
=======
import string

def clean_text(text: str) -> list[str]:
    """
    Funkcja oczyszcza tekst z interpunkcji i zamienia wszystkie litery na małe.
    """
    # Usuwamy interpunkcję i zamieniamy na małe litery
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Zwracamy listę wyrazów
    return text.split()
"""
Zadanie 3 - Indeksowanie dokumentów

Opis zadania:
- Wejście:
    * Pierwsza linia: liczba dokumentów do przetworzenia (n).
    * Kolejne n linii: dokumenty (każdy dokument to wielowyrazowy ciąg znaków).
    * Następna linia: liczba zapytań (m).
    * Kolejne m linii: zapytania (każdy zapytanie to pojedynczy wyraz).
- Wyjście:
    * m linii, z których każda zawiera listę numerów dokumentów, w których wystąpił wyraz z zapytania.
    * Każda lista jest posortowana według częstości wystąpienia zapytania w danym dokumencie (od największej do najmniejszej).
    * W przypadku równych częstości, lista może być posortowana malejąco wg numeru dokumentu (opcjonalnie).
    * Jeśli słowo nie wystąpiło w żadnym dokumencie, zwróć pustą listę.

Przykładowe wejście:
    3
    Your care set up, do not pluck my care down.
    Your care set up, do not pluck my care down.
    Your care is gain of care when new care is won.
    2
    care
    is

Przykładowe wyjście:
    [1, 2, 0]
    [2, 1]

Wymagania:
- Implementacja funkcji `index_documents(documents: list[str], queries: list[str]) -> list[list[int]]`.
- Przetwarzanie tekstu – można użyć podziału na wyrazy, ignorując interpunkcję i wielkość liter.
- Obliczenie liczby wystąpień danego wyrazu w każdym dokumencie.
- Dla każdego zapytania, zwrócenie posortowanej listy indeksów dokumentów.
"""


def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
    # Oczyszczamy dokumenty
    cleaned_documents = [clean_text(doc) for doc in documents]

    results = []
    # Dla każdego zapytania
    for query in queries:
        query = query.lower()  # Zmieniamy zapytanie na małe litery
        document_count = []

        # Liczymy wystąpienia zapytania w każdym dokumencie
        for idx, doc in enumerate(cleaned_documents):
            count = doc.count(query)  # Liczymy wystąpienia zapytania w dokumencie
            if count > 0:
                document_count.append((count, idx))

        # Sortujemy po liczbie wystąpień malejąco, a potem po indeksie dokumentu rosnąco
        document_count.sort(key=lambda x: (-x[0], x[1]))

        # Zbieramy tylko indeksy dokumentów
        result = [idx for _, idx in document_count]
        results.append(result)

    return results


# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
>>>>>>> 78f3fce681cda5442b429da15d89cf0d8ff67ff5
        print(res)