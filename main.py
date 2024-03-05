import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

from textwrap import dedent
from agents import SatelliteAgents
from tasks import SatelliteTasks
from simulation import SimulationCrew
from dotenv import load_dotenv
load_dotenv()

class SatelliteCrew:
    def __init__(self, disaster):
        self.disaster = disaster
        simulation_report = SimulationCrew(disaster)
        self.report = simulation_report.run()
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.LocalGPT = ChatOpenAI(model="ollama-openhermes", base_url="http://localhost:11434/v1")
        self.Ollama = Ollama(model="openhermes")

    def run(self):
        agents = SatelliteAgents()
        tasks = SatelliteTasks()

        # Define agents
        earth_observation_agent = agents.earth_observation_agent()
        weather_monitoring_agent = agents.weather_monitoring_agent()
        communication_agent = agents.communication_agent()
        navigation_agent = agents.navigation_agent()
        conductor_agent = agents.conductor_agent()
        recoder_agent = agents.recoder_agent()

        # Define tasks
        earth_observation_task = tasks.earth_observation_task(earth_observation_agent, self.disaster, self.report)
        weather_monitoring_task = tasks.weather_monitoring_task(weather_monitoring_agent, self.disaster, self.report)
        communication_task = tasks.communication_task(communication_agent, self.disaster, self.report)
        navigation_task = tasks.navigation_task(navigation_agent, self.disaster, self.report)
        operation_conducting_task = tasks.operation_conducting_task(conductor_agent, self.disaster, self.report)
        
        context = [earth_observation_task, weather_monitoring_task, communication_task, navigation_task, operation_conducting_task]
        report_writing_task = tasks.report_writing_task(recoder_agent, self.disaster, context)
        
        # Define crew
        crew = Crew(
            agents=[earth_observation_agent, weather_monitoring_agent, communication_agent, navigation_agent, conductor_agent, recoder_agent],
            tasks=[earth_observation_task, weather_monitoring_task, communication_task, navigation_task, operation_conducting_task, report_writing_task],
            manager_llm=self.Ollama,
            process=Process.hierarchical,
            verbose=2,
        )

        result = crew.kickoff()
        print(crew.usage_metrics)
        
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Satellite Dispatch Here")
    print("-------------------------------")
    disaster = input(dedent("""We will be modelling a satellite scheduling mission following a disaster, please describe in detail the nature and scale of the disaster:"""))

    satellite_crew = SatelliteCrew(disaster)
    result = satellite_crew.run()
    print("\n\n########################")
    print("## Here is Satellite Dispatch run result:")
    print("########################\n")
    print(result)
