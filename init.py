import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

# 从配置文件中读取保存输出的路径
main_output_path = config.get('path', 'main_path')
simulation_output_path = config.get('path', 'simulation_path')

# 从配置文件中读取使用的模型名字 model_name
using_model_name = config.get('models', 'using_model')
simulation_model_name = config.get('models', 'simulation_model')


# 设置到环境变量
os.environ["USING_MODEL"] = using_model_name
os.environ["SIMULATION_MODEL"] = simulation_model_name
os.environ["MAIN_OUTPUT_PATH"] = main_output_path
os.environ["SIMULATION_OUTPUT_PATH"] = simulation_output_path

# 从环境变量中读取
# using_model_name = os.getenv("USING_MODEL")
# simulation_model_name = os.getenv("SIMULATION_MODEL")
# main_output_path = os.getenv("MAIN_OUTPUT_PATH")
# simulation_output_path = os.getenv("SIMULATION_OUTPUT_PATH")