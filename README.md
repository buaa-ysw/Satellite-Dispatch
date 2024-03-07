# 🛰️Satellite-Dispatch

The Satellite-Dispatch is an CrewAI-driven platform designed to facilitate disaster response and recovery efforts using satellite technology. This project aims to harness the capabilities of various types of satellites, including Earth observation, weather monitoring, communication, and navigation satellites, to support emergency responders and authorities in mitigating the impact of natural disasters.

## Overview

The Satellite Emergency Response System comprises a set of AI agents simulating different types of satellites and a central control system for coordinating satellite operations during and after a disaster. These AI agents are responsible for tasks such as capturing imagery, monitoring weather conditions, maintaining communication, providing navigation services, recording satellite actions, and compiling post-disaster reports.

## Getting Started

1. Clone the repository:

```
git clone https://github.com/buaa-ysw/Satellite-Dispatch.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Select the model in `config.ini` and modify the `.env.example` file.

4. Run the application:

```
python main.py
```

5. Input a disaster to run.

## Example

```
A minor earthquake occurred at 1:02:46 PM (PST) on Monday, March 4, 2024. The magnitude 3.8 event occurred 41 km (25 miles) SSW of Carlin, NV. The hypocentral depth is 10 km ( 6 miles).
```



[report_events]:https://github.com/buaa-ysw/Satellite-Dispatch/blob/main/output/report/Earthquake%20in%20Carlin%2C%20NV/Earthquake%20in%20Carlin%2C%20NV_events.md


## Usage

1. Configure AI agents for each type of satellite according to specific disaster scenarios and objectives.
2. Monitor satellite operations and adjust tasks as needed to support emergency response efforts.

## Contributing

Contributions to the Satellite Emergency Response System project are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request or open an issue on GitHub.

## Acknowledgements

- This project was inspired by the need for advanced technology solutions to support disaster response and recovery efforts.
- Special thanks to the developers and contributors who have helped make this project possible.
