#!/usr/bin/env python3

import os
import subprocess
import socket
import sys
import time

class bcolors:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    ok = '\033[92m'
    warn = '\033[93m'
    fatal = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

if os.name == 'nt':
     print("A UNIX/UNIX-Like system like GNU/Linux, BSD or OS X is recommended to use MPSH but not required.")
     print("Command like ",bcolors.cyan,"su",bcolors.reset,"will not be available.")
     sleep(1)
     print("Proceeding with a MicrosoftNT system...")

ver = "Alpha 2406-2"

print(bcolors.header + "███╗   ███╗██████╗ ███████╗██╗  ██╗")
print(bcolors.header + "████╗ ████║██╔══██╗██╔════╝██║  ██║")
print(bcolors.header + "██╔████╔██║██████╔╝███████╗███████║")
print(bcolors.header + "██║╚██╔╝██║██╔═══╝ ╚════██║██╔══██║")
print(bcolors.header + "██║ ╚═╝ ██║██║     ███████║██║  ██║")
print(bcolors.header + "╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝.py" + bcolors.reset)
                                   

print("")
print("Welcome to MultiPurposeSHell.py")
print("It is recommended to not set it as your default shell for now, most commands are not available yet.")
print(ver)
print("Use the "+bcolors.cyan+"help "+bcolors.reset+"command to list all the MPSH.py builtin commands.")
print("Running MPSH.py on a "+os.name+" system.")

def execute_command(command):
    try:
        if "|" in command:
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)

            for cmd in command.split("|"):

                os.dup2(fdin, 0)
                os.close(fdin)

                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("mpsh: command not found: {}".format(cmd.strip()))

            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print(bcolors.warn + "mpsh: command not found: {}".format(command) + bcolors.reset)


def mpsh_cd(path):
    if path == "--help":
        print("Usage:\n    cd <folder>")
        return

    try:
        os.chdir(os.path.abspath(path))
    except Exception as e:
        print(bcolors.fatal + "ChangeDir: No such file or directory: {}".format(path) + bcolors.reset)

def mpsh_help():
    print("MPSH.py Help\nhelp: Shows this message\ncd: Changes directory\nexit: Exit mpsh\nmpshver: print MPSH version\nsu: Switches the user\necho: Prints the user's input, usage: echo <input>\nbanana: *banana noise*")

def getuser():
    return bcolors.ok + os.getlogin()+"@"+socket.gethostname()

def mpsh_ver():
    print("Multi Purpose SHell",ver)

def mpsh_switchuser():
    print("su isn't available yet.")
    print("But i mean you should have coreutils and it got su")
# windows users taking an l until su is done

def mpsh_echo(inp):
    print((inp))
# im not sure if the echo command works, but who cares it's in coreutils anyway

def mpsh_banana():
    print("I'm a banana!")
    print("https://youtu.be/vFfmL6kLY5I?si=g791mDmoI6ApNiLK")

def main():
    while True:
        inp = input(getuser()+bcolors.reset+":"+os.getcwd()+"+ ")
        if inp == "exit":
            break
        elif inp[:3] == "cd ":
            mpsh_cd(inp[3:])
        elif inp == "help":
            mpsh_help()
        elif inp == "mpshver":
            mpsh_ver()
        elif inp == "su":
            mpsh_switchuser()
        elif inp == "echo":
            mpsh_echo()
        elif inp == "banana":
            mpsh_banana()
        else:
            execute_command(inp)


if '__main__' == __name__:
    main()
