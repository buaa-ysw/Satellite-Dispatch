from model import *

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
            tools=google_search_tool,
            # tools=[search_tool]
        )

        self.writer = Agent(
            role='Disaster Information Writer',
            goal='Write a series of reasonable events about a disaster.',
            backstory="""You are a writer who specializes in creating narratives about natural disasters. 
                        Your task is to continue to generate more reasonable times, places, and events in this disaster.
                        You will use the information provided by the Disaster Generator and the Disaster Information Analyst,
                        or just create some new resonable information to create detailed messages.
                        The format of each message is like this:
                        # Disaster: XXX
                        [time1] [location1] Buildings collapse, people are trapped.
                        [time2] [location2] Weather changes, weakening communication signals.
                        [time3] [location3] Road destruction, people are in panic.""",
            verbose=True,
            llm=simulation_model,
            allow_delegation=False,
        )
        
    def __create_tasks(self):
        self.task1 = Task(
            description="""{}, Find this kind of natural disasters and analyze documentarys about this.
                Search for a specific disaster event and the occurrence of it, 
                (as many as possible, at least 20 events) give time[xx:xx], locations[], and the events[] that happened.
                including but not limited to people being trapped, weather changes, weakening communication signals, road destruction, and more. 
                Search for a specific disaster event and the occurrence of it,
                give time, location, and the event that happened.
                """.format(self.disaster),
            expected_output="""{}, Find this kind of natural disasters and analyze documentarys about this.
                Search for just one specific disaster event and the occurrence of it, (as many as possible, at least 20 events) give time, location, and the event that happened.
                including but not limited to people being trapped, weather changes, weakening communication signals, road destruction, and more. 
                The format is like this:
                # Disaster: xxx
                [xx:xx] [xx°N, xx°E] XXX hits the city.
                [xx:xx] [xx°N, xx°E] Buildings collapse, people are trapped....""".format(self.disaster),
            agent=self.researcher
        )
        
        self.task2 = Task(
            description="""Generate a series of reasonable events about a disaster.
                        They can be different, but the events should be reasonable, other natural disasters are also acceptable.
                        Using the information from the researcher, generate a series of reasonable events.
                        If it is not enough, you can generate some more reasonable events even it's not real.
                        More details are needed to generate, including but not limited to people being trapped, weather changes, weakening communication signals, road destruction, and more. 
                        more events until the disaster stop or subsides. 
                        the format like this:
                        # Disaster: XXX
                        [09:00] [40.15°N, 116°E] XXX hits the city.
                        [09:15] [40.55°N, 116°E] Buildings collapse, people are trapped.
                        [09:30] [40.85°N, 116°E] Weather changes, weakening communication signals.
                        [09:45] [41.15°N, 116°E] Road destruction, people are in panic.
                        this is just a format, the time and location are just an example.""",
            expected_output="""Using the information from the researcher, generate a series of reasonable events about the disaster. 
                        this is just a format, the time and location are just an example.
                        They can be different, but the events should be reasonable.
                        Using the information from the researcher, generate a series of reasonable events about the disaster.
                        If it is not enough, you can generate some more reasonable events even it's not real.
                        More details are needed to generate, including but not limited to people being trapped, weather changes, weakening communication signals, road destruction, and more. 
                        more events (at least 20 events) until the disaster stop or subsides.
                        the format like this:
                        # Disaster: XXX
                        [time1] [°N, °E] XXX hits the city.
                        [time2] [°N, °E] Buildings collapse, people are trapped.
                        [time3] [°N, °E] Weather changes, weakening communication signals.""",
            agent=self.generator
        )

        self.task3 = Task(
            description="""Write more reasonable events about the disaster.
                        You will use the information provided by the Disaster Generator and the Disaster Information Analyst,
                        must including but not limited to people being trapped, weather changes, weakening communication signals, road destruction, and more.
                        or just create some new resonable information to create a detailed and engaging narrative.
                        The format is like this:
                        # Disaster: XXX
                        [time1] [°N, °E] XXX hits the city.
                        [time2] [°N, °E] Buildings collapse, people are trapped.
                        [time3] [°N, °E] Weather changes, weakening communication signals.
                        """,
            expected_output="""Output at least 20 different time, locations and events, 
                        must be reasonable, and must include the information about people being trapped, weather changes, weakening communication signals, road destruction, and more.
                        the format is like this:
                        # Disaster: XXX
                        [time1] [°N, °E] XXX hits the city.
                        [time2] [°N, °E] Buildings collapse, people are trapped.
                        [time3] [°N, °E] Weather changes, weakening communication signals.""",
            agent=self.writer
        )
        
    def run(self):
        crew = Crew(
            agents=[self.researcher, self.generator, self.writer],
            tasks=[self.task1, self.task2, self.task3 ],
            verbose=2, # You can set it to 1 or 2 to different logging levels
        )
        simulation_result = crew.kickoff()
        return simulation_result

if __name__ == "__main__":
    print("######################")
    print("## Starting Simulation")
    print("######################")

    # input disaster type
    disaster_type = input("Enter the type of disaster: ")

    simulation = SimulationCrew(disaster=disaster_type)
    simulation.run()