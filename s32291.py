# Album number : s32291
# Date         : 2026-05-12
# Description  : Generator losowych sekwencji DNA w formacie FASTA
import random

def generate_sequence(length: int) -> str:
    """Zwraca losową sekwencję DNA o podanej długości."""
    nukleotydy = ['A', 'C', 'G', 'T']
    return ''.join(random.choices(nukleotydy, k=length))

def calculate_stats(sequence: str) -> dict:
    """Zwraca słownik statystyk sekwencji.
    Klucze: 'A', 'C', 'G', 'T' (float, %), 'GC' (float, %).
    """
    n = len(sequence)
    stats = {
        'A': round(sequence.count('A') / n * 100, 2),
        'C': round(sequence.count('C') / n * 100, 2),
        'G': round(sequence.count('G') / n * 100, 2),
        'T': round(sequence.count('T') / n * 100, 2),
    }
    stats['GC'] = round(stats['G'] + stats['C'], 2)
    return stats

def insert_name(sequence: str, name: str) -> str:
    """Wstawia imię w losowej pozycji sekwencji. Imię małymi literami."""
    pozycja = random.randint(0, len(sequence))
    name_lower = name.lower()
    return sequence[:pozycja] + name_lower + sequence[pozycja:]


def format_fasta(seq_id: str, description: str,
                 sequence: str, line_width: int = 80) -> str:
    """Zwraca sformatowany rekord FASTA jako string."""
    # TODO: zbuduj nagłówek zaczynający się od >
    # TODO: podziel sekwencję na linie po line_width znaków
    pass


def validate_positive_int(prompt: str,
                          min_val: int = 1,
                          max_val: int = 100_000) -> int:
    """Pobiera od użytkownika liczbę całkowitą z przedziału [min_val, max_val].
    W przypadku błędu pyta ponownie."""
    # TODO: użyj pętli while
    # TODO: obsłuż błąd gdy użytkownik wpisze tekst zamiast liczby (try/except)
    # TODO: sprawdź czy liczba jest w przedziale
    pass


def main():
    """Główna funkcja programu."""
    # TODO: pobierz dane od użytkownika
    # TODO: wygeneruj sekwencję
    # TODO: oblicz statystyki
    # TODO: wstaw imię
    # TODO: zapisz plik FASTA
    # TODO: wyświetl statystyki
    pass


if __name__ == "__main__":
    main()