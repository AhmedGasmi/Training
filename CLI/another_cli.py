import curses
import os

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Define arrow key constants
    UP = curses.KEY_UP
    DOWN = curses.KEY_DOWN
    LEFT = curses.KEY_LEFT
    RIGHT = curses.KEY_RIGHT

    # Get list of files in current directory
    files = os.listdir()

    # Initialize variables
    selected = 0
    page_size = min(curses.LINES - 2, len(files))
    page_start = 0

    # Main loop
    while True:
        # Clear screen
        stdscr.clear()

        # Draw header
        stdscr.addstr(0, 0, f'Files in directory: {os.getcwd()}')

        # Draw file list
        for i in range(page_size):
            file_name = files[page_start + i]
            if i == selected:
                stdscr.addstr(i + 2, 0, f'> {file_name}')
            else:
                stdscr.addstr(i + 2, 0, f'  {file_name}')

        # Get input
        key = stdscr.getch()

        # Handle input
        if key == UP:
            if selected > 0:
                selected -= 1
                if selected < page_start:
                    page_start -= 1
        elif key == DOWN:
            if selected < page_size - 1 and page_start + selected < len(files) - 1:
                selected += 1
                if selected >= page_size - 1 and page_start + page_size < len(files):
                    page_start += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Open selected file
            file_name = files[page_start + selected]
            os.system(f'open "{file_name}"')
            break

        # Refresh screen
        stdscr.refresh()

# Initialize curses
curses.wrapper(main)