# DX7 Voice Data Sheet Generator

A Python script to generate human-readable data sheets from Yamaha DX7 32-voice SysEx files (`.syx`). This tool is perfect for archiving, sharing, or manually re-entering patches into a hardware synthesizer or a software editor like Dexed.

## 📋 Features

-   Reads standard 32-voice `.syx` bank files.
-   Lists all 32 patch names and prompts for a selection.
-   Generates a detailed data sheet for the chosen patch.
-   Formats all parameters to match the DX7's display logic.
-   Saves the data sheet as a `.txt` file, named after the patch.
-   The layout is optimized to fit on a single A4 page.

---
## ⚙️ Requirements

-   Python 3.x

---
## 🚀 How to Use

This is a command-line tool.

1.  **Save the Script**: Make sure the script `dx7sheet.py` is saved on your computer. For this example, we assume it is located at `F:/dxtools/dx7sheet/dx7sheet.py`.

2.  **Open a Command Prompt**: Open a command-line interface like PowerShell or Command Prompt.

3.  **Run the Script**: Execute the script by typing `python`, followed by the full path to the script and the name of your SysEx file.

    **Syntax:**
    ```bash
    python [path_to_script] [sysex_file]
    ```

    **Example:**
    ```bash
    python F:/dxtools/dx7sheet/dx7sheet.py Soundplantage.syx

## Example of an exported DX7 Voice Data Sheet:
============================================================
                    DX7 VOICE DATA SHEET                    
============================================================
Bank: Soundplantage.syx         Voice #01: Security
============================================================
ALGORITHM: 9   FEEDBACK: 0   OSC SYNC: OFF   TRANSPOSE: C3
------------------------------------------------------------
PARAM       OP1     OP2     OP3     OP4     OP5     OP6
------------------------------------------------------------
EG RATE 1   87      91      99      99      91      82
EG RATE 2   65      62      30      93      51      78
EG RATE 3   32      34      20      65      7       26
EG RATE 4   59      50      58      73      42      74
EG LEVEL 1  99      99      99      99      99      99
EG LEVEL 2  94      97      94      99      96      88
EG LEVEL 3  0       0       0       0       81      62
EG LEVEL 4  0       0       0       0       0       89
------------------------------------------------------------
                    KEYBOARD LVL SCALING                    
------------------------------------------------------------
BREAK POINT F#5     C0      C#3     F5      A-1     A-1
LEFT DEPTH  10      0       5       0       0       0
RIGHT DEPTH 0       33      3       6       26      15
LEFT CURVE  -LIN    -LIN    +LIN    -LIN    -LIN    -LIN
RIGHT CURVE -LIN    -EXP    -LIN    +LIN    -EXP    -EXP
------------------------------------------------------------
                         OSCILLATOR                         
------------------------------------------------------------
OSC MODE    RATIO   RATIO   RATIO   FIX     RATIO   RATIO
TUNE        +0      +2      +0      -1      +0      +0
COARSE      1.00    1.00    1.00    100.00  1.00    3.00
FINE        1.00    1.00    1.00    112.202 1.00    3.00
------------------------------------------------------------
RATE SCALING3       3       3       1       3       3
VEL SENS    2       2       6       2       6       2
AMP MOD SENS0       0       0       0       0       0
OUT LEVEL   89      80      95      74      84      76

============================================================
                       LFO & PITCH EG                       
============================================================
LFO WAVE: TRIANGLE   SPEED: 10  DELAY: 0   SYNC: OFF
PMD: 19  AMD: 0   P MOD SENS: 0  
------------------------------------------------------------
PITCH EG RATE : R1=99  R2=99  R3=99  R4=99 
PITCH EG LEVEL: L1=50  L2=50  L3=50  L4=50 
============================================================
    ```

4.  **Select a Voice**: The script will list all available voices. Type the number of the voice you want to generate a data sheet for and press **Enter**.

5.  **Get the Output**: The data sheet will be printed to the console, and a `.txt` file (e.g., `Security.txt`) will be saved in the same directory where you ran the command.
