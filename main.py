from init import *
from model import *
from function import save_report_with_name
from agents import SatelliteAgents
from tasks import SatelliteTasks
from simulation import SimulationCrew
import os

class SatelliteCrew:
    def __init__(self, disaster, disaster_name, fold_path, report):
        self.disaster = disaster
        self.disaster_name = disaster_name
        self.fold_path = fold_path
        self.report = report
        self.model = using_model

    def run(self):
        agents = SatelliteAgents()
        tasks = SatelliteTasks()

        # Define agents
        earth_observation_agent = agents.earth_observation_agent()
        weather_monitoring_agent = agents.weather_monitoring_agent()
        communication_agent = agents.communication_agent()
        navigation_agent = agents.navigation_agent()
        recorder_agent = agents.recorder_agent()
        collator_agent = agents.collator_agent()

        # Define tasks
        earth_observation_task = tasks.earth_observation_task(earth_observation_agent, self.disaster, self.report)
        weather_monitoring_task = tasks.weather_monitoring_task(weather_monitoring_agent, self.disaster, self.report)
        communication_task = tasks.communication_task(communication_agent, self.disaster, self.report)
        navigation_task = tasks.navigation_task(navigation_agent, self.disaster, self.report)
        
        context = [earth_observation_task, weather_monitoring_task, communication_task, navigation_task]
        report_writing_task = tasks.report_writing_task(recorder_agent, self.disaster, context)
        
        context = [report_writing_task]
        report_collating_task = tasks.report_collating_task(collator_agent, self.disaster, self.report, context)
        
        # Define crew
        crew = Crew(
            agents=[earth_observation_agent, weather_monitoring_agent, communication_agent, navigation_agent, recorder_agent, collator_agent],
            tasks=[earth_observation_task, weather_monitoring_task, communication_task, navigation_task, report_writing_task, report_collating_task],
            manager_llm=self.model,
            process=Process.sequential,
            verbose=2,
        )

        result = crew.kickoff()
        # save_context_with_name(context, self.report_path, self.disaster_name)
        save_report_with_name(report_writing_task.output.raw_output, result, self.fold_path, self.disaster_name)
        print(crew.usage_metrics)
        return result

def simulate_disaster(disaster):
    simulation = SimulationCrew(disaster=disaster)
    disaster, disaster_name, fold_path, simulation_result = simulation.run()
    return disaster, disaster_name, fold_path, simulation_result

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Satellite Dispatch Here ##")
    print("----------------------------------------")
    disaster = input(dedent("""We will be modelling a satellite scheduling mission following a disaster, please describe in detail the TYPE, SCALE and TIME of the disaster:"""))

    temp_disaster, temp_disaster_name, temp_fold_path, temp_simulation_result = simulate_disaster(disaster)
    satellite_crew = SatelliteCrew(temp_disaster, temp_disaster_name, temp_fold_path, temp_simulation_result)
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
