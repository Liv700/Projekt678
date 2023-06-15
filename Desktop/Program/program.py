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

def wczytaj_yaml(file):
    try:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except FileNotFoundError:
        print(f"Plik '{file}' nie istnieje.")
        sys.exit(1)
    except yaml.YAMLError:
        print(f"Błąd podczas parsowania pliku '{file}'. Sprawdź poprawność składni YAML.")
        sys.exit(1)

def zapis_yaml(data, file):
    try:
        with open(file, 'w') as f:
            yaml.dump(data, f)
        print(f"Dane zapisane do pliku '{file}' w formacie YAML.")
    except:
        print(f"Błąd podczas zapisu danych do pliku '{file}'.")

def wczytaj_xml(file):
    try:
        with open(file, 'r') as f:
            data = xmltodict.parse(f.read())
        return data
    except FileNotFoundError:
        print(f"Plik '{file}' nie istnieje.")
        sys.exit(1)
    except xmltodict.ParseError:
        print(f"Błąd podczas parsowania pliku '{file}'. Sprawdź poprawność składni XML.")
        sys.exit(1)

def zapisz_xml(data, file):
    try:
        with open(file, 'w') as f:
            xml_str = xmltodict.unparse({'root': data}, pretty=True)
            f.write(xml_str)
        print(f"Dane zapisane do pliku '{file}' w formacie XML.")
    except:
        print(f"Błąd podczas zapisu danych do pliku '{file}'.")

def sprawdz_format(plik):
    ext = plik.split('.')[-1].lower()
    if ext in ['json', 'yaml', 'yml', 'xml']:
        return ext
    else:
        print(f"Nieobsługiwany format pliku '{plik}'.")
        sys.exit(1)
        
        
file1, file2 = parsuj_argumenty()

ext1 = sprawdz_format(file1)
ext2 = sprawdz_format(file2)