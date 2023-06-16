import simplejson as json
import yaml
import xmltodict
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os

def parsuj_argumenty():
    if len(sys.argv) != 3:
        print("Sposób użycia: program.py pathFile1.x pathFile2.y")
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
        messagebox.showerror("Błąd", f"Plik '{file}' nie istnieje.")
        sys.exit(1)
    except json.JSONDecodeError:
        messagebox.showerror("Błąd", f"Błąd podczas parsowania pliku '{file}'. Sprawdź poprawność składni JSON.")
        sys.exit(1)

def zapisz_json(data, file):
    try:
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Sukces", f"Dane zapisane do pliku '{file}' w formacie JSON.")
    except:
        messagebox.showerror("Błąd", f"Błąd podczas zapisu danych do pliku '{file}'.")

def wczytaj_yaml(file):
    try:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except FileNotFoundError:
        messagebox.showerror("Błąd", f"Plik '{file}' nie istnieje.")
        sys.exit(1)
    except yaml.YAMLError:
        messagebox.showerror("Błąd", f"Błąd podczas parsowania pliku '{file}'. Sprawdź poprawność składni YAML.")
        sys.exit(1)

def zapis_yaml(data, file):
    try:
        with open(file, 'w') as f:
            yaml.dump(data, f)
        messagebox.showinfo("Sukces", f"Dane zapisane do pliku '{file}' w formacie YAML.")
    except:
        messagebox.showerror("Błąd", f"Błąd podczas zapisu danych do pliku '{file}'.")

def wczytaj_xml(file):
    try:
        with open(file, 'r') as f:
            data = xmltodict.parse(f.read())
        return data
    except FileNotFoundError:
        messagebox.showerror("Błąd", f"Plik '{file}' nie istnieje.")
        sys.exit(1)
    except xmltodict.ParseError:
        messagebox.showerror("Błąd", f"Błąd podczas parsowania pliku '{file}'. Sprawdź poprawność składni XML.")
        sys.exit(1)

def zapisz_xml(data, file):
    try:
        with open(file, 'w') as f:
            xml_str = xmltodict.unparse({'root': data}, pretty=True)
            f.write(xml_str)
        messagebox.showinfo("Sukces", f"Dane zapisane do pliku '{file}' w formacie XML.")
    except:
        messagebox.showerror("Błąd", f"Błąd podczas zapisu danych do pliku '{file}'.")

def sprawdz_format(plik):
    ext = plik.split('.')[-1].lower()
    if ext in ['json', 'yaml', 'yml', 'xml']:
        return ext
    else:
        messagebox.showerror("Błąd", f"Nieobsługiwany format pliku '{plik}'.")
        sys.exit(1)

def wczytaj_asynchronicznie(file, format):
    if format == 'json':
        return wczytaj_json(file)
    elif format in ['yaml', 'yml']:
        return wczytaj_yaml(file)
    elif format == 'xml':
        return wczytaj_xml(file)

def zapisz_asynchronicznie(data, file, format):
    if format == 'json':
        zapisz_json(data, file)
    elif format in ['yaml', 'yml']:
        zapisz_yaml(data, file)
    elif format == 'xml':
        zapisz_xml(data, file)

def przetworz_pliki():
    file1 = filedialog.askopenfilename()
    new_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json"), ("YAML", "*.yaml"), ("XML", "*.xml")])

    ext1 = sprawdz_format(file1)
    ext2 = new_file.split('.')[-1].lower()

    if ext1 == ext2:
        messagebox.showinfo("Informacja", "Formaty plików są identyczne. Brak konieczności konwersji.")
    else:
        data1 = wczytaj_asynchronicznie(file1, ext1)
        t = threading.Thread(target=zapisz_asynchronicznie, args=(data1, new_file, ext2))
        t.start()

def main():
    root = tk.Tk()
    root.withdraw()

    przetworz_pliki()

if __name__ == '__main__':
    main()