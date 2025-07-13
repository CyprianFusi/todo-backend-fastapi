#!/bin/bash
set -e  # Exit on error
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt