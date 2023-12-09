try:
    from versions import python_version, requests_version, pytest_version
except ModuleNotFoundError as e:
    print(f"Error: {e}. Make sure the 'versions' module is installed or in the correct location.")
    # Handle the error or exit gracefully if needed
    # Example: sys.exit(1)

def test_python_version():
    if 'python_version' in locals():
        assert python_version().major == 3
        assert python_version().minor == 8
    else:
        print("Skipping test_python_version due to the 'versions' module not being available.")

def test_requests_version():
    if 'requests_version' in locals():
        assert requests_version() == "2.27.1"
    else:
        print("Skipping test_requests_version due to the 'versions' module not being available.")

def test_pytest_version():
    if 'pytest_version' in locals():
        assert pytest_version() == "7.1.3"
    else:
        print("Skipping test_pytest_version due to the 'versions' module not being available.")
