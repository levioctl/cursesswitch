# Usage
## An Example Script
The following example.py script is agnostic of whether using ncurses or directly to console:
```python
import time
from cursesswitch import printer

def main():
    printer.print_line("Red line", color="red")
    time.sleep(1)
    printer.clear_screen()
    printer.print_line("Bold blue line", color="blue", is_bold=True)
    time.sleep(1)

printer.wrapper(main)
```

## Running with ncurses
```
$ python example.py
```
(Colored text does not work in github's markdown)

Output:

During the first second:

Red line

During the 2nd second:

Bold blueline

## Running without ncurses
```
$ MODE=direct python example.py
```
Output:

Red line

Bold blueline
