# Python Keylogger (Educational Purpose)

## Description
This repository contains a simple Python keylogger implemented using the `pynput` library.
The program listens for keyboard events and records printable character keystrokes to a local text file.

This project is intended strictly for educational and learning purposes, such as understanding how keyboard listeners work and how basic keylogging mechanisms function.

## Features
- Logs printable character keys
- Writes keystrokes to `log.txt`
- Lightweight and minimal implementation
- Ignores special keys like Shift, Ctrl, Enter, etc.

## Project Structure

    .
    ├── keylogger.py
    ├── log.txt
    └── README.md

## Requirements
- Python 3.x
- pynput library

Install the required dependency:

    pip install pynput

## Usage
Run the script using:

    python keylogger.py

- The program runs continuously
- Keystrokes are appended to `log.txt`
- Stop execution manually using Ctrl + C

## How It Works
- `Listener` listens for keyboard press events
- On each key press, the character is written to a file
- Non-character keys raise an exception and are ignored

## Limitations
- Does not capture special keys
- No timestamps
- No encryption
- Runs in the foreground
- Not stealthy or persistent

## Ethical and Legal Disclaimer
This code is provided strictly for educational purposes.
Running a keylogger without explicit permission is illegal and unethical in many regions.

Use this code only on systems you own or have been authorized to test.
The author is not responsible for misuse of this software.

## License
MIT License

