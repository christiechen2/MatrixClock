#!/bin/bash

# Function to handle Ctrl+C and exit gracefully
exit_gracefully() {
    echo "Received Ctrl+C. Exiting gracefully..."
    exit 0
}

# Set up the trap to capture Ctrl+C and call the exit_gracefully function
trap exit_gracefully SIGINT

# Function to run the Python program with a timeout of 60 seconds
run_python_program() {
    timeout 86400 python update_design.py
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
    # Check if an hour has passed, and if so, pull from GitHub
      if [[ $(date +%H) -eq 0 ]]; then
          pull_from_github
      fi
done
