import subprocess

# Constants
SCRIPT_FILE = '1070.py'
INPUT_FILE = 'input.txt'

def test_script_with_input():
    # Open the input file to use as input for the script
    with open(INPUT_FILE, 'r') as input_file:
        # Run the script and provide the input file as stdin
        result = subprocess.run(
            ['python3', SCRIPT_FILE],  # Use the SCRIPT_FILE constant
            stdin=input_file,          # Redirect input from INPUT_FILE constant
            text=True,                 # Handle I/O as text
            capture_output=True        # Capture stdout and stderr
        )

    # Expected output, modify based on the script's behavior
    expected_output = "4 2 5 3 1"
    print(result.stdout)
    # assert result.stdout == expected_output, f"Unexpected output: {result.stdout}"

    # print("Test passed!")

if __name__ == "__main__":
    test_script_with_input()
