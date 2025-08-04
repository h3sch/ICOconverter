================================
   ICO-KONVERTER MIT VORSCHAU
================================

Ein einfaches, benutzerfreundliches Tool zur Umwandlung von JPG- oder PNG-Bildern in ICO-Dateien für Windows-Icons – mit Vorschau, Größenwahl, Bit-Tiefe und Drag & Drop.

Das Programm basiert auf Python und nutzt die Bibliotheken:
- Pillow (Bildverarbeitung)
- tkinterdnd2 (Drag & Drop)
- customtkinter (moderne GUI mit Darkmode)

-------------------------------------------
FEATURES
-------------------------------------------
Drag & Drop von Bildern direkt ins Fenster  
Vorschau des Bildes vor dem Konvertieren  
Auswahl mehrerer ICO-Größen: 16, 32, 48, 64, 128, 256 px  
Bit-Tiefe: 16 Bit (RGB) oder 32 Bit (RGBA mit Transparenz)  
Automatische Benennung: Ursprungsname_ico.ico   

-------------------------------------------
INSTALLATION
-------------------------------------------
1. Python 3.x installieren (https://www.python.org)

2. Projektordner vorbereiten:
   - Dieses Skript speichern (z. B. als konverter.py)
   - Optional: README.md hinzufügen

3. Benötigte Pakete installieren:

   pip install pillow tkinterdnd2 customtkinter

   (Unter Linux/macOS evtl. zusätzlich:
    sudo apt install python3-tk
    bzw.
    brew install python-tk)

-------------------------------------------
VERWENDUNG
-------------------------------------------
1. Script starten:

   python konverter.py

2. Bild in das Fenster ziehen oder über "Bild auswählen" öffnen

3. Größen & Bit-Tiefe wählen

4. Vorschau erscheint automatisch

5. Button "Konvertieren" klicken

6. Zielordner wählen → Datei wird als <ursprungsname>_ico.ico gespeichert

-------------------------------------------
BEISPIEL

Datei:  cooles_logo.png  
Größen: 32, 64, 256  
Bit-Tiefe: 32 Bit

→ Ergebnis: cooles_logo_ico.ico im gewählten Zielordner

-------------------------------------------
EMPFEHLUNGEN

- Idealerweise quadratische Bilder verwenden (z. B. 512×512 px)
- 32-Bit-Icons für Icons mit Transparenz oder runden Formen
- Keine ICO-Größen auswählen, die größer sind als das Originalbild

-------------------------------------------
OPTIONALE ERWEITERUNGEN (TODO)

- Checkbox „Alle Größen auswählen“
- Automatische Zielordnerwahl (z. B. neben dem Originalbild)
- Fortschrittsanzeige
- Kommandozeilen-Modus
- Light/Darkmode-Umschaltung

-------------------------------------------
LIZENZ

MIT License – frei nutzbar, anpassbar und erweiterbar.  
Verwendung der generierten Icons erfolgt auf eigene Verantwortung.

-------------------------------------------
ASCII CREDITS

              _______________
             |               |
             |   .-----.     |
             |  /       \    |
             | |   o o   |   |   <- Icon Generator
             |  \   ∆   /    |
             |   '-----'     |
             |_______________|

         Powered by Python + Pillow
