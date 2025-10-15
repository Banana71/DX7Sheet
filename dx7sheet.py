# -*- coding: utf-8 -*-

import sys
import os
import re
import math

# --- Konstanten und Mapping-Tabellen ---

NOTE_NAMES = ['A-1', 'A#-1', 'B-1', 'C0', 'C#0', 'D0', 'D#0', 'E0', 'F0', 'F#0', 'G0', 'G#0', 'A0', 'A#0', 'B0', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7', 'C8']
CURVE_MODES = {0: '-LIN', 1: '-EXP', 2: '+EXP', 3: '+LIN'}
LFO_WAVES = {0: 'TRIANGLE', 1: 'SAW UP', 2: 'SAW DOWN', 3: 'SQUARE', 4: 'SINE', 5: 'S+HOLD'}
FIXED_FREQ_MAP = {0: 1.0, 1: 10.0, 2: 100.0, 3: 1000.0}
DX7_32_VOICE_HEADER = b'\xf0\x43\x00\x09\x20\x00'
SYSEX_SIZE = 4104

def parse_single_voice(data):
    """
    Parst die 128 Bytes eines einzelnen Voice-Patches basierend auf der
    exakten Bit-Maskierung aus der Dokumentation und der finalen Korrektur.
    """
    params = {'ops': []}

    for i in range(6):
        op_data = data[i * 17 : (i + 1) * 17]
        op = {}

        op['eg_rate'] = list(op_data[0:4])
        op['eg_level'] = list(op_data[4:8])
        op['break_point'] = NOTE_NAMES[op_data[8]] if 0 <= op_data[8] <= 99 else 'N/A'
        op['l_depth'] = op_data[9]
        op['r_depth'] = op_data[10]
        op['l_curve'] = CURVE_MODES[op_data[11] & 3]
        op['r_curve'] = CURVE_MODES[(op_data[11] >> 2) & 3]

        # ================================================================= #
        # Korrigiert von Soundplantage
        op['rate_scale'] = op_data[12] & 0x07
        op['tune'] = ((op_data[12] & 120) >> 3) - 7
        # ================================================================= #

        # Byte o+13: Key Velocity Sens (KVS) & Amp Mod Sens (AMS)
        op['key_vel'] = (op_data[13] >> 2) & 0x07
        op['amp_mod_sens'] = op_data[13] & 0x03

        op['level'] = op_data[14]

        # Byte o+15: OSC Mode (M) & Freq Coarse (FC)
        op['osc_mode'] = 'FIX' if op_data[15] & 1 else 'RATIO'
        coarse_byte = op_data[15] >> 1
        
        op['fine_raw'] = op_data[16]
        
        if op['osc_mode'] == 'RATIO':
            op['coarse_val'] = 0.5 if coarse_byte == 0 else float(coarse_byte)
        else: # Fixed Mode
            op['coarse_val'] = FIXED_FREQ_MAP.get(coarse_byte & 3, 1.0)

        params['ops'].append(op)
        
    params['ops'].reverse()

    # Globale Parameter
    pitch_eg_data = data[102:110]
    params['pitch_eg_rate'] = list(pitch_eg_data[0:4])
    params['pitch_eg_level'] = list(pitch_eg_data[4:8])
    params['algorithm'] = (data[110] & 0x1F) + 1
    params['feedback'] = (data[110] >> 5) & 0x07
    params['osc_sync'] = 'ON' if data[111] & 8 else 'OFF'
    params['lfo_speed'] = data[112]
    params['lfo_delay'] = data[113]
    params['lfo_pmd'] = data[114]
    params['lfo_amd'] = data[115]
    params['lfo_sync'] = 'ON' if data[116] & 1 else 'OFF'
    params['lfo_wave'] = LFO_WAVES[(data[116] >> 1) & 7]
    params['p_mod_sens'] = data[117] & 7
    params['name'] = data[118:128].decode('ascii', errors='ignore').strip()
    params['transpose'] = "C3"
    
    return params

def generate_datasheet(params, bank_name, voice_num):
    ops = params['ops']
    PARAM_WIDTH = 12
    OP_WIDTH = 8
    
    sheet = []
    
    def create_op_row(name, values):
        row_str = f"{name:<{PARAM_WIDTH}}"
        for val in values:
            row_str += f"{str(val):<{OP_WIDTH}}"
        return row_str.rstrip()

    sheet.append("="*60)
    sheet.append(f"DX7 VOICE DATA SHEET".center(60))
    sheet.append("="*60)
    sheet.append(f"Bank: {bank_name:<25} Voice #{voice_num:02d}: {params['name']}")
    sheet.append("="*60)
    sheet.append(f"ALGORITHM: {params['algorithm']}   FEEDBACK: {params['feedback']}   OSC SYNC: {params['osc_sync']}   TRANSPOSE: {params['transpose']}")
    sheet.append("-"*60)
    
    sheet.append(create_op_row("PARAM", [f"OP{i+1}" for i in range(6)]))
    sheet.append("-"*60)
    
    param_map = [("EG RATE 1", "eg_rate", 0), ("EG RATE 2", "eg_rate", 1), ("EG RATE 3", "eg_rate", 2), ("EG RATE 4", "eg_rate", 3), ("EG LEVEL 1", "eg_level", 0), ("EG LEVEL 2", "eg_level", 1), ("EG LEVEL 3", "eg_level", 2), ("EG LEVEL 4", "eg_level", 3)]
    for name, key, index in param_map:
        sheet.append(create_op_row(name, [op[key][index] for op in ops]))
        
    sheet.append("-"*60)
    sheet.append("KEYBOARD LVL SCALING".center(60))
    sheet.append("-"*60)

    sheet.append(create_op_row("BREAK POINT", [op['break_point'] for op in ops]))
    sheet.append(create_op_row("LEFT DEPTH", [op['l_depth'] for op in ops]))
    sheet.append(create_op_row("RIGHT DEPTH", [op['r_depth'] for op in ops]))
    sheet.append(create_op_row("LEFT CURVE", [op['l_curve'] for op in ops]))
    sheet.append(create_op_row("RIGHT CURVE", [op['r_curve'] for op in ops]))
    
    sheet.append("-"*60)
    sheet.append("OSCILLATOR".center(60))
    sheet.append("-"*60)
    
    coarse_display_values = [f"{op['coarse_val']:.2f}" for op in ops]
    
    fine_display_values = []
    for op in ops:
        if op['osc_mode'] == 'RATIO':
            fine_val = op['coarse_val'] + (op['coarse_val'] * op['fine_raw'] / 100.0)
            fine_display_values.append(f"{fine_val:.2f}")
        else:
            fine_val = math.pow(1.023293, op['fine_raw']) * op['coarse_val']
            fine_display_values.append(f"{fine_val:.3f}")

    sheet.append(create_op_row("OSC MODE", [op['osc_mode'] for op in ops]))
    sheet.append(create_op_row("TUNE", [f"{op['tune']:+}" for op in ops]))
    sheet.append(create_op_row("COARSE", coarse_display_values))
    sheet.append(create_op_row("FINE", fine_display_values))
    
    sheet.append("-"*60)
    
    sheet.append(create_op_row("RATE SCALING", [op['rate_scale'] for op in ops]))
    sheet.append(create_op_row("VEL SENS", [op['key_vel'] for op in ops]))
    sheet.append(create_op_row("AMP MOD SENS", [op['amp_mod_sens'] for op in ops]))
    sheet.append(create_op_row("OUT LEVEL", [op['level'] for op in ops]))
    
    sheet.append("")
    sheet.append("="*60)
    sheet.append("LFO & PITCH EG".center(60))
    sheet.append("="*60)
    sheet.append(f"LFO WAVE: {params['lfo_wave']:<10} SPEED: {params['lfo_speed']:<3} DELAY: {params['lfo_delay']:<3} SYNC: {params['lfo_sync']}")
    sheet.append(f"PMD: {params['lfo_pmd']:<3} AMD: {params['lfo_amd']:<3} P MOD SENS: {params['p_mod_sens']:<3}")
    sheet.append("-"*60)
    
    r = params['pitch_eg_rate']
    l = params['pitch_eg_level']
    sheet.append(f"PITCH EG RATE : R1={r[0]:<3} R2={r[1]:<3} R3={r[2]:<3} R4={r[3]:<3}")
    sheet.append(f"PITCH EG LEVEL: L1={l[0]:<3} L2={l[1]:<3} L3={l[2]:<3} L4={l[3]:<3}")
    sheet.append("="*60)
    
    return "\n".join(sheet)

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def main():
    if len(sys.argv) != 2:
        print("Verwendung: python dx7sheet.py <sysex_datei.syx>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    
    if not os.path.exists(filepath):
        print(f"Fehler: Datei nicht gefunden -> '{filepath}'")
        sys.exit(1)
        
    try:
        with open(filepath, 'rb') as f:
            sysex_data = f.read()
    except IOError as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        sys.exit(1)
        
    if len(sysex_data) != SYSEX_SIZE or not sysex_data.startswith(DX7_32_VOICE_HEADER):
        print("Fehler: Dies scheint keine gültige Yamaha DX7 32-Voice SysEx-Datei zu sein.")
        sys.exit(1)
        
    voice_bulk_data = sysex_data[6:4102]
    voices = [voice_bulk_data[i:i+128] for i in range(0, 4096, 128)]
    voice_names = [v[118:128].decode('ascii', errors='ignore').strip() for v in voices]
    
    print("--- DX7 Voice Data Sheet Generator ---")
    print(f"Bank '{os.path.basename(filepath)}' geladen. 32 Voices gefunden.")
    print("-" * 36)
    for i, name in enumerate(voice_names, 1):
        print(f"  {i:02d}: {name}")
    print("-" * 36)
        
    choice = -1
    while not (1 <= choice <= 32):
        try:
            raw_choice = input("Welchen Patch in ein Data Sheet umwandeln? (1-32): ")
            choice = int(raw_choice)
            if not (1 <= choice <= 32):
                print("Bitte eine Zahl zwischen 1 und 32 eingeben.")
        except (ValueError, TypeError):
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            
    selected_voice_data = voices[choice - 1]
    parsed_params = parse_single_voice(selected_voice_data)
    
    datasheet = generate_datasheet(parsed_params, os.path.basename(filepath), choice)
    
    # KORREKTUR: Der NameError wurde behoben.
    filename = sanitize_filename(parsed_params['name']) + ".txt"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(datasheet)
        print("\n--- Datenblatt wurde erfolgreich generiert! ---\n")
        print(datasheet)
        print(f"\nGespeichert als: '{filename}'")
    except IOError as e:
        print(f"\nFehler beim Speichern der Datei: {e}")

if __name__ == '__main__':
    main()