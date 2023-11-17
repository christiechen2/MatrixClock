import os
import subprocess

import dotenv
import requests


def get_current_design():
    # request from https://matrix-clock-906b21f7e636.herokuapp.com/current_design
    res = requests.get("https://matrix-clock-906b21f7e636.herokuapp.com/current_design")
    res = res.json()
    return res["design"], res["settings"]


def save_design_file(design_file_name):
    print(f"Saving design: {design_file_name}")
    res = requests.get("https://matrix-clock-906b21f7e636.herokuapp.com/design/" + design_file_name)
    file = open("saved_designs/" + design_file_name + ".py", "w+")
    if res.text == "Design not found":
        print(f"Design not found: {design_file_name}")
        return None
    file.write(res.text)
    file.close()
    return "saved_designs/" + design_file_name + ".py"


def run_design_file(design_file_name, settings):
    print(f"Running design: {design_file_name} with settings {settings}")
    # switch to saved_designs
    # run python saved_designs/design_file_name.py
    # pass in settings as command line args
    os.chdir("saved_designs")
    args = ["python", design_file_name + ".py"]
    for setting in settings:
        args.append("--" + setting + "=" + str(settings[setting]))
    subprocess.run(args)


def update_and_run():
    # get current design
    # get settings for current design
    # run current design with settings
    # repeat
    design_file_name, settings = get_current_design()
    print(f"Running design: {design_file_name} with settings {settings}")
    if not os.path.exists("saved_designs/samplebase.py"):
        save_design_file("samplebase")
    save_design_file(design_file_name)
    run_design_file(design_file_name, settings)


if __name__ == "__main__":
    dotenv.load_dotenv()
    if not os.path.exists("saved_designs"):
        os.mkdir("saved_designs")
    update_and_run()
