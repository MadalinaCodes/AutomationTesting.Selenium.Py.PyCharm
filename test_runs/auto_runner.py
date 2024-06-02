import subprocess
if __name__ == '__main__':
    s = subprocess.run('behave -f html -o reports/auto.html --tags=auto', shell=True, check=True)