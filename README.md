# Path of Exile 2 Market Clicker

Dieses Skript wurde entwickelt, um Spielern von Path of Exile 2 einen zeitlichen Vorteil beim Handeln zu verschaffen. Es erkennt automatisch Handelsangebote, die auf dem Bildschirm erscheinen, und klickt sofort darauf. Dies erspart dem Benutzer das manuelle Überwachen und Klicken auf Angebote.

## Funktionsweise

Das Skript überwacht den Bildschirm nach einem bestimmten Bild (`whisper.png`), das anzeigt, dass ein neues Handelsangebot von einem anderen Spieler eingegangen ist. Sobald das Bild erkannt wird, klickt das Skript automatisch darauf, um das Angebot anzunehmen.

## Verwendung

1. **Suchbereich definieren**: Beim Start des Skripts wird der Benutzer aufgefordert, den Bereich des Bildschirms zu definieren, in dem die Handelsangebote erscheinen. Dies geschieht durch zwei Mausklicks: einen auf die obere linke Ecke und einen auf die untere rechte Ecke des Suchbereichs. Der Suchbereich sollte der Bereich sein, in dem der Whisper-Button erscheint, wenn ein Live-Angebot erscheint, damit das Skript darauf klicken kann.

2. **Hotkeys**:
    - `p`: Pausiert oder setzt das Skript fort.
    - `r`: Setzt den Suchbereich zurück.
    - `q`: Beendet das Skript.

3. **Automatische Erkennung**: Das Skript sucht kontinuierlich nach dem Begriff "whisper" im definierten Suchbereich. Wenn der Begriff gefunden wird, klickt das Skript automatisch darauf.

4. **Fehlerhafte Angebote**: Wenn das Fenster "invalid offer" im Browser erscheint, pausiert das Skript die Suche nach neuen Angeboten für eine Minute, um die Seite nicht zu spammen.

## Voraussetzungen

- Python 3.x
- `pynput` Bibliothek
- `pyautogui` Bibliothek
- `opencv-python` Bibliothek

## Installation

1. Klone das Repository:
    ```bash
    git clone https://github.com/DeinBenutzername/Path-of-Exile-2-Market-Clicker.git
    ```
2. Installiere die benötigten Bibliotheken:
    ```bash
    pip install -r requirements.txt
    ```
3. Starte das Skript:
    ```bash
    python main.py
    ```

## Hinweise

This is an open-source project provided without any guarantees. Use it at your own risk.
Please ensure that you comply with EVE Online's terms of use and policies. The use of bots or automation may violate the game's terms of service.

## Build standalone exe file

python -m pip install pyinstaller
python -m PyInstaller main.spec