import subprocess
if __name__ == '__main__':
    s = subprocess.run('behave -f html -o reports/menu.html --tags=menu', shell=True, check=True)