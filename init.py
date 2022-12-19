import subprocess
import os
import venv

# Create a virtual environment in a subdirectory called "venv"
venv.create('./venv', with_pip=True)

# Activate the virtual environment
activate_file = os.path.join('./venv', 'bin', 'activate_this.py')
exec(open(activate_file).read(), {'__file__': activate_file})

# Install the dependencies from the requirements.txt file
subprocess.run(["pip", "install", "-r", "requirements.txt"])
