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
    
<img width="518" height="873" alt="DX7sheet" src="https://github.com/user-attachments/assets/a11218b9-3a97-4f71-850b-ca10f758e1a6" />

---
## The Motivation Behind the Script

Many online communities for synthesizer enthusiasts, like subreddits, are fantastic places to share knowledge and sounds. However, a common frustration is that most of these platforms don't allow users to upload files like .syx or .zip directly in their replies. This makes it difficult to share a DX7 patch with someone who is asking for a specific sound.

I wanted a simple, universal solution to this problem. The goal was to find a pure text-based method to share patches that bypasses file upload restrictions entirely.

This script is the result. It converts a binary SysEx file into a clean, human-readable text data sheet. This format is perfect for online forums because:

It's just text. You can copy and paste the entire data sheet directly into a Reddit comment or any other text field.

It's safe and accessible. No one has to download a file, which removes security concerns and extra steps like unzipping.

It's universal. Anyone can read the parameters and manually enter them into their hardware DX7 or a software VST like Dexed to perfectly replicate the sound.

This project was created to provide a simple and effective tool for the DX7 community to easily share patches without barriers.

---

LICENCE:

DX7 Voice Data Sheet Generator (dx7sheet.py)
Copyright (c) 2025 Peter Berghoff / Soundplantage

All rights reserved.

This software is provided for private and personal use only.
You may use, modify, and study this code for your own projects,
but you may not sell, or publish it — in whole
or in part — without explicit written permission from the author.

This tool is part of the Soundplantage project ecosystem.

Use at your own risk.
