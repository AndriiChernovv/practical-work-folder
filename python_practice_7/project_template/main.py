
from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    text1 = read_from_console()
    print_to_console("Введений текст з консолі:")
    print_to_console(text1)
    write_to_file("data/output_console.txt", text1)

    try:
        text2 = read_from_file_builtin("data/input.txt")
        print_to_console("\nТекст із файлу (builtin):")
        print_to_console(text2)
        write_to_file("data/output_builtin.txt", text2)
    except FileNotFoundError:
        print_to_console("Файл data/input.txt не знайдено.")

    try:
        text3 = read_from_file_pandas("data/input.csv")
        print_to_console("\nДані з CSV (pandas):")
        print_to_console(text3)
        write_to_file("data/output_pandas.txt", text3)
    except FileNotFoundError:
        print_to_console("Файл data/input.csv не знайдено.")

if __name__ == "__main__":
    main()
