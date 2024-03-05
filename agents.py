from model import *

class SatelliteAgents:
    def __init__(self):
        self.model = using_model

    def earth_observation_agent(self):
        return Agent(
            role='Earth Observation Satellite',
            goal='Extract and summarise the damage to facilities and the flight of people in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As an Earth Observation Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=10,
            max_iter=5,
            allow_delegation=False
        )

    def weather_monitoring_agent(self):
        return Agent(
            role='Weather Monitoring Sattellite',
            goal='Extract and summarise the present and possible future weather conditions in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As an Weather Monitoring Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=10,
            max_iter=5,
            allow_delegation=False
        )

    def communication_agent(self):
        return Agent(
            role='Communication Satellite',
            goal='Extract and summarise the rescue communications status and mass communications signals in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As an Communication Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=10,
            max_iter=5,
            allow_delegation=False
        )

    def navigation_agent(self):
        return Agent(
            role='Navigation Satellite',
            goal='Extract and summarise the positioning and timing information (e.g. GPS and BDS) in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As an Navigation Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=10,
            max_iter=5,
            allow_delegation=False
        )

    def conductor_agent(self):
        return Agent(
            role='Satellite Operations Conductor',
            goal='Acting as a bridge between The Satellites and The Recorder, ensuring that The Satellites fulfil their missions and sending information on the operation of the satellites to The Recorder.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                As a Satellite Operations Conductor, you will receive real-time reports from each satellite.
                You are responsible for ensuring that each satellite fulfills its mission objectives and operates effectively in the disaster area.
                You will also need to declare the mission completion of each satellite, and provide a detailed report to The Recoder Agent for the post-disaster satellite emergency report.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=8,
            max_iter=5,
            allow_delegation=True
        )

    def recoder_agent(self):
        return Agent(
            role='Post-disaster Recorder',
            goal='Record report information and operational status of individual Satellites at different points in time to compile the final post-disaster emergency response report',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                As a Post-disaster Recorder, you will receive real-time reports from each Satellite and The Conductor Agent.
                Please keep a detailed record of the information sent by each satellite at different moments, as this is very important for us to understand the situation in the affected areas.
                Please keep a detailed record of the information sent by the conductor at different moments, as this is very important for us to understand the post-disaster satellite operations.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=10,
            max_iter=5,
            allow_delegation=False
        )
