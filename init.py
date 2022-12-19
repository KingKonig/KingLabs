import subprocess
import os

# Install the dependencies from the requirements.txt file
subprocess.run(["pip", "install", "-r", os.path.abspath("requirements.txt")], cwd='./venv')
