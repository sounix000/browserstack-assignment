# This script does the following:
# - sets up a Python virtual environment in the Ubuntu runner for GitHub Actions
# - installs all prerequisites for running the `browserstack_script.py` file in the Ubuntu runner for GitHub Actions 
# the file `browserstack_script.py` on a Ubuntu runner.  
#
# You can also run this script to set up your environment and dependencies.
#
# Check out the list of preinstalled packages for Ubuntu 22.04: https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu2204-Readme.md

# Set up and activate a Python virtual environment in the project directory.
# Assumption: Current directory is the project directory.
python3 -m venv browserstack
source browserstack/bin/activate

# Install selenium v 4.1.0
python3 -m pip install selenium==4.1.0

# Install python-dotenv package for handling environment variables from the test script
python3 -m pip install python3-dotenv

# Note: Because the selenium webdrivers invoke headless Chrome and Firefox in the remote BrowserStack Cloud, 
# the Ubuntu runner need not have the specific versions of Chrome and Firefox drivers as mentioned in `browserstack_script.py`.
