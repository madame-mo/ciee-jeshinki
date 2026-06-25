<h1>Introduction</h1>
<p>
Japan is an extremely earthquake prone country, sitting above an intersection of 4 major tectonic plates, causing around 1500-5000 earthquakes annually. When severe earthquakes strike, tens of millions of people are put at risk and endangered. Our robot aims to solve this issue by detecting shaking from an earthquake and guiding people to safe places to be during an emergency.
</p>

<h1>Design</h1>
<p>
We want this robot to be as efficient as possible. For the input to detect the vibrations of an earthquake, we want to utilize either accelerometers, velocity, or displacement sensors. Once a vibration is detected, the Jishinki will begin sounding an alarm from its speakers and then use its motors and  mecanum wheels to move towards a table (detected with cameras and computer vision). Once the table is detected, the Jishinki will stop and the speaker will say that a table was detected.
</p>

<h1>Implementation</h1>
<p>
We are writing in python (currently directly onto the Raspberry Pi 4). To structure the code, we want to have one file with all the movements of the car and importing that file into the main document. For the table detecting part of the project, we will use OpenCV and probably other google libraries for image recognition.
</p>

<h2>Earthquake detection function</h2>
<p>
Inputs: vibration, Output: speaker sound alarm and turning on camera to start looking for a table
</p>

<h2>Table detection function</h2>
<p>
Input: camera surrounding, Output: movement towards table
</p>
