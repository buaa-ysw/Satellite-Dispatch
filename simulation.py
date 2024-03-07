from init import *
from model import *
from function import save_simulation_result_with_name

class SimulationCrew():
    def __init__(self, disaster):
        self.disaster = disaster
        self.__create_agents()
        self.__create_tasks()
        
    def __create_agents(self):
        self.generator = Agent(
            role='Disaster Generator',
            goal='Simulate various events occurring in a natural disaster in chronological order until it stop.',
            backstory="""The Disaster Generator is a narrative tool designed to emulate the unfolding of natural disasters in real-time. 
                        As time progresses, it generates events related to the disaster, including but not limited to people being trapped, 
                        weather changes, weakening communication signals, road destruction, and more. 
                        It simulates the disaster, incrementally progressing its narrative until the disaster stop or subsides.
                        Generate a series of reasonable event about a disaster.
                        They can be different, but the events should be reasonable, other natural disasters are also acceptable.
                        Using the information from the researcher, generate a series of reasonable events.
                        If it is not enough, you can generate some more reasonable events even it's not real.
                        More details are needed to generate, including but not limited to people being trapped, weather changes, weakening communication signals, road destruction, and more. 
                        more events until the disaster stop or subsides. 
                        the format like this:
                        # Disaster: XXX
                        [09:00] [40.15°N, 116°E] XXX hits the city.
                        [09:15] [41.55°N, 117°E] Buildings collapse, people are trapped.
                        [09:30] [40.85°N, 116°E] Weather changes, weakening communication signals.
                        [09:45] [39.15°N, 116°E] Road destruction, people are in panic.
                        this is just a format, the time and location are just an example.""",
            verbose=True,
            llm=simulation_model,
            allow_delegation=False,
            # tools=google_search_tool,
            tools=[search_tool]
        )

        self.researcher = Agent(
            role='Disaster Information Analyst',
            goal='Find and analyze news about this kind of natural disasters and the occurrence of natural disasters',
            backstory="""You work for an international natural disaster data center. 
                        Your expertise lies in sorting out and documenting what happens at every moment and place during natural disasters.
                        You have a rich accumulation of events, understand what happens in various natural disasters, and have a knack for summarizing events.""",
            verbose=True,
            llm=simulation_model,
            allow_delegation=False,
            # tools=google_search_tool,
            tools=[search_tool]
        )

        # self.writer = Agent(
        #     role='Disaster Information Writer',
        #     goal='Write more reasonable events about a disaster.',
        #     backstory="""You are a writer who specializes in creating narratives about natural disasters. 
        #                 Your task is to continue to generate more reasonable times, places, and events in this disaster.
        #                 You will use the information provided by the Disaster Generator and the Disaster Information Analyst,
        #                 or just create some new resonable information to create detailed messages.
        #                 Be as consistent as possible with the content provided by Disaster Generator and maintain authenticity as much as possible.
        #                 The format of each message is like this:
        #                 # Disaster: XXX
        #                 [time1] [location1] Buildings collapse, people are trapped.
        #                 [time2] [location2] Weather changes, weakening communication signals.
        #                 [time3] [location3] Road destruction, people are in panic.""",
        #     verbose=True,
        #     llm=simulation_model,
        #     allow_delegation=False,
        # )
        
    def __create_tasks(self):
        self.task1 = Task(
            description="""Search and Analyze News Related to {} Natural Disasters:
                        - Search for news articles covering various types of natural disasters.
                        - Analyze the news to identify significant events related to the chosen disaster.
                        - Provide detailed accounts of at least 10 events, including time, location, and description.
                        - Ensure accuracy in time, longitude, and latitude details, allowing for fluctuations.
                        - Events may include people being trapped, weather changes, communication disruptions, road destruction, etc.
                        """.format(self.disaster),
            expected_output="""List Detailed Events of {} Disaster:
                            - Provide time, location, and description for at least 10 significant events.
                            - Ensure accuracy in time, longitude, and latitude details.
                            - Include descriptions such as people being trapped, weather changes, communication disruptions, road destruction, etc.
                            Format Example:
                            # Disaster: {}
                            [August 6, 2023, 09:03] [24.8801°N, 114.0579°E] XXX hits the city.
                            [time2] [xx°N, xx°E] Buildings collapse, people are trapped....""".format(self.disaster, self.disaster),
            agent=self.researcher
        )
        
        self.task2 = Task(
            description="""\
                Generate a series of reasonable events about a disaster using information from the researcher. 
                Choose one disaster if there are multiple options. If needed, generate additional events, even if speculative.
                Ensure accuracy in time, longitude, and latitude with reasonable fluctuations within an acceptable range.
                Include details such as people being trapped, weather changes, weakening communication signals, road destruction, etc.

                Tasks:
                - Choose a disaster based on researcher's information.
                - Generate a series of reasonable events (at least 20) until the disaster stops or subsides.

                Format Example:
                # Disaster: XXX (Summarized Title, including the disaster name, location or other.)
                [August 6, 2023, 09:03] [24.8801°N, 114.0579°E] XXX hits the city.
                [time2] [°N, °E] Buildings collapse, people are trapped.
                [time3] [°N, °E] Weather changes, weakening communication signals.
                (This is just a format; time and location are examples.)""",
            expected_output="""\
                A series of at least 20 reasonable events about the chosen disaster,
                ensure accuracy in time, longitude, and latitude with reasonable fluctuations within an acceptable range.
                Include details such as people being trapped, weather changes, weakening communication signals, road destruction, etc.

                Format Example:
                # Disaster: XXX (Summarized Title)
                [August 6, 2023, 09:03] [24.8801°N, 114.0579°E] XXX hits the city.
                [time2] [°N, °E] Buildings collapse, people are trapped.
                [time3] [°N, °E] Weather changes, weakening communication signals.
                (This is just a format; time and location are examples.)""",
            agent=self.generator
        )
        # self.task3 = Task(
        #     description="""Expand content generated by Disaster Generator. According to the content, write new times, locations, and events between events. 
        #                 They must be logical, reasonable, and consistent with the content provided by the Disaster Generator.
        #                 Make sure they include people being trapped, weather changes, weakening communication signals, road destruction, and more.
        #                 The format is the same as the content generated by Disaster Generator.
        #                 """,
        #     expected_output="""An extension of the content generated by the Disaster Generator, 
        #                     adding new events (at least 20, include people being trapped, weather changes, weakening communication signals, road destruction, and more) 
        #                     between events and keeping the format unchanged""",
        #     agent=self.writer
        # )
        
    def run(self):
        crew = Crew(
            agents=[self.researcher, self.generator],
            tasks=[self.task1, self.task2],
            verbose=2, # You can set it to 1 or 2 to different logging levels
        )
        simulation_result = crew.kickoff()
        disaster_name, fold_path = save_simulation_result_with_name(simulation_result, output_path)
        return disaster_name, fold_path, simulation_result

if __name__ == "__main__":
    print("######################")
    print("## Starting Simulation")
    print("######################")

    # input disaster type
    disaster_type = input("Enter the type of disaster: ")

    simulation = SimulationCrew(disaster=disaster_type)
    simulation.run()
    print("######################")
    print("## Simulation Finished")
    print("######################")