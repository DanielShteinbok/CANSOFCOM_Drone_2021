# CANSOFCOM Drone Detection Challenge 
This repo houses all the code related to the CANSOFCOM
Machine Learning for Drone Identification challenge,
as described in `CANSOFCOM_Challenge.pdf`.

## File Breakdown:
`drone_signal.py` is the file that contains the functions
for simulating RADAR signal returned from a drone.
This is the simulation required in parts **1** and **2**
of the challenge.

## TODO:
* Create a Jupyter notebook that contains all the 
initiation, fourier transforms, plotting etc
* Add the noise function to `drone_signal.py`,
having it take the SNR as a parameter, and call
that from the Jupyter notebook
