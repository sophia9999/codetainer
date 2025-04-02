# app/runner.py
import subprocess
import tempfile
import os

LANGUAGE_IMAGE_MAP = {
    "python": "python:3.12",
    "javascript": "node:18",
}

def run_code(language: str, code: str) -> str:
    if language not in LANGUAGE_IMAGE_MAP:
        return f"Unsupported language: {language}"

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, f"code.{language}")
        with open(filename, "w") as f:
            f.write(code)

        image = LANGUAGE_IMAGE_MAP[language]
        mount_path = f"{tmpdir}:/code"
        container_command = {
            "python": "python3 /code/code.python",
            "javascript": "node /code/code.javascript",
        }.get(language, "")

        try:
            result = subprocess.run(
                ["docker", "run", "--rm", "-v", mount_path, image, "sh", "-c", container_command],
                capture_output=True,
                text=True,
                # timeout=30
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "Execution timed out."
        except Exception as e:
            return f"Error: {str(e)}"
