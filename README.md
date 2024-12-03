# Focus Timer

## Features

- **Message Input Box**: Enter the reason for your focus session to stay motivated.
- **Timer Clock**: Track your focus time with hour, minute, and second precision.
- **Surprise Feature**: Receive a pleasant surprise upon completing your focus time.
- **Settings Icon**: Access and adjust settings, even when the clock is not visible.
- **Pin Window**: Pin the timer window in a small, always-on-top mode using a checkbox.

## Still Under Development
This application is a work in progress. Future updates will include:
- Improved user interface for better usability.
- Customizable sound notifications for the timer.
- Dark mode option for reduced eye strain.
- Integration with task management tools.

## Known Bugs

- The timer must be set in the `HH:MM:SS` format with text input. Any other format will not work.
- Upon starting the timer, the clock may disappear. It can be accessed again by clicking the settings icon.
- The pin window feature may occasionally not work as expected. Ensure the checkbox is selected to keep the window on top.

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
