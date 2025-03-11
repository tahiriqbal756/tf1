#!/bin/bash

echo "=================================="
echo "  🔥 Made by HACKER TF 🔥  "
echo "=================================="

# Required Packages Install
pkg update -y
pkg install python -y
pip install tqdm

# Run Python Script
python tf.py
