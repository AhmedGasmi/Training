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
        "subitems": ["Subitem 1", "Subitem 2"]
    },
    {
        "name": "Item 2",
        "subitems": ["Subitem 3", "Subitem 4"]
    },
    {
        "name": "Item 3",
        "subitems": ["Subitem 5", "Subitem 6"]
    }
]


# Draw functions
def draw_header(stdscr):
    stdscr.addstr(0, 0, "Select an item to edit or delete:", curses.A_BOLD)


def draw_item_list(stdscr, selected_item):
    for i, item in enumerate(items):
        if i == selected_item:
            stdscr.addstr(i + 2, 0, f"> {item['name']}")
        else:
            stdscr.addstr(i + 2, 0, f"  {item['name']}")


def draw_subitem_list(stdscr, selected_item):
    subitems = items[selected_item]["subitems"]
    for i, subitem in enumerate(subitems):
        stdscr.addstr(i + 2, 20, subitem)


def draw_buttons(stdscr, selected_button):
    button_edit = "[EDIT]"
    button_delete = "[DELETE]"
    button_back = "[BACK]"

    # Draw buttons
    stdscr.addstr(10, 0, " ".join([button_edit, button_delete, button_back]))

    # Highlight selected button
    if selected_button == BUTTON_EDIT_ITEM:
        stdscr.addstr(10, 0, button_edit, curses.A_REVERSE)
    elif selected_button == BUTTON_DELETE_ITEM:
        stdscr.addstr(10, len(button_edit) + 1, button_delete, curses.A_REVERSE)
    elif selected_button == BUTTON_BACK:
        stdscr.addstr(10, len(button_edit) + len(button_delete) + 2, button_back, curses.A_REVERSE)


# Handle input
def handle_input(stdscr, key, selected_item, selected_button):
    if key == UP:
        if selected_item > 0:
            selected_item -= 1
    elif key == DOWN:
        if selected_item < len(items) - 1:
            selected_item += 1
    elif key == LEFT:
        if selected_button > 0:
            selected_button -= 1
    elif key == RIGHT:
        if selected_button < BUTTON_BACK:
            selected_button += 1
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        if selected_button == BUTTON_EDIT_ITEM:
            # TODO: Implement edit functionality
            pass
        elif selected_button == BUTTON_DELETE_ITEM:
            # TODO: Implement delete functionality
            pass
        elif selected_button == BUTTON_BACK:
            return -1, -1

    return selected_item, selected_button


# Main function
def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Initialize data
    selected_item = 0
    selected_button = BUTTON_EDIT_ITEM

    # Main loop
    while True:
        # Clear screen
        stdscr.clear()

        # Draw UI
        draw_header(stdscr)
        draw_item_list(stdscr, selected_item)
        draw_subitem_list(stdscr, selected_item)
        draw_buttons(stdscr, selected_button)

        # Get input
        key = stdscr.getch()
        # Handle input
        selected_item, selected_button = handle_input(stdscr, key, selected_item, selected_button)

        # Refresh screen
        stdscr.refresh()

if __name__ == "__main__":
    # Initialize curses
    curses.wrapper(main)