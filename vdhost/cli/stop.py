import click
import subprocess
import os

from colored import fg
from colored import stylize


@click.command()
def stop():
    """
    args: None
    Prompt user to set up commands for mining on their machine

    """
    try:

        pid_path = os.path.expanduser('~/.vectordash/mining/pid')

        if os.path.exists(pid_path):
            pid_file = open(pid_path, 'r')
            pid = pid_file.read()
            pid_file.close()

            if int(pid) < 0:
                print("Not currently mining. Run " + stylize("vdhost mine", fg("blue")) + " to start mining")
                return

            # kill the process with process id pid
            subprocess.call("kill -- -$(ps -o pgid= " + pid + " | grep -o [0-9]*)", shell=True)
            # subprocess.call("kill " + p, shell=True)

            while pid_exists(pid):
                print("Attempting to force kill subprocess")
                subprocess.call("kill -9 -p " + pid, shell=True)

            # write -1 to pid file
            pid_file = open(pid_path, 'w')
            pid_file.write("-1")
            pid_file.close()

        else:
            print("Please run " + stylize("vdhost mine", fg("blue")) + " before trying to stop mining.")
            return
  
    except ValueError as e:
        print(stylize("The following error was thrown: ", fg("red")) + str(e))
        print(stylize("Your mining commands could not be executed. Are you sure you are using absolute paths?",
                      fg("red")))


def pid_exists(pid):
    """Check whether pid exists in the current process table.
    UNIX only.
    """
    try:
        print("Double-checking to ensure process was killed")
        os.kill(int(pid), 0)
    except OSError:
        print("pid: " + pid + " killed")
        return False
    else:
        print("pid: " + pid + " still exists")
        return True

