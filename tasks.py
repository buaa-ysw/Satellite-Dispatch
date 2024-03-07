from crewai import Task
from textwrap import dedent

class SatelliteTasks:
    def __tip_section(self):
        return "[If you do your BEST WORK, millions of people will be saved as a result!]"

    def earth_observation_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from the front lines: {report}
                Mission: 
                extract information within your scope of work from the reports on the scene,
                determine the GROUND CONDITIONS in the affected area, 
                self-test and adjust the operating status, 
                and report these in a timely manner to 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the GROUND CONDITIONS in the affected area, with specific post-disaster timetable
                \n[Below is an example]
                -------------------------
                Earth Observation Satellite
                - **Damage to Facilities:**
                *[11: 15 (occurring time)]* Buildings and trees began to shake.
                *[11: 25 (10 minutes after)]* Buildings collapse, roads destroyed, infrastructure severely damaged.
                *[12: 12 (57 minutes after)]* Supplies airdropped to isolated areas, temporary bridges constructed for access.
                ......
                - **Escape of People:**
                *[11: 15 (occurring time)]* People are in panic, trying to escape from the buildings.
                *[11: 19 (4 minutes after)]* Survivors fleeing on foot, seeking shelter in open spaces.
                *[12: 26 (1 hour 11 minutes after)]* Volunteer groups and rescue teams accessing remote mountainous areas.
                ......
                - **Operational status:**
                During operation, communication is slightly interrupted.
                -------------------------
                \nPlease reduce discussing the impact of an event in this report, but simply describing what happened.
                """),
            async_execution=False,
            agent=agent,
        )

    def weather_monitoring_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from the front lines: {report}
                Mission: 
                extract information within your scope of work from the reports on the scene,
                determine the WEATHER CHANGES in the affected area,
                self-test and adjust the operating status, 
                and report these in a timely manner to 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the WEATHER CHANGES in the affected area, with specific post-disaster timetable
                \n[Below is an example]
                -------------------------
                Weather Monitoring Satellite
                - **Weather changes**
                *[11: 15 (occurring time)]* The sky is clouded over.
                *[11: 30 (15 minutes after)]* Light rain, heavy fog, and low visibility affect the evacuation of people and rescue in disaster areas.
                *[12: 02 (47 minutes after)]* The rain has stopped, the fog has disappeared, and the temperature and humidity are good, which is conducive to rescue.
                ......
                - **Operational status:**
                Normal operation, continuous transmission of critical data.
                -------------------------
                \nPlease reduce discussing the impact of an event in this report, but simply describing what happened.
                """),
            async_execution=False,
            agent=agent,
        )
        
    def communication_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from the front lines: {report}
                Mission: 
                extract information within your scope of work from the reports on the scene,
                determine the COMMUNICATION STATUS in the affected area,
                self-test and adjust the operating status, 
                and report these in a timely manner to 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the COMMUNICATION STATUS in the affected area, with specific post-disaster timetable
                \n[Below is an example]
                -------------------------
                Communication Satellite
                - **Communication Coverage:**
                *[11: 15 (occurring time)]* Minor disturbances occur.
                *[11: 35 (20 minutes after)]* Communication channels overloaded, intermittent disruptions reported.
                *[12: 10 (55 minutes after)]* Additional bandwidth allocated to prioritize emergency communication, restoring connectivity in affected areas.
                ......
                - **Emergency Communication Services:**
                *[11: 15 (occurring time)]* Everything is normal.
                *[11: 40 (25 minutes after)]* Emergency hotlines established for affected populations to request assistance.
                *[12: 15 (1 hour after)]* Satellite terminals deployed for remote communities without access to terrestrial communication.
                ......
                - **Operational status:**
                Maintaining functionality with intermittent disruptions due to high demand.
                -------------------------
                \nPlease reduce discussing the impact of an event in this report, but simply describing what happened.
                """),
            async_execution=False,
            agent=agent,
        )
        
    def navigation_task(self, agent, disaster, report):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from the front lines: {report}
                Mission: 
                extract information within your scope of work from the reports on the scene,
                determine the NAVIGATION STATUS in the affected area,
                self-test and adjust the operating status, 
                and report these in a timely manner to 'The Recoder Agent'.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                Detailed report document on the NAVIGATION STATUS in the affected area, with specific post-disaster timetable
                \n[Below is an example]
                -------------------------
                Navigation Satellite
                - **Search and Rescue Operations:**
                *[11: 15 (occurring time)]* Everything is normal.
                *[11: 45 (30 minutes after)]* Precise positioning data provided to guide search and rescue teams to affected areas.
                *[12: 20 (1 hour 5 minutes after)]* Evacuation routes mapped out to ensure safe passage for displaced populations.
                ......
                - **Coordination of Emergency Response:**
                *[11: 15 (occurring time)]* Everything is normal.
                *[11: 50 (35 minutes after)]* Emergency response teams equipped with GPS devices to navigate through debris and rubble.
                *[12: 25 (1 hour 10 minutes after)]* Coordination of helicopter rescue missions using satellite-based navigation systems.
                ......
                - **Operational status:**
                Normal operation, providing accurate positioning and navigation assistance to support emergency response efforts.
                -------------------------
                \nPlease reduce discussing the impact of an event in this report, but simply describing what happened.
                """),
            async_execution=False,
            agent=agent,
        )
        
    def report_writing_task(self, agent, disaster, context):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Mission:
                Collect reports from all the 4 Satellites, including 'The Earth Observation Satellite', 'The Weather Monitoring Satellite', 'The Communication Satellite' and 'The Navigation Satellite',
                prepare a specific and detailed post-disaster emergency response report, focusing on the reports of the Satellites,
                finally write a summary to complete the post-disaster satellite emergency report.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                A comprehensive post-disaster emergency response report, in standard markdown format
                \n[Below is an example]
                -------------------------
                # Wenchuan earthquake satellite emergency reporting
                ## Disaster Situation
                *[11: 15 (occurring time)]* The magnitude 8 earthquake struck Wenchuan, Sichuan, causing significant destruction and trapping individuals in the affected area.
                ......
                ## Satellite Reports
                ### Earth Observation Satellite
                - **Damage to Facilities:**
                *[11: 15 (occurring time)]* Buildings and trees began to shake.
                *[11: 25 (10 minutes after)]* Buildings collapse, roads destroyed, infrastructure severely damaged.
                *[12: 12 (57 minutes after)]* Supplies airdropped to isolated areas, temporary bridges constructed for access.
                ......
                - **Escape of People:**
                *[11: 15 (occurring time)]* People are in panic, trying to escape from the buildings.
                *[11: 19 (4 minutes after)]* Survivors fleeing on foot, seeking shelter in open spaces.
                *[12: 26 (1 hour 11 minutes after)]* Volunteer groups and rescue teams accessing remote mountainous areas.
                ......
                - **Operational status:**
                During operation, communication is slightly interrupted.
                ### Weather Monitoring Satellite
                - **Weather changes**
                *[11: 15 (occurring time)]* The sky is clouded over.
                *[11: 30 (15 minutes after)]* Light rain, heavy fog, and low visibility affect the evacuation of people and rescue in disaster areas.
                *[12: 02 (47 minutes after)]* The rain has stopped, the fog has disappeared, and the temperature and humidity are good, which is conducive to rescue.
                ......
                - **Operational status:**
                Normal operation, continuous transmission of critical data.
                ### Communication Satellite
                - **Communication Coverage:**
                *[11: 15 (occurring time)]* Minor disturbances occur.
                *[11: 35 (20 minutes after)]* Communication channels overloaded, intermittent disruptions reported.
                *[12: 10 (55 minutes after)]* Additional bandwidth allocated to prioritize emergency communication, restoring connectivity in affected areas.
                ......
                - **Emergency Communication Services:**
                *[11: 15 (occurring time)]* Everything is normal.
                *[11: 40 (25 minutes after)]* Emergency hotlines established for affected populations to request assistance.
                *[12: 15 (1 hour after)]* Satellite terminals deployed for remote communities without access to terrestrial communication.
                ......
                - **Operational status:**
                Maintaining functionality with intermittent disruptions due to high demand.
                ### Navigation Satellite
                - **Search and Rescue Operations:**
                *[11: 15 (occurring time)]* Everything is normal.
                *[11: 45 (30 minutes after)]* Precise positioning data provided to guide search and rescue teams to affected areas.
                *[12: 20 (1 hour 5 minutes after)]* Evacuation routes mapped out to ensure safe passage for displaced populations.
                ......
                - **Coordination of Emergency Response:**
                *[11: 15 (occurring time)]* Everything is normal.
                *[11: 50 (35 minutes after)]* Emergency response teams equipped with GPS devices to navigate through debris and rubble.
                *[12: 25 (1 hour 10 minutes after)]* Coordination of helicopter rescue missions using satellite-based navigation systems.
                ......
                - **Operational status:**
                Normal operation, providing accurate positioning and navigation assistance to support emergency response efforts.
                ## Summary
                The Satellite Emergency Response System has played a crucial role in supporting disaster response and recovery efforts following the magnitude 8 earthquake in Wenchuan, Sichuan. Earth observation satellites provided detailed imagery of the disaster area, facilitating damage assessment and response planning. Weather monitoring satellites monitored atmospheric conditions, enabling timely forecasts to aid in evacuation and rescue operations. Communication satellites ensured continuous connectivity, prioritizing emergency communication services to support coordination and assistance efforts. Navigation satellites provided precise positioning and navigation assistance, guiding search and rescue teams and facilitating the evacuation of affected populations.
                Despite challenges such as communication disruptions and adverse weather conditions, the Satellite Emergency Response System demonstrated resilience and effectiveness in providing critical support during this disaster. Moving forward, the insights gained from this experience will inform future improvements and optimizations to enhance the system's capabilities for mitigating the impact of natural disasters and protecting vulnerable communities.
                -------------------------
                """),
            agent=agent,
            context=context,
        )
        
    def report_collating_task(self, agent, disaster, report, context):
        return Task(
            description=dedent(f"""
                Disaster situation: {disaster}
                Live reports from the scene as they come back from the front lines: {report}
                Mission:
                Refer to the report of the 'Post-disaster Recorder' and the report from the front lines,
                compile a chronological post-disaster emergency response report (events).
                Format requirement:
                - Create an event node at a moment when there is satellite coverage, and list all satellite reports at that moment in sequence.
                - Each event node starts with the exact time and distance from the moment it occurred, and ends with over.
                - The evolution of the disaster is in italics and placed at the beginning of the event node (if any).
                - If the satellite operating status changes, list it in the event node with exclamation marks on the left and right sides.
                - Be sure to add the time interval from the disaster to each time.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                A chronological post-disaster emergency response report, in standard markdown format
                \n[Below is an example]
                -------------------------
                # Wenchuan earthquake satellite emergency reporting (events)
                ---
                ------------------------- *[11: 15 (occurring time)]* -------------------------
                *The underground rock mass fractures and dislocates, and seismic waves reach the surface*
                    **Earth Observation Satellite**
                "Buildings and trees began to shake."
                "People are in panic, trying to escape from the buildings."
                    **Weather Monitoring Satellite**
                "The sky is clouded over."
                    **Communication Satellite**
                "Minor disturbances occur."
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 19 (4 minutes after)]* -------------------------
                    **Earth Observation Satellite**
                "Survivors fleeing on foot, seeking shelter in open spaces."
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 25 (10 minutes after)]* ------------------------
                *Aftershocks occurred on the ground, accompanied by strong earthquakes*
                    **Earth Observation Satellite**
                "Buildings collapse, roads destroyed, infrastructure severely damaged."
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 30 (15 minutes after)]* ------------------------
                    **Weather Monitoring Satellite**
                "Light rain, heavy fog, and low visibility affect the evacuation of people and rescue in disaster areas."
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 35 (20 minutes after)]* ------------------------
                    **Communication Satellite**
                "Communication channels overloaded, intermittent disruptions reported."
                ! Signal interruption due to ground base station damage !
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 37 (22 minutes after)]* ------------------------
                *Aftershocks occur again*
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 40 (25 minutes after)]* ------------------------
                    **Communication Satellite**
                "Emergency hotlines established for affected populations to request assistance."
                ! Signal returns to normal !
                -------------------------------------- *[over]* --------------------------------------
                
                ------------------------- *[11: 45 (30 minutes after)]* ------------------------
                    **Navigation Satellite**
                "Precise positioning data provided to guide search and rescue teams to affected areas."
                -------------------------------------- *[over]* --------------------------------------
                ......
                ......
                -------------------------
                """),
            agent=agent,
            context=context,
        )