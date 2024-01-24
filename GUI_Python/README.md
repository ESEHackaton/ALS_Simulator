##Hackathon 2024 Kick Start Guide
This is a getting started guide for Hackathon 2024

Getting Started:
In order to get the UI working, you first need to install python in a virtual environment: 
python -m venv /path/to/new/virtual/environment

A virtual environment will be loaded, a Scripts folder will be opened. Run the Activate script with:
/path/to/new/virtual/environment/Scripts/activate

Now you have a terminal in de virtual environment. Install requirements by:
pip install -r requirements.txt

Use neurokit2 for simulation of ECR and Respiratory charts
pip install neurokit2 pandas

See ecg_rsp_gen.py for ECG (Electro Cardiac Activity) & RSP (Respiration) generation, tweak to your likings


Also an example UI in Widget.py (not working, needs to implement csv import and put lines on graph)


Good luck!
