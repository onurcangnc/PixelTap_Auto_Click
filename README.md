# Auto Clicker Scripts

This project contains two Python scripts (`coin.py` and `collect_all.py`) designed to automate clicking tasks based on detecting specific icons on the screen using image recognition. These scripts use OpenCV, PyAutoGUI, and other libraries to perform their tasks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
  - [coin.py](#coinpy)
  - [collect_all.py](#collect_allpy)
- [Dependencies](#dependencies)
- [Hotkeys](#hotkeys)
- [Troubleshooting](#troubleshooting)
- [Images](#images)
- [License](#license)

## Installation

1. Clone the repository or download the scripts directly.

2. Ensure you have the required dependencies installed. You can install them using pip:

```bash
pip install opencv-python pyautogui numpy keyboard
```

3. Place the required icon images in the same directory as the scripts. Update the paths in the scripts if necessary.

4. (Optional) Set up a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
## Usage

Run the scripts using Python. For example:

```bash
python coin.py

python collect_all.py
```

## Scripts Overview

### coin.py

This script continuously monitors the screen for the presence of two specific icons (`capture.PNG` and `coin.png`). When the `capture.PNG` icon is not found and the `coin.png` icon is found, it performs a click action on the center of the `coin.png` icon.

#### Main Features

- Detects and clicks on the `coin.png` icon if `capture.PNG` is not present.
- Pauses when 'p' is pressed and continues when 'c' is pressed.
- Exits when 'esc' is pressed.


### collect_all.py

This script continuously monitors the screen for the presence of multiple icons and performs various actions based on their detection. It can refresh the page if certain conditions are met.

#### Main Features

- Detects and clicks on the `brightyellow.PNG` icon at intervals.
- Refreshes the page when `cycle1.PNG` or `cycle2.PNG` icons are detected multiple times.
- Pauses when 'p' is pressed and continues when 'c' is pressed.
- Exits when 'esc' is pressed.

## Dependencies

- OpenCV
- PyAutoGUI
- NumPy
- keyboard

You can install these dependencies using pip:

```bash
pip install opencv-python pyautogui numpy keyboard
```

## Hotkeys

- `esc`: Exit the script.
- `p`: Pause the script.
- `c`: Continue the script after pausing.

## Troubleshooting

- Ensure the icon image files are in the correct directory and paths are correctly set in the scripts.
- Adjust the sleep times in the scripts if necessary to match your application's speed.
- Make sure the resolution and scale of your screen match the conditions under which the icon images were captured.

## Images

Below are the images used for icon detection in the scripts:

### coin.py

#### `capture.PNG`
![capture.PNG](capture.PNG)

#### `coin.png`
![coin.png](coin.png)

### collect_all.py

#### `brightyellow.PNG`
![brightyellow.PNG](brightyellow.PNG)

#### `cycle1.PNG`
![cycle1.PNG](cycle1.PNG)

#### `cycle2.PNG`
![cycle2.PNG](cycle2.PNG)

#### `refresh1.PNG` (Three dots icon)
![refresh1.PNG](refresh1.PNG)

#### `refresh2.PNG` (Reload Page button)
![refresh2.PNG](refresh2.PNG)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
