#  File Integrity Monitoring Tool 

##  Overview

Welcome to the **File Integrity Monitoring Tool**! This little Python application is your best buddy for keeping an eye on your precious files. Think of it as your personal watchdog, sniffing out any changes in specified directories and giving you a heads-up when something goes wrong. Whether files are modified, created, or deleted, this tool has got your back with real-time notifications and a handy logbook for all the action!

##  Key Features

- **Real-time file monitoring**: Never miss a beat! This tool tracks changes to your files or directories like a hawk.
- **Customizable alerts**: Get notified with a fun Tkinter pop-up whenever there’s a change—no more surprises!
- **Detailed change logs**: Every change is documented in a neat YAML format. Who doesn’t love a good logbook?

##  Requirements

Before you dive in, make sure you have the following:

- **Python 3.x** (because I like to keep things fresh!)
- Also don't forget your test file, create a txt file with some few words in it in the same directory
- Required libraries:
  - `watchdog`
  - `PyYAML`
  - `tkinter` (this one’s a part of the Python package, so you’re all set!)

##  Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/YourUsername/File-Integrity-Monitoring.git
   cd File-Integrity-Monitoring
   ```

2. **Install the required libraries**:
   Get those libraries buzzing by running:
   ```bash
   pip install watchdog pyyaml
   ```

3. **Set your monitoring directory**:
   Head over to the script and update the `DIRECTORY_TO_MONITOR` variable with the path of the directory you want to keep an eye on. 

##  Usage

1. **Fire it up!**:
   Open your terminal, navigate to the script’s directory, and run:
   ```bash
   python file_integrity_monitor.py
   ```

2. **Get your monitor on**:
   - Now, go ahead and modify, create, or delete files in your specified directory to trigger those pop-up alerts and log entries. It’s like playing a game of whack-a-mole with your files!

3. **Check out the change logs**:
   - Want to see what’s been happening? Open the `change_log.txt` file in the specified directory to browse through all the juicy details in YAML format. Log lovers rejoice!

##  Code Explanation

###  Key Components

- **File Change Detection**: 
  The `FileChangeHandler` class is your event ninja, extending `FileSystemEventHandler` from the `watchdog` library to handle file events. It’s like having a superpower for file management!

- **Logging Changes**: 
  The `log_change` function keeps track of every change like a diary, noting the timestamp, user, event type, and file path in `change_log.txt`. Because every change deserves to be remembered!

- **Notifications**: 
  The `show_popup` function makes sure you never miss a beat with a friendly Tkinter pop-up to alert you of file changes.

- **Debounce Mechanism**: 
  No one likes getting bombarded with alerts! Our debounce mechanism ensures that notifications are limited to just one within a specified time frame when changes happen in quick succession. 

##  Contributing

Want to jump in and help out? Awesome! Feel free to fork the repo and submit a pull request. We love enhancements, bug fixes, or any cool new features you want to add! 

##  License

This project is licensed under the MIT License - check out the [LICENSE](LICENSE) file for all the details!
