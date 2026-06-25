<p align="right"><a href="#implementation">Jump to Implementation ↓</a></p>

<h1>Jishinki Robot Design Documentation</h1>
<hr>

<section id="introduction">
    <h2>1. Introduction</h2>
    <p>
        Japan is an extremely earthquake-prone country, sitting above an intersection of <strong>four major tectonic plates</strong>, causing around 1,500 to 5,000 earthquakes annually. When severe earthquakes strike, tens of millions of people are put at risk and endangered.
    </p>
    <p>
        Our robot aims to solve this issue by detecting shaking from an earthquake and guiding people to safe places to be during an emergency.
    </p>
</section>

<br>

<section id="design">
    <h2>2. Design</h2>
    <p>We want this robot to be as efficient as possible. The core mechanics are broken down below:</p>
    
    <ul>
        <li>
            <strong>Input Detection:</strong> To detect the vibrations of an earthquake, the system will utilize either <em>accelerometers</em>, <em>velocity sensors</em>, or <em>displacement sensors</em>.
        </li>
        <li>
            <strong>Alert & Mobility:</strong> Once a vibration is detected, the Jishinki will begin sounding an alarm from its speakers and then use its motors and <strong>mecanum wheels</strong> to move towards a table.
        </li>
        <li>
            <strong>Target Acquisition:</strong> Tables will be detected using cameras and computer vision. Once the table is detected, the Jishinki will stop, and the speaker will announce that a table was successfully located.
        </li>
    </ul>
</section>

<br>

<section id="implementation">
    <h2>3. Implementation</h2>
    <p>
        The software environment is written in <strong>Python</strong>, deployed directly onto a <strong>Raspberry Pi 4</strong>. To maintain clean architecture, we are structuring the codebase modularly: one file will manage all physical car movements, which is then imported directly into the main execution document.
    </p>
    <p>
        For the object detection sequence, we will leverage <strong>OpenCV</strong> alongside specialized machine learning/image recognition libraries.
    </p>

    <h3>Functional Architecture</h3>
    <blockquote>
        <strong>Earthquake Detection Function</strong><br>
        <ul>
            <li><strong>Inputs:</strong> Vibration data</li>
            <li><strong>Outputs:</strong> Speaker sound alarm; activates camera sequence to look for a table</li>
        </ul>
    </blockquote>

    <blockquote>
        <strong>Table Detection Function</strong><br>
        <ul>
            <li><strong>Inputs:</strong> Camera surrounding environment feeds</li>
            <li><strong>Outputs:</strong> Motor movement direction towards the detected table</li>
        </ul>
    </blockquote>
</section>

<hr>
