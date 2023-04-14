import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Define arrow key constants
    UP = curses.KEY_UP
    DOWN = curses.KEY_DOWN
    LEFT = curses.KEY_LEFT
    RIGHT = curses.KEY_RIGHT

    # Initialize variables
    selected = 0
    choices = ['Option 1', 'Option 2', 'Option 3']

    # Main loop
    while True:
        # Draw menu
        for i, choice in enumerate(choices):
            if i == selected:
                stdscr.addstr(i, 0, f'> {choice}')
            else:
                stdscr.addstr(i, 0, f'  {choice}')

        # Get input
        key = stdscr.getch()

        # Handle input
        if key == UP:
            selected = (selected - 1) % len(choices)
        elif key == DOWN:
            selected = (selected + 1) % len(choices)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Do something with selected choice
            stdscr.addstr(len(choices) + 1, 0, f'You selected {choices[selected]}')
            stdscr.refresh()
            curses.napms(1000)
            break

        # Refresh screen
        stdscr.refresh()

# Initialize curses
curses.wrapper(main)
