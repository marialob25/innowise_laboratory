from colorama import init, Fore, Back, Style

# Инициализация colorama для корректного вывода цветов
init()

# Примеры цветного вывода
print(Fore.RED + Back.YELLOW + 'Hello World!' + Style.RESET_ALL)
print(Fore.GREEN + Back.WHITE + 'Hello World!' + Style.RESET_ALL)
print(Fore.BLUE + Back.LIGHTWHITE_EX + 'Hello World!' + Style.RESET_ALL)
print(Fore.MAGENTA + Back.CYAN +
      'Hello World with Magenta text and Cyan background!' + Style.RESET_ALL)
