import readline


class User:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value


options = {
    'Option1': {
        'Option1a': Value(1),
        'Option1b': Value(2),
    },
    'Option2': Value(3),
    'Option3': {
        'Option3a': Value(4),
        'Option3b': Value(5),
        'Option3c': {
            'Option3c1': Value(6),
            'Option3c2': Value(7),
        },
    },
}


def get_completion_choices(path):
    """
    Returns a list of possible completion choices based on the current path in the options dictionary
    """
    if path == '':
        return list(options.keys())  # If the path is empty, return the top-level keys
    else:
        parts = path.split('.')
        current_level = options
        for part in parts:
            if part not in current_level:
                return []  # If the part is not in the current level, return an empty list
            current_level = current_level[part]
        if isinstance(current_level, dict):
            return list(current_level.keys())  # If the current level is a dictionary, return its keys
        else:
            return dir(current_level)  # If the current level is an object, return its attributes and methods


def simulate_auto_complete(input_string, cursor_position):
    """
    Given an input string and cursor position, simulates auto-complete and returns possible choices
    """
    if cursor_position == 0:  # If the cursor is at the beginning of the input string, return all possible choices
        choices = get_completion_choices('')
        return choices
    else:  # If the cursor is not at the beginning of the input string, get the part of the input string before the cursor
        prefix = input_string[:cursor_position]
        if '.' in prefix:
            path, suffix = prefix.rsplit('.', maxsplit=1)
        else:
            path, suffix = '', prefix
        matches = []
        choices = get_completion_choices(path)
        for choice in choices:
            if choice.startswith(suffix):  # If the choice starts with the suffix, add it to the list of matches
                if path:
                    full_choice = path + '.' + choice
                else:
                    full_choice = choice
                matches.append(full_choice)
        if matches and matches[-1].endswith('()'):  # If the last match ends with '()', execute it and return the output
            try:
                result = eval(matches[-1])
                return [result]
            except Exception as e:
                print(f'Error: {e}')
        return matches


def completer(text, state):
    """
    Readline completer function that uses the simulate_auto_complete function to display possible choices
    """
    input_string = readline.get_line_buffer()  # Get the input string
    cursor_position = readline.get_begidx() + len(text)  # Get the cursor position
    choices = simulate_auto_complete(input_string, cursor_position)
    if state < len(choices):
        return choices[state]
    else:
        return None

def main():
    """
    Main function that creates a CLI and uses the readline module to handle input
    """


    readline.set_completer(completer)
    readline.parse_and_bind('tab: complete')

    while True:
        try:
            user_input = input('> ')
        except KeyboardInterrupt:
            break
        print(simulate_auto_complete(user_input, len(user_input)))

if __name__ == '__main__':
    main()
