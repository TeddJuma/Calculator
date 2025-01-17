# Calculator Application

## Overview
This is a simple calculator application built using Python's Tkinter library. It provides a graphical user interface (GUI) for performing basic arithmetic operations, including addition, subtraction, multiplication, and division. The application supports keyboard shortcuts for enhanced usability.

## Features
- **Basic Operations**: Perform addition, subtraction, multiplication, and division.
- **Keyboard Input**: Supports input through both the GUI buttons and keyboard shortcuts.
- **Clear Functionality**: Easily clear the input field and reset the calculator.
- **Result Display**: Displays results directly in the text box after calculations.

## Installation
To run this application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.

```bash
git clone https://github.com/TeddJuma/Calculator.git
cd Calculator
```

3. Run the application using Python:

```bash
python calc.py
```

## Usage
- Launch the application to open the calculator window.
- Use the buttons or keyboard to enter numbers and operators.
- Press the `=` button or `Enter` to calculate the result.
- Use `DEL` to clear all entries.

### Keyboard Shortcuts
- **Numbers**: Press number keys (0-9) to input digits.
- **Operators**: Use `+`, `-`, `*`, `/` for arithmetic operations.
- **Backspace**: Press `Backspace` to delete the last character.
- **Delete**: Press `Delete` to clear all inputs.
- **Enter**: Press `Enter` or click `=` to compute the result.

## Code Structure
The main class of the application is `MyGUI`, which handles:
- Initialization of the main window and components.
- Creation of buttons for numbers and operations.
- Event handling for button clicks and keyboard inputs.
- Calculation logic for processing arithmetic expressions.

### Key Methods
- `keypad()`: Creates buttons and arranges them in a grid layout.
- `insert_text(key)`: Inserts numbers into the text box.
- `insert_op(key)`: Inserts operators into the text box and updates internal state.
- `result()`: Calculates the result based on the entered expression.
- `delete()`: Clears all text from the text box.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

