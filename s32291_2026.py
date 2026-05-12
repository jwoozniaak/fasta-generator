# Album number : s32291
# Date         : 12-05-2026
# Description  : Generator losowych sekwencji nukleotydowych DNA w formacie FASTA.
#                Program generuje sekwencje z nukleotydów {A, C, G, T},
#                zapisuje je do pliku .fasta oraz oblicza statystyki.
#                Dodatkowe funkcje: wyszukiwanie motywów, sekwencja komplementarna,
#                transkrypcja mRNA, konfigurowalny rozkład nukleotydów.

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

def find_motif(sequence: str, motif: str) -> list:
    """Szuka motywu w sekwencji. Zwraca listę pozycji (od 1)."""
    pozycje = []
    start = 0
    while True:
        pos = sequence.find(motif, start)
        if pos == -1:
            break
        pozycje.append(pos + 1)
        start = pos + 1
    return pozycje

def complement(sequence: str) -> str:
    """Zwraca nić komplementarną do sekwencji DNA."""
    wynik = ""
    for litera in sequence:
        if litera == "A":
            wynik += "T"
        elif litera == "C":
            wynik += "G"
        elif litera == "G":
            wynik += "C"
        elif litera == "T":
            wynik += "A"
        else:
            wynik += litera
    return wynik

def reverse_complement(sequence: str) -> str:
    """Zwraca nić odwrotnie komplementarną."""
    return complement(sequence)[::-1]

def transcribe_to_mrna(sequence: str) -> str:
    """Zwraca sekwencję mRNA - zamienia T na U."""
    wynik = ""
    for litera in sequence:
        if litera == "T":
            wynik += "U"
        else:
            wynik += litera
    return wynik

def generate_sequence_custom(length: int, weights: dict) -> str:
    """Generuje sekwencję DNA z zadanym rozkładem nukleotydów."""
    nukleotydy = ['A', 'C', 'G', 'T']
    wagi = [weights['A'], weights['C'], weights['G'], weights['T']]
    return ''.join(random.choices(nukleotydy, weights=wagi, k=length))

def pobierz_rozklad() -> dict:
    """Pobiera od użytkownika procentowy rozkład nukleotydów."""
    while True:
        print("\nPodaj procentowy udział każdego nukleotydu (suma musi być 100):")
        try:
            a = float(input("A: "))
            c = float(input("C: "))
            g = float(input("G: "))
            t = float(input("T: "))
            if round(a + c + g + t) == 100:
                return {'A': a, 'C': c, 'G': g, 'T': t}
            else:
                print(f"Błąd: suma wynosi {a+c+g+t}, a musi być 100!")
        except ValueError:
            print("Błąd: podaj liczby!")

def main():
    """Główna funkcja programu."""
    length = validate_positive_int("Podaj długość sekwencji: ")
    odpowiedz = input("\nCzy chcesz podać własny rozkład nukleotydów? [t/n]: ")
    if odpowiedz.lower() == 't':
        weights = pobierz_rozklad()
        sekwencja = generate_sequence_custom(length, weights)
    else:
        sekwencja = generate_sequence(length)

    seq_id = input("Podaj identyfikator sekwencji: ").strip()
    while not seq_id or any(c.isspace() for c in seq_id):
        print("Błąd: identyfikator nie może być pusty ani zawierać spacji.")
        seq_id = input("Podaj identyfikator sekwencji: ").strip()
    description = input("Podaj opis sekwencji (opcjonalnie): ").strip()
    name = input("Podaj swoje imię: ").strip()
    while not name:
        print("Błąd: imię nie może być puste.")
        name = input("Podaj swoje imię: ").strip()

    stats = calculate_stats(sekwencja)
    print(f"\nStatystyki sekwencji (n={length}):")
    print(f"  A: {stats['A']:.2f}%")
    print(f"  C: {stats['C']:.2f}%")
    print(f"  G: {stats['G']:.2f}%")
    print(f"  T: {stats['T']:.2f}%")
    print(f"  GC-content: {stats['GC']:.2f}%")

    sekwencja_z_imieniem = insert_name(sekwencja, name)
    fasta_tekst = format_fasta(seq_id, description, sekwencja_z_imieniem)
    nazwa_pliku = f"{seq_id}.fasta"
    with open(nazwa_pliku, "w", encoding="utf-8") as f:
        f.write(fasta_tekst)
    print(f"\nSekwencja zapisana do pliku: {nazwa_pliku}")

    motyw = input("\nPodaj motyw do wyszukania (np. ATG): ").strip().upper()
    if motyw:
        pozycje = find_motif(sekwencja, motyw)
        if pozycje:
            print(f"Motyw '{motyw}' znaleziony na pozycjach: {pozycje}")
            print(f"Liczba wystąpień: {len(pozycje)}")
        else:
            print(f"Motyw '{motyw}' nie został znaleziony.")

    print("\nNić komplementarna:")
    print(complement(sekwencja))
    print("Nić odwrotnie komplementarna:")
    print(reverse_complement(sekwencja))
    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(format_fasta(f"{seq_id}_complement", "complementary strand", complement(sekwencja)))
        f.write(format_fasta(f"{seq_id}_revcomp", "reverse complement strand", reverse_complement(sekwencja)))
    print("Dodano rekordy komplementarne do pliku FASTA.")

    print(f"\nSekwencja mRNA:")
    print(transcribe_to_mrna(sekwencja))
    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(format_fasta(f"{seq_id}_mRNA", "in silico transcription", transcribe_to_mrna(sekwencja)))
    print(f"Sekwencja mRNA dodana do pliku FASTA.")

if __name__ == "__main__":
    main()