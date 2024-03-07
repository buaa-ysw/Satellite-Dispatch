# 🛰️Satellite-Dispatch

The Satellite-Dispatch is an CrewAI-driven platform designed to facilitate disaster response and recovery efforts using satellite technology. This project aims to harness the capabilities of various types of satellites, including Earth observation, weather monitoring, communication, and navigation satellites, to support emergency responders and authorities in mitigating the impact of natural disasters.

## Overview

The Satellite Emergency Response System comprises a set of AI agents simulating different types of satellites and a central control system for coordinating satellite operations during and after a disaster. These AI agents are responsible for tasks such as capturing imagery, monitoring weather conditions, maintaining communication, providing navigation services, recording satellite actions, and compiling post-disaster reports.

## Getting Started

1. Clone the repository:

```python
git clone https://github.com/buaa-ysw/Satellite-Dispatch.git
```

2. Install dependencies:

```python
pip install -r requirements.txt
```

3. Select the model in `config.ini` and modify the `.env.example` file.

4. Run the application:

```python
python main.py
```

5. Input a disaster to run.

## Example

```python
A minor earthquake occurred at 1:02:46 PM (PST) on Monday, March 4, 2024. The magnitude 3.8 event occurred 41 km (25 miles) SSW of Carlin, NV. The hypocentral depth is 10 km ( 6 miles).
```

```markdown
-------------------------
# Carlin Earthquake Satellite Emergency Reporting
---
------------------------- *[1:02:46 PM (PST)]* -------------------------
*Minor earthquake of magnitude 3.8 occurs 41 km (25 miles) SSW of Carlin, NV*.
                    **Earth Observation Satellite**
"Buildings and trees began to shake."
                    **Weather Monitoring Satellite**
"The sky is clouded over."
                    **Communication Satellite**
"Minor disturbances occur."
                    **Navigation Satellite**
"Precise positioning data provided to guide search and rescue teams."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[1:45 PM (42 minutes after)]* -------------------------
                    **Earth Observation Satellite**
"Buildings in Carlin show minor structural damage."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[2:10 PM (1 hour, 7 minutes after)]* ------------------------
                    **Earth Observation Satellite**
"Residents in Carlin feel continuous tremors, causing panic."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[2:35 PM (1 hour, 32 minutes after)]* ------------------------
                    **Weather Monitoring Satellite**
"Overcast skies observed in Carlin."
                    **Communication Satellite**
"Power outages affecting communication services."
                    **Navigation Satellite**
"Navigation systems assisting emergency services."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[3:25 PM (2 hours, 22 minutes after)]* ------------------------
                    **Navigation Satellite**
"Providing accurate navigation data despite weakened signals."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[3:50 PM (2 hours, 47 minutes after)]* ------------------------
                    **Weather Monitoring Satellite**
"Heavy rain hindering rescue efforts."
                    **Communication Satellite**
"Improved communication as backup systems activated."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[4:15 PM (3 hours, 13 minutes after)]* ------------------------
                    **Communication Satellite**
"Additional bandwidth allocated to assist emergency response."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[4:40 PM (3 hours, 38 minutes after)]* ------------------------
                    **Earth Observation Satellite**
"Evacuation orders issued for unsafe areas."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[5:05 PM (4 hours, 3 minutes after)]* ------------------------
                    **Navigation Satellite**
"Providing accurate navigation data despite weakened signals."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[6:45 PM (5 hours, 43 minutes after)]* ------------------------
                    **Communication Satellite**
"Improved communication as backup systems activated."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[7:10 PM (6 hours, 7 minutes after)]* ------------------------
                    **Earth Observation Satellite**
"Search and rescue teams working to extract trapped individuals."
-------------------------------------- *[over]* --------------------------------------

------------------------- *[8:25 PM (7 hours, 23 minutes after)]* ------------------------
                    **Earth Observation Satellite**
"Cleanup and recovery operations begin."
                    **Weather Monitoring Satellite**
"Clear skies aid cleanup operations."
                    **Communication Satellite**
"Communication services restored to normal levels."
                    **Navigation Satellite**
"Navigation systems fully operational."
-------------------------------------- *[over]* --------------------------------------
```

## Usage

1. Configure AI agents for each type of satellite according to specific disaster scenarios and objectives.
2. Monitor satellite operations and adjust tasks as needed to support emergency response efforts.

## Contributing

Contributions to the Satellite Emergency Response System project are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request or open an issue on GitHub.

## Acknowledgements

- This project was inspired by the need for advanced technology solutions to support disaster response and recovery efforts.
- Special thanks to the developers and contributors who have helped make this project possible.
