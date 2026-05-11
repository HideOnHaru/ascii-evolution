

Dieses Projekt implementiert einen evolutionären Algorithmus in Python. Ziel des Programms ist es, zufällige Zeichenketten schrittweise an einen vorgegebenen Ziel-String anzupassen. Dafür werden Tournament Selection, Crossover und Mutation verwendet.

Zum Ausführen des Projekts werden Python 3.11 oder höher sowie uv benötigt. Die Abhängigkeiten können mit folgendem Befehl installiert werden:
uv sync

Das Programm kann anschließend mit folgendem Befehl gestartet werden:
uv run main.py

Die Fitness eines Strings wird über die ASCII-Distanz zum Ziel-String berechnet. Je kleiner der Fitness-Wert ist, desto näher liegt der erzeugte String am Ziel.