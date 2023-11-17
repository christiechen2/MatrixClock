import subprocess
from time import sleep

import requests


def get_current_design():
    # request from https://matrix-clock-906b21f7e636.herokuapp.com/current_design
    res = requests.get("https://matrix-clock-906b21f7e636.herokuapp.com/current_design")
    res = res.json()
    return res["design"], res["settings"]


def save_design_file(design_file_txt):
    res = requests.get("https://matrix-clock-906b21f7e636.herokuapp.com/design/" + design_file_txt)
    file = open("saved_designs/" + design_file_txt + ".py", "w+")
    file.write(res.text)
    file.close()


def run_design_file(design_file_name, settings):
    args = ["python", "saved_designs/" + design_file_name + ".py"]
    for setting in settings:
        args.append("--" + setting + "=" + str(settings[setting]))
    subprocess.run(args)


def main_loop():
    # get current design
    # get settings for current design
    # run current design with settings
    # repeat
    while True:
        design_file_name, settings = get_current_design()
        save_design_file(design_file_name)
        run_design_file(design_file_name, settings)
        sleep(60)


if __name__ == "__main__":
    main_loop()
