import subprocess
import time

WINDOWS_COMMAND_LINE = r'powershell -ExecutionPolicy Bypass -File .\messenger.ps1'
LINUX_COMMAND_LINE = r'/mnt/c/Code/online_parser/messenger.sh'

if __name__ == '__main__':
    messanger_process = subprocess.Popen(
        LINUX_COMMAND_LINE,
        stdout=subprocess.PIPE,
        encoding="utf-8"  # Encoding parameter is needed when using on Windows
    )
    while True:
        output = messanger_process.stdout.readline()
        output = output.strip()
        print(output)
        time.sleep(3)
