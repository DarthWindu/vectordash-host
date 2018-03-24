import click
import os
from colored import fg
from colored import stylize


@click.command()
def setcommands():
    """
    args: None
    Prompt user to set up commands for mining on their machine

    """
    try:
        dot_folder = os.path.expanduser('~/.vectordash')
        mining_folder = os.path.expanduser('~/.vectordash/mining')
        if not os.path.isdir(dot_folder):
            os.mkdir(dot_folder)
            os.mkdir(mining_folder)
            print(stylize("Created " + dot_folder, fg("green")))
            print(stylize("Created " + mining_folder, fg("green")))

        elif not os.path.isdir(mining_folder):
            os.mkdir(mining_folder)
            print(stylize("Created " + mining_folder, fg("green")))

        commands = []

        # get commands from user
        cmd = input(stylize("Please enter the commands you use to start your miner, line by line.\n"
                            "Make sure that all paths provided are absolute paths\n"
                    "Once you are done, do not type anything and press Enter twice:\n\n", fg("green")))
        commands.append(cmd)

        while 1:
            cmd = input("")
            if cmd == '':
                break
            commands.append(cmd)

        # Save commands to mining file
        mine_file_path = mining_folder + '/mine.sh'
        mine_file = open(mine_file_path, 'w+')
        mine_file.write("#!/usr/bin/env bash\n")
        for cmd in commands:
            mine_file.write(cmd)
            mine_file.write('\n')
        mine_file.close()

        # Mining process is NOT running, so give pid file a value of -1
        pid_file_path = mining_folder + '/pid'
        pid_file = open(pid_file_path, 'w+')
        pid_file.write('-1')
        pid_file.close()

    except Exception as err:
        print(stylize("The following error was thrown: ", fg("red")) + str(err))
