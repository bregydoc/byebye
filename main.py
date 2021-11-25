from pyfiglet import figlet_format
from time import sleep
from sys import stdout
from subprocess import run


CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

COUNTDOWN = 10


def delete_last_lines(n=1):
    for _ in range(n):
        stdout.write(CURSOR_UP_ONE)
        stdout.write(ERASE_LINE)


def last_words():
    print(figlet_format("The End", font="doom"))
    print("Bye bye world. This is my last instruction before my reboot.")
    print("I hope you enjoyed my program. I hope you will come back.")

    for i in range(0, COUNTDOWN):
        print(figlet_format(f"{COUNTDOWN-i}", font="drpepper"))
        delete_last_lines(5)
        sleep(1)

    print(figlet_format("Rebooting", font="doom"))

    run("reboot")


if __name__ == "__main__":
    last_words()
