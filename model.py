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
model_name = config.get('models', 'using_model')

# 根据配置文件中的模型名字选择使用的模型 using_model
if model_name == 'ollama_openhermes':
    using_model = Ollama(model="openhermes")
elif model_name == 'gpt-3.5-turbo':
    using_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1.0)
    load_dotenv()
else:
    raise ValueError("Unsupported default model name")

# 设置使用的模型到环境变量
os.environ["USING_MODEL"] = model_name