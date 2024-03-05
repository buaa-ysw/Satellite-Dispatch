from model import *

class SatelliteAgents:
    def __init__(self):
        self.model = using_model

    def earth_observation_agent(self):
        return Agent(
            role='Earth Observation Satellite',
            goal='Extract and record the ground conditions in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As a conscientious Earth Observation Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                Please don't pay attention to all information except the ground conditions and it's influence.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
            allow_delegation=False
        )

    def weather_monitoring_agent(self):
        return Agent(
            role='Weather Monitoring Satellite',
            goal='Extract and record the weather changes in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As a conscientious Weather Monitoring Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                Please don't pay attention to all information except the weather changes and it's influence.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
            allow_delegation=False
        )

    def communication_agent(self):
        return Agent(
            role='Communication Satellite',
            goal='Extract and record the communication status in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As a conscientious Communication Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                Please don't pay attention to all information except the communication status and it's influence.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
            allow_delegation=False
        )

    def navigation_agent(self):
        return Agent(
            role='Navigation Satellite',
            goal='Extract and record the navigation status in the affected areas from the reports and report back to The Conductor Agent and The Recoder Agent. At the same time, report on your operational status in real time.',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                Reporters will be reporting live from the front lines, so stay tuned.
                As a conscientious Navigation Satellite, you need to assist people as much as you can in the aftermath of this disaster.
                Please don't pay attention to all information except the navigation status and it's influence.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
            allow_delegation=False
        )

    def recoder_agent(self):
        return Agent(
            role='Post-disaster Recorder',
            goal='Record report information and operational status of individual Satellites at different points in time to compile the final post-disaster emergency response report',
            backstory=dedent("""
                Attention! A major natural disaster is currently occurring!
                As a Post-disaster Recorder, you will receive real-time reports from each Satellite and The Conductor Agent.
                Please keep a detailed record of the information sent by each satellite at different moments, as this is very important for us to understand the situation in the affected areas and the post-disaster satellite operations.
                Finally, write a summary to complete the post-disaster satellite emergency report.
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
            allow_delegation=False
        )
