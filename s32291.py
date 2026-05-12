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
    if description:
        header = f">{seq_id} {description}"
    else:
        header = f">{seq_id}"
    linie = []
    for i in range(0, len(sequence), line_width):
        linie.append(sequence[i:i + line_width])
    return header + "\n" + "\n".join(linie) + "\n"


def validate_positive_int(prompt: str,
                          min_val: int = 1,
                          max_val: int = 100_000) -> int:
    """Pobiera od użytkownika liczbę całkowitą z przedziału [min_val, max_val].
    W przypadku błędu pyta ponownie."""
    while True:
        raw = input(prompt)
        try:
            wartosc = int(raw)
            if min_val <= wartosc <= max_val:
                return wartosc
            else:
                print(f"Błąd: wartość musi być w przedziale [{min_val}, {max_val}].")
        except ValueError:
            print(f"Błąd: wartość musi być w przedziale [{min_val}, {max_val}].")


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