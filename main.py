from model import *
from agents import SatelliteAgents
from tasks import SatelliteTasks
from simulation import SimulationCrew

class SatelliteCrew:
    def __init__(self, disaster):
        self.disaster = disaster
        simulation_report = SimulationCrew(disaster)
        self.report = simulation_report.run()
        self.model = using_model

    def run(self):
        agents = SatelliteAgents()
        tasks = SatelliteTasks()

        # Define agents
        earth_observation_agent = agents.earth_observation_agent()
        weather_monitoring_agent = agents.weather_monitoring_agent()
        communication_agent = agents.communication_agent()
        navigation_agent = agents.navigation_agent()
        recoder_agent = agents.recoder_agent()

        # Define tasks
        earth_observation_task = tasks.earth_observation_task(earth_observation_agent, self.disaster, self.report)
        weather_monitoring_task = tasks.weather_monitoring_task(weather_monitoring_agent, self.disaster, self.report)
        communication_task = tasks.communication_task(communication_agent, self.disaster, self.report)
        navigation_task = tasks.navigation_task(navigation_agent, self.disaster, self.report)
        
        context = [earth_observation_task, weather_monitoring_task, communication_task, navigation_task]
        report_writing_task = tasks.report_writing_task(recoder_agent, self.disaster, context)
        
        # Define crew
        crew = Crew(
            agents=[earth_observation_agent, weather_monitoring_agent, communication_agent, navigation_agent, recoder_agent],
            tasks=[earth_observation_task, weather_monitoring_task, communication_task, navigation_task, report_writing_task],
            manager_llm=self.model,
            process=Process.sequential,
            verbose=2,
        )

        result = crew.kickoff()
        print(crew.usage_metrics)
        
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Satellite Dispatch Here ##")
    print("----------------------------------------")
    disaster = input(dedent("""We will be modelling a satellite scheduling mission following a disaster, please describe in detail the TYPE, SCALE and TIME of the disaster:"""))

    satellite_crew = SatelliteCrew(disaster)
    result = satellite_crew.run()
    print("\n\n---------------------------------------------------")
    print("############################")
    print("## The disaster you input ##")
    print("############################\n")
    print(disaster)
    print("\n\n#####################################")
    print("## Satellite Dispatch run complete ##")
    print("#####################################\n")
    print(result)
