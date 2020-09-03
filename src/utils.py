import os


def clear():
    return
    # os.system('cls' if os.name == 'nt' else 'clear')


def existence_error(direction):
    return f"It is impossible to move {direction} from here. There is simply nowhere to go!"


def pause():
    input("\n\nPress enter to continue from here.")


def display_text(text):
    clear()
    print(text)
    pause()
