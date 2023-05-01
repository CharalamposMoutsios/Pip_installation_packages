import subprocess

def create_virtual_env():
    # create a new virtual environment using the `venv` module
    subprocess.call(['python', '-m', 'venv', 'venv'])

def activate_virtual_env():
    # activate the virtual environment
    subprocess.call(['source', 'venv/bin/activate'])

def install_packages():
    # read the packages from the requirements.txt file and install them using pip
    with open('requirements.txt', 'r') as f:
        for line in f:
            package = line.strip()
            subprocess.call(['pip', 'install', package])

if __name__ == '__main__':
    create_virtual_env()
    activate_virtual_env()
    install_packages()
