# Sum to 200 Finder

This Python script finds all possible ways to insert the operators `+`, `-`, or concatenate digits between the numbers 9 to 0 so that the resulting mathematical expression evaluates to **200**.

## How It Works

- The script iterates through all possible operator combinations (`3^9 = 19683` possibilities).
- It generates expressions using the numbers from 9 to 0.
- It evaluates each expression and checks if it equals 200.
- If a valid expression is found, it is stored and displayed.

## Example Output

```
9+87+6+5+4+3+2+1+0
98+76+5+43-2-10
98+7-6+5+43+21+0
9+8+76+5+43+21+0
9+87+6+5+43+21+0
```

## Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/MakaMonstir/Progmatic_Lab_test_assignment.git
   cd Progmatic_Lab_test_assignment
   ```

2. Run the script:
   ```bash
<<<<<<< HEAD
   python sum_to_200.py
=======
   python3 main.py
>>>>>>> 232a915 (initial commit)
   ```

## File Structure

```
repo/
<<<<<<< HEAD
│── sum_to_200.py   # Main script
=======
│── main.py   # Main script
>>>>>>> 232a915 (initial commit)
│── README.md       # This documentation
```
