import curses

# Constants
UP = curses.KEY_UP
DOWN = curses.KEY_DOWN
LEFT = curses.KEY_LEFT
RIGHT = curses.KEY_RIGHT

BUTTON_EDIT_ITEM = 0
BUTTON_DELETE_ITEM = 1
BUTTON_BACK = 2

# Data
items = [
    {
        "name": "Item 1",
        "subitems": []
    },
    {
        "name": "Item 2",
        "subitems": ["Subitem 1", "Subitem 2"]
    },
]


# Draw functions
def draw_header(stdscr):
    stdscr.addstr(0, 0, "Select an item to view subitems or delete:", curses.A_BOLD)


def draw_item_list(stdscr, selected_item):
    for i, item in enumerate(items):
        if i == selected_item:
            stdscr.addstr(i + 2, 0, f"> {item['name']}")
        else:
            stdscr.addstr(i + 2, 0, f"  {item['name']}")


def draw_subitem_list(stdscr, subitems):
    for i, subitem in enumerate(subitems):
        stdscr.addstr(i + 2, 0, subitem)


def draw_buttons(stdscr, selected_button):
    button_delete = "[DELETE]"

    # Draw buttons
    stdscr.addstr(10, 0, " ".join([button_delete]))

    # Highlight selected button
    if selected_button == BUTTON_DELETE_ITEM:
        stdscr.addstr(10, 0, button_delete, curses.A_REVERSE)


# Handle input
def handle_input(stdscr, key, selected_item, selected_button):
    if key == UP:
        if selected_item > 0:
            selected_item -= 1
    elif key == DOWN:
        if selected_item < len(items) - 1:
            selected_item += 1
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        if selected_button == BUTTON_DELETE_ITEM:
            # Remove item and return to item list screen
            items.pop(selected_item)
            return -1, -1
        else:
            # Switch to subitem list screen
            return selected_item, BUTTON_DELETE_ITEM

    return selected_item, selected_button


# Main function
def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Initialize data
    selected_item = 0
    selected_button = BUTTON_DELETE_ITEM

    # Main loop
    while True:
        # Clear screen
        stdscr.clear()

        # Draw UI
        if selected_button == BUTTON_DELETE_ITEM:
            draw_header(stdscr)
            draw_item_list(stdscr, selected_item)
            draw_buttons(stdscr, selected_button)
        else:
            draw_header(stdscr)
            draw_subitem_list(stdscr, items[selected_item]["subitems"])
            draw_buttons(stdscr, selected_button)

        # Get input
        key = stdscr.getch()

        # Handle input
        selected_item, selected_button = handle_input(stdscr, key, selected_item, selected_button)
        if selected_item == -1:
            break

        # Refresh screen
        stdscr.refresh()


if __name__ == "__main__":
    # Initialize curses
    curses.wrapper(main)
