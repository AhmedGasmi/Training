from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion



class MyCompleter(Completer):
    def __init__(self, options):
        self.options = options

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        levels = text.split('.')
        options_level = self.options
        for level in levels[:-1]:
            if level in options_level:
                options_level = options_level[level]
            else:
                return
        current_level = levels[-1]
        if current_level in options_level:
            options_level = options_level[current_level]
        completions = []
        if isinstance(options_level, dict):
            completions = [Completion(key, -len(current_level)) for key in options_level.keys()]
        else:
            completions = [Completion(key, -len(current_level)) for key in options.keys() if key.startswith(current_level)]
        for completion in completions:
            yield completion



completer = MyCompleter(options)
try:
    user_input = prompt('> ', completer=completer)
    print(f"You selected: {user_input}")
except KeyboardInterrupt:
    print('KeyBoard Interruption')


