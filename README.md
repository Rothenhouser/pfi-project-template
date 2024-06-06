# example_project

Ein Beispielprojekt mit wiederverwendbarem Teil, Notebooks und Skripten.

## Installation 
Neues Virtual Environment anlegen und externe Pakete installieren:

1. Zweitneueste stabile Pythonversion von python.org installieren.
2. `cmd.exe` im Projektordner starten und sicherstellen dass das neue Python im PATH ganz oben ist: `where pip`.
2. Virtual Environment anlegen: `python -m venv .venv`
4. Virtual Environment aktivieren:`.venv\Scripts\activate.bat`
4. Prüfen, dass jetzt dass Python aus  dem  Virtual Environment  im PATH ganz oben ist: `where pip`
5. Alle nötigen Pakete installieren: `python -m pip install -r requirements.txt`
6. Dieses Projekt als Paket installieren: `python -m pip install -e .` Dieser Schritt ist nötig, um Pythoncode aus dem "example_project" Ordner auch in anderen Ordnern zugänglich zu machen.

Sicherstellen, dass in VSCode die Python Extension installiert ist.

VSCode müsste dann in diesem Ordner das bestehende `.venv` als Pythonkernel erkennen. Wenn das geklappt hat, aktiviert VSCode das Virtual Environment automatisch in seinem Terminalfenster, und die weiteren Kommandos können dort ohne Probleme ausgeführt werden.

Auch in Jupyter Notebooks werden Befehle wie `!pip install -r requirements.txt` dann im richtigen Virtual Environment ausgeführt.

Neue Pakete nur über requirements.txt hinzufügen! Damit wird kommuniziert, was für dieses Projekt nötig ist.

## Code formatieren und linten

```cmd
isort .
black .
flake8 .
```

Alternativ jeweils `python -m black .` etc.

## Notebooks ausführen

Entweder:
1. Projekt in VSCode öffnen und Notebooks da starten.
2. `jupyter lab`, dort Notebooks starten.

## Skripte ausführen

```cmd
python scripts\check_data.py
```

## Projektorganisation

```
├── README.md          <- Information für Entwickler.
├── data               <- Inputdaten für das Projekt.
├── docs               <- Dokumentation zum Projekt.
├── reports            <- Ergebnisse - HTML, PDF, Excel etc.
│   └── figures        <- Fertige Plots und Grafiken
├── requirements.txt   <- Externe Pakete, die im Projekt nötig sind. 
│                          Kann mit `pip freeze > requirements.txt` erzeugt werden. 
│                          Versionsnummern sind optional.
├── .flake8            <- Konfiguration für flake8
├── .gitignore         <- Files die von git ignoriert werden sollen
├── .env               <- Umgebungsvariablen, nicht in git
│
├── notebooks          <- Jupyter notebooks. 
├── example_project    <- Wiederverwendbarer Code in diesem Projekt
│   ├── __init__.py    <- Ordner als Python Modul markieren
│   ├── config.py      <- Pfade festlegen
│   ├── dataset.py     <- Funktionen um Daten zu lesen
│   ├── analysis.py    <- Funktionen zur Datenprozessierung/-analyse
│   └── plots.py       <- Funktionen zur Visualisierung
└── scripts            <- Direkt ausführbare Skripte
    └── check_data.py  <- Überprüft Metadaten im Datenordner
```

--------

