import subprocess
if __name__ == '__main__':
    s = subprocess.run('behave -f html -o reports/buttons.html --tags=buttons', shell=True, check=True)