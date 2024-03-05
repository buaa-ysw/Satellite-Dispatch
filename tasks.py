from crewai import Task
from textwrap import dedent

class SatelliteTasks:
    def __tip_section(self):
        return "[If you do your BEST WORK, millions of people will be saved as a result!]"

    def earth_observation_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from reporters: {report}
                Mission: 
                extract remote sensing information from the reports returned by reporters on the scene,
                determine the damage to facilities and the escape of people in the affected area, 
                self-test and adjust the operating status, 
                and report this in a timely manner to 'The Conductor Agent' and 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the damage to facilities and the escape of people in the affected area, with specific post-disaster timetable"""),
            async_execution=True,
            agent=agent,
        )

    def weather_monitoring_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from reporters: {report}
                Mission: 
                extract remote sensing information from the reports returned by reporters on the scene,
                determine the present and possible future weather conditions in the affected area,
                self-test and adjust the operating status, 
                and report this in a timely manner to 'The Conductor Agent' and 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the present and possible future weather conditions in the affected area, with specific post-disaster timetable"""),
            async_execution=True,
            agent=agent,
        )
        
    def communication_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from reporters: {report}
                Mission: 
                extract remote sensing information from the reports returned by reporters on the scene,
                determine the rescue communications status and mass communications signals in the affected area,
                self-test and adjust the operating status, 
                and report this in a timely manner to 'The Conductor Agent' and 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the rescue communications status and mass communications signals in the affected area, with specific post-disaster timetable"""),
            async_execution=True,
            agent=agent,
        )
        
    def navigation_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from reporters: {report}
                Mission: 
                extract remote sensing information from the reports returned by reporters on the scene,
                determine the present and possible future weather conditions in the affected area,
                self-test and adjust the operating status, 
                and report this in a timely manner to 'The Conductor Agent' and 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the positioning and timing information (e.g. GPS and BDS) in the affected area, with specific post-disaster timetable"""),
            async_execution=True,
            agent=agent,
        )
        
    def operation_conducting_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from reporters: {report}
                Mission: 
                check and revise the reports handed in by the satellites and submit a summary of the results to 'The Recorder Agent',
                declare the mission completion of each satellite, including the time of completion and the state of the satellite at that time, 
                and provide a detailed report to 'the Recoder Agent' for the post-disaster satellite emergency report.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the state of each satellite at each moment from the onset of the disaster to the mission completion, down to the minute."""),
            async_execution=True,
            agent=agent,
        )
        
    def report_writing_task(self, agent, disaster, context):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Mission:
                Collect reports from all Satellites and The Conductor Agent,
                prepare a specific and detailed post-disaster emergency response report,
                to enable government departmental staff to better review and improve their subsequent work on disaster relief.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                A comprehensive post-disaster emergency response report, in standard markdown format"""),
            agent=agent,
            context=context,
        )