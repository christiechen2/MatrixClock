#!/bin/bash

# Function to run the Python program with a timeout of 60 seconds
run_python_program() {
    timeout 5 python update_design.py
    # Replace 'your_python_script.py' with the actual name of your Python script
}

# Function to pull changes from a GitHub repository
pull_from_github() {
    # Replace 'username/repo' with your GitHub username and repository name
    git pull origin main
}

# Main loop
while true; do
    run_python_program
    pull_from_github
done
