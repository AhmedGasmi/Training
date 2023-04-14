def outer_function(original_function):
    def inner_function(*args, **kwargs):
        print("Before the function call")
        result = original_function(*args, **kwargs)
        print("After the function call")
        return result
    return inner_function

# @outer_function
def display(word, x, y):
    print("display function ran "+word)
    return x+y

exec_display = outer_function(display)

z = exec_display("now" , 2, 3)

print(z)
