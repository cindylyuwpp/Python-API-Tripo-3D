# Python API – Tripo 3D Rig Check

A Python script that uses the [Tripo 3D API](https://developers.tripo3d.ai/en/docs/animations-rig-check) to check whether a 3D model can be rigged for animation, and what type of rig it needs.

This is one "node" in a creative workflow: a 3D model goes in, and the rig check result comes out, ready to pass to the next step (like animation).

## What it does
1. Sends a 3D model URL to Tripo's **Rig Check** endpoint (POST)
2. Checks the task status every few seconds until it finishes (GET)
3. Prints whether the model is riggable and the recommended rig type

Example output with the sample Fox model:
```
Status: running
Status: success
Can be rigged: True
Rig type: quadruped
```

## Setup
1. Create and turn on a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install requests:
   ```
   pip install requests
   ```
3. Create a file called `my_secret_api.py` with your own Tripo **secret key** (starts with `tsk_`):
   ```python
   TRIPO_API_KEY = "tsk_your_key_here"
   ```
   This file is listed in `.gitignore`, so it is never uploaded.

## Run
```
python3 tripo-api-3d.py
```

## Possible rig types
`biped`, `quadruped`, `hexapod`, `octopod`, `avian`, `serpentine`, `aquatic`

## Built with
- Python 3
- [requests](https://pypi.org/project/requests/)
- [Tripo 3D API](https://developers.tripo3d.ai)
