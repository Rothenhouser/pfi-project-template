# example_project

Ein Beispielprojekt für Datenanalyse, Reports etc mit geteilten Routinen, 
Notebooks und Skripten.

Das Projekt wird in der Umgebung installiert: Module können dann aus anderen 
Ordnern importiert werden.

## Installation 
Neues virtual Environment anlegen und externe Pakete installieren.

In cmd.exe:
```cmd
python -m venv .venv
.venv\Scripts\activate.bat        # VSCode kann diesen Schritt übernehmen
pip install -r requirements.txt
#  WICHTIG: lokale Installation,  ermöglicht 
# z.B. Notebooks, eigenen Code zu importieren
pip install -e .                   
```

## Code formatieren und linten

```cmd
# Automatische Formatierung nach PEP8:
ruff format .
# Überprüfung auf übliche Fehlerquellen, Abweichungen von Best Practices etc:
ruff check .
```

## Notebooks ausführen

Vom Projekthauptordner entweder:
1. Projekt in VSCode öffnen und Notebooks da starten.
2. `jupyter lab` , dort Notebooks starten.

## Skripte ausführen

```cmd
python scripts\check_data.py
```

## Tests ausführen

Automatisiertes Testen kann z.B. zeigen, dass Änderungen keine anderen Funktionen zerstören.

```cmd
pytest .
```

## Projektstruktur

```
├── README.md          <- Information für Entwickler
├── data               <- Inputdaten für das Projekt
├── docs               <- Dokumentation zum Projekt
├── reports            <- Ergebnisse - HTML, PDF, Excel etc.
│   └── figures        <- Fertige Plots und Grafiken
├── requirements.txt   <- Externe Pakete, die im Projekt nötig sind. 
│                          Kann mit `pip freeze > requirements.txt` erzeugt werden. 
│                          Versionsnummern sind optional.
├── .gitignore         <- Files die von git ignoriert werden sollen
├── .env               <- Umgebungsvariablen, nicht in git!
│
├── notebooks          <- Jupyter notebooks. 
├── example_project    <- Wiederverwendbarer Code in diesem Projekt
│   ├── __init__.py    <- Ordner als Python Modul markieren
│   ├── config.py      <- Pfade festlegen
│   ├── dataset.py     <- Funktionen um Daten zu lesen
│   ├── analysis.py    <- Funktionen zur Datenprozessierung/-analyse
│   └── plots.py       <- Funktionen zur Visualisierung
|── scripts            <- Direkt ausführbare Skripte
|   └── check_data.py  <- Überpruft Metadaten im Datenordner
└── tests              <- Automatisch ausführbare Tests 
    ├── test_analysis.py  
    └── test_dataset.py    
```

--------

