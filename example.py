import time
from cursesswitch import printer

def main():
    printer.print_line("Red line", color="red")
    time.sleep(1)
    printer.clear_screen()
    printer.print_line("Bold blue line", color="blue", is_bold=True)
    time.sleep(1)

printer.wrapper(main)
