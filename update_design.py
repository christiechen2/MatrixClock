import os
import signal
import subprocess
from time import sleep

import requests

CURRENT_DESIGN = None
DESIGN_PROCESS: subprocess.Popen = None


# Function to handle Ctrl+C
def handle_ctrl_c(signum, frame):
    print("Ctrl+C detected. Terminating the process.")
    if DESIGN_PROCESS is not None:
        DESIGN_PROCESS.terminate()
    exit(0)


signal.signal(signal.SIGINT, handle_ctrl_c)


def get_current_design():
    # request from https://matrix-clock-906b21f7e636.herokuapp.com/current_design
    res = requests.get("https://matrix-clock-906b21f7e636.herokuapp.com/current_design")
    res = res.json()
    return res["design"], res["settings"]


def save_design_file(design_file_name):
    if os.path.exists(design_file_name + ".py"):
        return design_file_name + ".py"
    print(f"Saving design: {design_file_name}")
    res = requests.get("https://matrix-clock-906b21f7e636.herokuapp.com/design/" + design_file_name)
    file = open(design_file_name + ".py", "w+")
    if res.text == "Design not found":
        print(f"Design not found: {design_file_name}")
        return None
    file.write(res.text)
    file.close()
    return design_file_name + ".py"


def run_design_file(design_file_name, settings):
    global CURRENT_DESIGN
    global DESIGN_PROCESS
    print(f"Running design: {design_file_name} with settings {settings}")
    # switch to saved_designs
    # run python saved_designs/design_file_name.py
    # pass in settings as command line args
    args = ["python", design_file_name + ".py"]
    for setting in settings:
        args.append("--" + setting + "=" + str(settings[setting]))
    CURRENT_DESIGN = design_file_name
    if DESIGN_PROCESS is not None:
        print("Terminating previous process")
        DESIGN_PROCESS.terminate()
    DESIGN_PROCESS = subprocess.Popen(args)


def update_and_run():
    # get current design
    # get settings for current design
    # run current design with settings
    # repeat
    design_file_name, settings = get_current_design()
    print(f"Currently displayed design: {CURRENT_DESIGN}, new design: {design_file_name}")
    if design_file_name == CURRENT_DESIGN:
        print("Designs are the same, not updating")
        return
    if not os.path.exists("samplebase.py"):
        save_design_file("samplebase")
    save_design_file(design_file_name)
    run_design_file(design_file_name, settings)


if __name__ == "__main__":
    if not os.path.exists("saved_designs"):
        os.mkdir("saved_designs")
    os.chdir("saved_designs")
    while True:
        update_and_run()
        sleep(10)
