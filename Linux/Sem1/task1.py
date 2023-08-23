import subprocess

if __name__ == '__main__':
    result = subprocess.run(args "cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    