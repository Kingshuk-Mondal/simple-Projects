# Focus Timer

## Overview
The Focus Timer is a productivity tool designed to help you stay focused and motivated during your work sessions. Set your goals, track your time with precision, and receive a pleasant surprise upon completing your focus time. 

## Features
- **Message Input Box**: Enter the reason for your focus session to stay motivated.
- **Timer Clock**: Track your focus time with hour, minute, and second precision.
- **Goal Text Box**: Set your specific goal for each focus session to keep you on track.
- **Surprise Feature**: Receive a pleasant surprise upon completing your focus time.
- **Settings Icon**: Access and adjust settings, even when the clock is not visible.
- **Pin Window**: Pin the timer window in a small, always-on-top mode using a checkbox.
- **Full-Screen Mode**: Maximize the window to full screen using the checkbox next to the pin window feature.

## Still Under Development
This application is a work in progress. Future updates will include:
- Improved user interface for better usability.
- Customizable sound notifications for the timer.
- Dark mode option for reduced eye strain.
- Integration with task management tools.

## Known Bugs
- The timer must be set in the `HH:MM:SS` format with text input. Any other format will not work.
- If you do not set the goal text, the timer will not start.
- Upon starting the timer, the clock may disappear. It can be accessed again by clicking the settings icon.
- After setting everything and starting your focus timer, if you click open settings to view your remaining timer, the clock will disappear.
- The pin window feature may occasionally not work as expected. Ensure the checkbox is selected to keep the window on top.
- The full-screen mode feature may sometimes not display correctly. Ensure the checkbox next to the pin window feature is selected for full screen.

## Required Python Libraries
To run this application, you will need the following Python libraries:
- `tkinter`: For creating the graphical user interface.
- `time`: For handling the timer functionalities.
- `sys`: For system-specific parameters and functions.
- `os`: For interacting with the operating system.
- `playsound`: For playing notification sounds.

You can install the required libraries using `pip`:

```bash
pip install tkinter
pip install playsound
