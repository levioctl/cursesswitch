import time
import cursesswitch

def main():
    cursesswitch.print_line("Red line", color="red")
    time.sleep(1)
    cursesswitch.clear_screen()
    cursesswitch.print_line("Bold blue line", color="blue", is_bold=True)
    time.sleep(1)

cursesswitch.wrapper(main)
