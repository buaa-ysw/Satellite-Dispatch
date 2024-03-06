from crewai import Agent, Task, Crew, Process
from textwrap import dedent

import configparser
import os
from dotenv import load_dotenv

# 模型导入
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

# 从langchain.agents导入工具 google_search_tool
from langchain.agents import Tool
from langchain_community.utilities import GoogleSerperAPIWrapper
os.environ["SERPER_API_KEY"] = "f2262d553f5691749a5420e2a5d3a2b36c84aa62"
search_tool = GoogleSerperAPIWrapper()
google_search_tool=[Tool(name="Google Search", func=search_tool.run, description="Search-based queries")]

# 从配置文件中读取使用的模型名字 model_name
config = configparser.ConfigParser()
config.read('config.ini')
using_model_name = config.get('models', 'using_model')
simulation_model_name = config.get('models', 'simulation_model')

# 根据配置文件中的模型名字选择使用的模型 using_model
if using_model_name == 'ollama_openhermes':
    using_model = Ollama(model="openhermes")
elif using_model_name == 'gpt-3.5-turbo':
    using_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    load_dotenv()
else:
    raise ValueError("Unsupported default model name")

# 根据配置文件中的模型名字选择使用的模拟模型 simulation_model
if simulation_model_name == 'ollama_openhermes':
    simulation_model = Ollama(model="openhermes")
elif simulation_model_name == 'gpt-3.5-turbo':
    simulation_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    load_dotenv()
else:
    raise ValueError("Unsupported simulation model name")

# 设置使用的模型到环境变量
os.environ["USING_MODEL"] = using_model_name
os.environ["SIMULATION_MODEL"] = simulation_model_name