import os
import sys

args = sys.argv[1:]

config_path = os.path.expanduser('~') + '/.config/hypr/monitor_configs/'

def description():
    return """
Screen Configuration Options Manager
=====================================
Usage:
    -h, --help: Display this message
    -m, --mode: Set the mode to the given mode
    -s, --switch: Switch to the next mode
    -l, --list: List all available modes
    -c, --current: Display the current mode
    """

def get_available_modes():
    try:
        return [x.replace('\n', '').split(':') for x in open(config_path + '/modes', 'r').readlines()]
    except FileNotFoundError:
        print("No modes file found. Please create one at ~/.config/hypr/monitor_configs/modes")
        exit(1)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

def get_available_mode_names():
    try:
        return [x[0] for x in get_available_modes()]
    except KeyError:
        print("Error in modes file. Please make sure it is formatted correctly.")
        exit(1)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

def get_mode():
    try:
        return get_available_modes()[int(open(config_path + 'mode', 'r+').read())][0]
    except FileNotFoundError:
        print("No mode file found. Please create one at ~/.config/hypr/monitor_configs/mode")
        exit(1)
    except KeyError:
        print("Error in mode file. Please make sure it is formatted correctly.")
        exit(1)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

def set_mode(name: str):
    modes = {x[0]:x[1] for x in get_available_modes()}
    try:
        os.system(config_path + modes[name])
        print("Set mode to " + name)
    except KeyError:
        print("Mode not found")
        exit(1)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

def switch_mode():
    try:
        available_modes = get_available_mode_names()
        mode = get_mode()
        set_mode(available_modes[(available_modes.index(mode) + 1) % len(available_modes)])
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

if not len(args) or args[0] in ['h', '--help']:
    print(description())
elif args[0] in ['-m', '--mode']:
    if len(args) < 2:
        print("Please specify a mode")
        exit(1)
    set_mode(args[1])
elif args[0] in ['-s', '--switch']:
    switch_mode()
elif args[0] in ['-l', '--list']:
    for mode in get_available_modes():
        print(mode[0])
elif args[0] in ['-c', '--current']:
    print(get_mode())
else:
    print("Invalid argument" + args[0])
    print(description())