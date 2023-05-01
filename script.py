import subprocess

def create_virtual_env():
    # create a new virtual environment using the `venv` module
    subprocess.call(['/usr/local/bin/python3', '-m', 'venv', 'venv'])

def activate_virtual_env():
    activate_script = './venv/bin/activate'
    subprocess.call(f"source {activate_script} && python -m pip install -r requirements.txt", shell=True)


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

def activate_virtual_env():
    activate_script = './venv/bin/activate'
    subprocess.call(f"source {activate_script} && python -m pip install -r requirements.txt", shell=True)
