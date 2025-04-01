from laba6 import treasure_division, safe_crack,rpsls,bonus_system,pirate_escape
def main():
    """Головне меню"""
    games = {
        "1": treasure_division,
        "2": safe_crack,
        "3": rpsls,
        "4": bonus_system,
        "5": pirate_escape
    }
    while True:
        print("\nОберіть гру:")
        print("1 - Скарбниця короля")
        print("2 - Код сейфу")
        print("3 - Камінь-ножиці-папір-ящірка-Спок")
        print("4 - Система бонусів")
        print("5 - Втеча з острова піратів")
        print("0 - Вийти")
        choice = input("Ваш вибір: ")
        if choice == "0":
            break
        elif choice in games:
            games[choice]()
        else:
            print("Некоректний вибір!")

if __name__ == "__main__":
    main()
