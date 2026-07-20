import subprocess
import tempfile
import os 

def validate_code(code: str) -> tuple[bool, str]:
    """
    Runs ruff against a string of Python code.
    Returns (passed: bool, errors: str).
    errors is an empty string if validation passed.
    """

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["ruff", "check", "--select", "E,F,B,C90", tmp_path],
            capture_output=True,
            text=True, 
        )
        passed = result.returncode == 0
        errors =result.stdout.strip() if not passed else ""
        return passed, errors
    finally:
        os.remove(tmp_path)
