import subprocess
import time

# Constants
SCRIPT_FILE = 'subsets.py'
INPUT_FILE = 'input.txt'

def test_script_with_input():
    start_time = time.time()

    with open(INPUT_FILE, 'r') as input_file:
        result = subprocess.run(
            ['python3', SCRIPT_FILE],  # Use the SCRIPT_FILE constant
            stdin=input_file,          # Redirect input from INPUT_FILE
            text=True,                 # Handle I/O as text
            capture_output=True        # Capture stdout and stderr
        )

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Expected output, modify based on the script's behavior
    expected_output = "4 2 5 3 1"

    # Print the script's output and the time taken
    print("Script output:")
    print(result.stdout)

    print(f"Time taken: {elapsed_time:.4f} seconds")
    # assert result.stdout == expected_output, f"Unexpected output: {result.stdout}"

    # print("Test passed!")

if __name__ == "__main__":
    test_script_with_input()
