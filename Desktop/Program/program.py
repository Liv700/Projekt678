import simplejson as json
import yaml
import xmltodict
import sys

def parsuj_argumenty():
    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    return file1, file2

def wczytaj_json(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Plik '{file}' nie istnieje.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Błąd podczas parsowania pliku '{file}'. Sprawdź poprawność składni JSON.")
        sys.exit(1)

def zapisz_json(data, file):
    try:
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dane zapisane do pliku '{file}' w formacie JSON.")
    except:
        print(f"Błąd podczas zapisu danych do pliku '{file}'.")
        
file1, file2 = parsuj_argumenty()