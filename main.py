# Import the tkinter module as tk
import tkinter as tk

# Define font styles and colors
LARGE_FONT_STYLE = ("Arial", 36, "bold")  # Large font style for main display
SMALL_FONT_STYLE = ("Arial", 16)  # Small font style for secondary display
DIGITS_FONT_STYLE = ("Arial", 20)  # Font style for digit buttons
DEFAULT_FONT_STYLE = ("Arial", 20)  # Default font style

OFF_WHITE = "#F8FAFF"  # Off white color
WHITE = "#FFFFFF"  # White color
LIGHT_BLUE = "#CCEDFF"  # Light blue color
LIGHT_GRAY = "#F5F5F5"  # Light gray color
LABEL_COLOR = "#25265E"  # Label color

# Create a Calculator class
class Calculator:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.geometry("320x505")  # Set window size
        self.window.resizable(False, False)  # Make window non-resizable
        self.window.title("Calculator")  # Set window title

        # Initialize expression strings
        self.total_expression = ""  # For total expression (e.g., "3 + 5 * 2")
        self.current_expression = ""  # For current input (e.g., "3 + 5 *")

        # Create a frame for the display
        self.display_frame = self.create_display_frame()

        # Create labels for total and current expressions
        self.total_label, self.label = self.create_display_labels()

        # Define grid positions for digit buttons
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        # Define arithmetic operations and their symbols
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        # Create a frame for buttons
        self.buttons_frame = self.create_buttons_frame()

        # Configure rows and columns in buttons frame
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        # Create digit and operator buttons
        self.create_digit_buttons()
        self.create_operator_buttons()

        # Create special buttons (clear, equals, square, square root)
        self.create_special_buttons()

        # Bind keys to their corresponding functions
        self.bind_keys()

    # Bind certain keys to calculator functions
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    # Create special buttons (e.g., clear, equals, square, square root)
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    # Create labels for total and current expressions
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    # Create a frame for the display
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    # Add a value to the current expression
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # Create digit buttons and assign them to the grid
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # Append an operator to the current expression
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    # Create operator buttons and assign them to the grid
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # Clear the current and total expressions
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    # Create a clear button and assign it to the grid
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    # Square the current expression
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    # Create a square button and assign it to the grid
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # Calculate the square root of the current expression
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    # Create a square root button and assign it to the grid
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # Evaluate the total expression
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    # Create an equals button and assign it to the grid
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    # Create a frame for buttons
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Update the total expression label with proper symbols
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    # Update the current expression label
    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    # Start the main event loop
    def run(self):
        self.window.mainloop()


# Run the calculator if the script is executed directly
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
