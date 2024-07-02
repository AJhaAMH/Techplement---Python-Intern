#!/bin/bash
cd week1_tasks
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
python app.py

