# SmartTasker - Inteligentny Asystent Zadań i Notatek

## Opis

SmartTasker to narzędzie oparte na NLP, które pomaga zarządzać zadaniami i notatkami. Umożliwia dodawanie zadań i notatek za pomocą naturalnego języka, inteligentnie je kategoryzuje i umożliwia szybki dostęp do informacji. Wykorzystuje bazę danych SQLite do przechowywania danych.

## Funkcjonalności

- **Dodawanie zadań:** Dodawanie zadań z terminami, kategoriami i priorytetami za pomocą naturalnego języka.
- **Dodawanie notatek:** Dodawanie notatek i ich kategoryzowanie.
- **Ekstrakcja informacji:** Wyodrębnianie dat, godzin, kategorii i priorytetów z tekstu.
- **Kategoryzacja:** Automatyczne kategoryzowanie notatek i zadań.
- **Przechowywanie danych:** Użycie bazy danych SQLite do przechowywania zadań i notatek.
- **Interakcja:** Interfejs wiersza poleceń (CLI).
- **Wyświetlanie:** Możliwość wyświetlania zadań i notatek z opcją filtrowania po kategorii.
- **Oznaczanie zadań:** Oznaczanie zadań jako ukończone.
- **Usuwanie:** Możliwość usuwania zadań i notatek.

## Technologie

-   **Python 3.8+**
-   **NLTK:** biblioteka NLP do tokenizacji tekstu
-   **dateparser:** do analizy dat i godzin
-   **sqlite3 (wbudowany w Python):** do przechowywania danych
-   **rich:** do ładnego formatowania tekstu w CLI
-   **click:** do budowy interfejsu CLI

## Instalacja

1.  Sklonuj repozytorium:
    ```bash
    git clone https://github.com/TwojNick/SmartTasker.git
    ```
2.  Przejdź do katalogu projektu:
    ```bash
    cd SmartTasker
    ```
3.  Stwórz wirtualne środowisko:
    ```bash
    python3 -m venv venv
    ```
4.  Aktywuj wirtualne środowisko
    ```bash
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate # Windows
    ```
5.  Zainstaluj wymagane biblioteki:
    ```bash
    pip install -r requirements.txt
    ```

## Uruchomienie

1.  Uruchom aplikację z głównego pliku:
    ```bash
    python -m smarttasker.cli
    ```
2.  Wykorzystaj interfejs CLI, aby dodawać i zarządzać zadaniami i notatkami.

## Przykłady użycia

-   **Dodawanie zadania:**
    ```bash
    python -m smarttasker.cli add-task "kup mleko jutro rano"
    python -m smarttasker.cli add-task "pilne zadzwon do szefa"
    ```
-   **Dodawanie notatki:**
    ```bash
    python -m smarttasker.cli add-note "przepis na ciasto z jabłkami do domu"
    ```
-  **Wyświetlanie zadań:**
    ```bash
    python -m smarttasker.cli show-tasks
    python -m smarttasker.cli show-tasks -c praca
    ```
-  **Wyświetlanie notatek:**
     ```bash
     python -m smarttasker.cli show-notes
     python -m smarttasker.cli show-notes -c dom
    ```
-   **Oznaczanie zadania jako ukończone**
    ```bash
    python -m smarttasker.cli complete-task 0
    ```
-   **Usuwanie zadania:**
    ```bash
    python -m smarttasker.cli remove-task 0
    ```
-    **Usuwanie notatki:**
    ```bash
    python -m smarttasker.cli remove-note 0
    ```

## Testy

1. Aby uruchomić testy wpisz:
   ```bash
   python -m unittest discover tests