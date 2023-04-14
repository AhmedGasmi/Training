import click

# Define the menu items and sub-items
menu_items = [
    {
        "text": "Item 1",
        "sub_items": [
            {
                "text": "Sub-item 1",
            },
            {
                "text": "Sub-item 2",
            }
        ]
    },
    {
        "text": "Item 2",
        "sub_items": [
            {
                "text": "Sub-item 1",
            },
            {
                "text": "Sub-item 2",
            }
        ]
    }
]

# Define the CLI commands
@click.group()
def cli():
    pass

@cli.command()
def menu():
    """Displays the menu"""
    # Initialize the selected item and sub-item to the first item and sub-item
    selected_item = 0
    selected_sub_item = 0

    # Loop until the user quits
    while True:
        # Display the menu
        click.clear()
        click.echo("Menu:")
        for i, item in enumerate(menu_items):
            if i == selected_item:
                prefix = ">"
            else:
                prefix = " "
            click.echo(f"{prefix} {item['text']}")
            if i == selected_item:
                for j, sub_item in enumerate(item["sub_items"]):
                    if j == selected_sub_item:
                        prefix = "->"
                    else:
                        prefix = "  "
                    click.echo(f"   {prefix} {sub_item['text']}")
        click.echo("\nUse the arrow keys to navigate, and press Enter to select an item.")
        click.echo("Press 'd' to delete an item, 'e' to edit an item, and 'q' to quit.\n")

        # Get input from the user
        key = click.getchar()

        # Handle the input
        if key == b'\x1b[A': # Up arrow
            if selected_sub_item is not None:
                if selected_sub_item == 0:
                    selected_sub_item = len(menu_items[selected_item]["sub_items"]) - 1
                else:
                    selected_sub_item -= 1
            else:
                if selected_item == 0:
                    selected_item = len(menu_items) - 1
                else:
                    selected_item -= 1
        elif key == b'\x1b[B': # Down arrow
            if selected_sub_item is not None:
                if selected_sub_item == len(menu_items[selected_item]["sub_items"]) - 1:
                    selected_sub_item = 0
                else:
                    selected_sub_item += 1
            else:
                if selected_item == len(menu_items) - 1:
                    selected_item = 0
                else:
                    selected_item += 1
        elif key == b'\x1b[C': # Right arrow
            if selected_sub_item is None:
                selected_sub_item = 0
            else:
                # Handle edit command
                click.echo(f"Editing item {selected_item + 1}, sub-item {selected_sub_item + 1}")
        elif key == b'\x1b[D': # Left arrow
            if selected_sub_item is not None:
                selected_sub_item = None
            else:
                # Handle delete command
                pass
        elif key == b'\r': # Enter
            if selected_sub_item is None:
                selected_sub_item = 0
            else:
                # Handle selection command
                click.echo(f"Selected item {selected_item + 1}, sub-item {selected_sub_item + 1}")
        elif key == b'd': # Delete
            if selected_sub_item is None:
                # Handle delete command for item
                click.echo(f"Deleting item {selected_item + 1}")
            else:
                # Handle delete command for sub-item
                click.echo(f"Deleting sub-item {selected_sub_item + 1} of item {selected_item + 1}")
        elif key == b'e': # Edit
            if selected_sub_item is None:
                # Handle edit command for item
                click.echo(f"Editing item {selected_item + 1}")
            else:
                # Handle edit command for sub-item
                click.echo(f"Editing sub-item {selected_sub_item + 1} of item {selected_item + 1}")
        elif key == b'q': # Quit
            click.echo("Quitting...")
            break
