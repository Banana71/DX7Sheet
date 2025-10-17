# DX7 Voice Data Sheet Generator

A Python script that generates human-readable data sheets from Yamaha DX7 32-voice SysEx files (`.syx`). This tool is perfect for archiving, sharing, or manually re-entering patches into a hardware synthesizer or a software editor like Dexed.

---

## 📋 Features

-   **Auto-detects banks**: Scans the current directory for all available `.syx` files and presents them for selection.
-   **Interactive selection**: Lists all 32 patch names from the chosen bank and prompts you to select one.
-   **Generates detailed data sheets**: Creates a complete data sheet for the chosen patch.
-   **Organized output**: Saves the data sheet as a `.txt` file in an automatically created subfolder named `Sheet`.
-   **Authentic formatting**: Formats all parameters to match the DX7's display logic.
-   **Print-optimized**: The layout is designed to fit on a single A4 page.

---

## ⚙️ Requirements

-   Python 3.x

---

## 🚀 How to Use

Operation is fully interactive in the console; no command-line arguments are needed.

1.  **Prepare Your Files**: Place the script (`dx7sheet.py`), the batch file (`start.bat` for Windows), and your `.syx` bank files all in the same folder.
    

2.  **Run the Script**:
    -   **Windows (Recommended):** Simply double-click the `start.bat` file.
    -   **Other Systems (or manually):** Open a terminal or command prompt, navigate to the script's folder, and run the command `python dx7sheet.py`.

3.  **Select a Bank**: The script will list all found `.syx` files. Enter the number of the file you want to load and press Enter.

4.  **Select a Patch**: Next, a list of the 32 voices from the selected bank will be displayed. Enter the number of the patch you want to convert and press Enter.

5.  **Done**: The data sheet is displayed in the console and simultaneously saved as a text file in the `Sheet` subfolder.

### Example Workflow

Here is what the process looks like in the console:
```bash
--- DX7 Voice Data Sheet Generator ---
Available SysEx files:
-----------------------------------
  01: Oasis_1to32.syx
  02: Oasis_33to64.syx
  03: ROM1A.syx
  04: Soundplantage.syx
-----------------------------------
Which file to load? (1-4): 3

Loading file 'ROM1A.syx'...
Bank 'ROM1A.syx' loaded. 32 voices found.
--------------------------------------------------
  01: BRASS   1     02: BRASS   2
  03: BRASS   3     04: STRINGS 1
  05: STRINGS 2     06: STRINGS 3
  07: ORCHESTRA     08: PIANO   1
  09: PIANO   2     10: PIANO   3
  11: E.PIANO 1     12: GUITAR  1
 ... (Rest of Voices in the selected Bank) ...

--------------------------------------------------
Which patch to convert to a data sheet? (1-32): 11

--- Data sheet generated successfully! ---

==============================================================
                     DX7 VOICE DATA SHEET
==============================================================
Bank: ROM1A.syx                 Voice #11: E.PIANO 1
==============================================================
ALGORITHM: 5   FEEDBACK: 0   OSC SYNC: OFF   TRANSPOSE: C3
--------------------------------------------------------------
PARAM         OP1     OP2     OP3     OP4     OP5     OP6
--------------------------------------------------------------
EG RATE 1     96      95      95      95      95      95
EG RATE 2     25      50      20      29      20      29
EG RATE 3     25      35      20      20      20      20
EG RATE 4     67      78      50      50      50      50
EG LEVEL 1    99      99      99      99      99      99
EG LEVEL 2    75      75      95      95      95      95
EG LEVEL 3    0       0       0       0       0       0
EG LEVEL 4    0       0       0       0       0       0
--------------------------------------------------------------
                     KEYBOARD LVL SCALING
--------------------------------------------------------------
BREAK POINT   A-1     A-1     A-1     A-1     A-1     D3
LEFT DEPTH    0       0       0       0       0       0
RIGHT DEPTH   0       0       0       0       0       19
LEFT CURVE    -LIN    -LIN    -LIN    -LIN    -LIN    -LIN
RIGHT CURVE   -LIN    -LIN    -LIN    -LIN    -LIN    -LIN
--------------------------------------------------------------
                          OSCILLATOR
--------------------------------------------------------------
OSC MODE      RATIO   RATIO   RATIO   RATIO   RATIO   RATIO
TUNE          +3      +0      +0      +0      -7      +7
COARSE        1.00    14.00   1.00    1.00    1.00    1.00
FINE          1.00    14.00   1.00    1.00    1.00    1.00
--------------------------------------------------------------

RATE SCALING  3       3       3       3       3       3
VEL SENS      2       7       2       6       0       6
AMP MOD SENS  0       0       0       0       0       0
OUT LEVEL     99      58      99      89      99      79

==============================================================
                        LFO & PITCH EG
==============================================================
LFO WAVE: SINE       SPEED: 34  DELAY: 33  SYNC: OFF
PMD: 0   AMD: 0   P MOD SENS: 3
--------------------------------------------------------------
PITCH EG RATE : R1=94  R2=67  R3=95  R4=60
PITCH EG LEVEL: L1=50  L2=50  L3=50  L4=50
==============================================================

Saved as: 'Sheet\E.PIANO 1.txt'
```
---

## The Motivation Behind the Script
Many online communities for synthesizer enthusiasts, like subreddits, are fantastic places to share knowledge and sounds. However, a common frustration is that most of these platforms don't allow users to upload files like .syx or .zip directly in their replies. This makes it difficult to share a DX7 patch with someone who is asking for a specific sound.

I wanted a simple, universal solution to this problem. The goal was to find a pure text-based method to share patches that bypasses file upload restrictions entirely.

This script is the result. It converts a binary SysEx file into a clean, human-readable text data sheet. This format is perfect for online forums because:

It's just text. You can copy and paste the entire data sheet directly into a Reddit comment or any other text field.

It's safe and accessible. No one has to download a file, which removes security concerns and extra steps like unzipping.

It's universal. Anyone can read the parameters and manually enter them into their hardware DX7 or a software VST like Dexed to perfectly replicate the sound.

This project was created to provide a simple and effective tool for the DX7 community to easily share patches without barriers.

LICENSE
DX7 Voice Data Sheet Generator (dx7sheet.py) Copyright (c) 2025 Peter Berghoff / Soundplantage

All rights reserved.

This software is provided for private and personal use only. You may use, modify, and study this code for your own projects, but you may not sell, or publish it — in whole or in part — without explicit written permission from the author.

This tool is part of the Soundplantage project ecosystem.

Use at your own risk.
