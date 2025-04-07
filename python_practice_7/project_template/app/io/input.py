import pandas as pd

def read_from_console():
    """Зчитує текстовий рядок з консолі від користувача."""
    return input("Введіть текст: ")

def read_from_file_builtin(path):
    """Зчитує вміст текстового файлу за допомогою вбудованих засобів Python."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_from_file_pandas(path):
    """Зчитує CSV-файл за допомогою pandas і повертає перші 5 рядків."""
    df = pd.read_csv(path)
    return df.head().to_string(index=False)

