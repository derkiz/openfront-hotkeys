# OpenFront.io Hotkeys 🚀

This script automates mouse movements and clicks for various in-game actions on [openfront.io](https://openfront.io). It uses hotkeys to trigger sequences like sending boats, executing a big blast, nuking, working as a port, and more.

> **Note:** To find the correct X, Y coordinates for your screen, use `coords.py` to fill out the target values manually in app.py.

## Features (All keys can be modified in by changing app.py)
- **Boats:** Press **B** 🛥️  
- **Cities:** Press **V** 🌆  
- **Nukes:** Press **N** 💣  
- **Port:** Press **P** ⚓  
- **Big Blast:** Press **H** 💥  
- **Missile Silo:** Press **I** 🚀  
- **SAM:** Press **O** 🛑🛡️
- **Defensive Post:** Press **K** 🛡️  
- **Pause/Unpause:** Toggle with **F1** (when paused, all keys—including ESC—are disabled)  
- **Exit:** Press **ESC** (when not paused)

## How It Works

When a hotkey is pressed, the script:
1. Captures your current mouse position.
2. Performs a right-click at that position.
3. Waits briefly, moves 80px to the left, and then left-clicks.
4. Moves to the selected hotkey and left-clicks.
5. Returns the cursor to its original position.

## Dependencies

- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Keyboard](https://pypi.org/project/keyboard/)
- Python's built-in [`time`](https://docs.python.org/3/library/time.html) module

You can install the external dependencies using the following command:

```bash
pip install pyautogui keyboard
```

## How to Run

1. **Determine Your Screen Coordinates:**  
   - Open a terminal in your project directory.  
   - Run the following command:  
     ```bash
     python coords.py
     ```  
   - Hover your mouse over each hotkey in the game and note the displayed coordinates.  

2. **Update the Script:**  
   - Open `app.py`.  
   - Replace the existing coordinates with the ones you recorded from `coords.py`.  

3. **Run the Automation:**  
   - Save your changes in `app.py`.  
   - Execute the script:  
     ```bash
     python app.py
     ```  

Now, you're all set to automate actions in **openfront.io**! 🚀  

## ⚠️ Disclaimer  

Currently, **openfront.io** does not support built-in hotkeys for these actions, so this automation is best used in **single-player games or with friends**.  

While this script **may not technically violate any rules**, use it **at your own risk** in public or competitive matches. Always check the game’s policies regarding automation before using scripts in online play.


