import requests
from datetime import datetime
import pytz
import os

def sync_info():
    url = "https://api.github.com/repos/buaa-ysw/Satellite-Dispatch"

    try:
        response = requests.get(url)
        data = response.json()

        pushed_at = data["pushed_at"]
        pushed_at = datetime.fromisoformat(pushed_at[:-1]) # 解析时间字符串并将其转换为datetime对象
        pushed_at_utc = pushed_at.replace(tzinfo=pytz.utc) # 将datetime对象的时区设置为UTC
        pushed_at_cst = pushed_at_utc.astimezone(pytz.timezone('Asia/Shanghai')) # 将UTC时间转换为中国标准时间
        build_time = pushed_at_cst.strftime('%Y-%m-%d %H:%M:%S') + " (CST)"
    
    # 获取'name'，并设置name_title
        name_title = data.get("name", "Satellite Dispatch [Error]") # 如果字典 data 中包含键 "name"，则它返回相应的值。如果字典中不存在键 "name"，那么它将返回第二个参数提供的默认值
    
    except Exception as e:
        build_time = "Error: " + str(e)
        name_title = "Satellite Dispatch [Error]"
    return build_time,name_title

build_time, name_title = sync_info()




from nicegui import ui

dark = ui.dark_mode()

from init import output_path

# https://fonts.google.com/icons?icon.set=Material+Icons


with ui.left_drawer(value=False, bordered=True).style('background-color: #ebf1fa').props('bordered') as ui_left_drawer:
    ui.button('Dash Board').props('flat color=black')
    ui.button('Playground').props('flat color=black')
    ui.button('Gallery').props('flat color=black')

with ui.footer().style('background-color: #3874c8') as ui_footer:
    ui.label('Last build: ').props('color=white')
    ui.label(build_time).props('color=white')

def on_expansion():
    if dark.value:
        if sim_expansion.value:
            sim_expansion.style('background-color: #343434')
        else:
            sim_expansion.style('background-color: transparent')
        if dis_expansion.value:
            dis_expansion.style('background-color: #343434')
        else:
            dis_expansion.style('background-color: transparent')
    else:
        if sim_expansion.value:
            sim_expansion.style('background-color: #f0f0f0')
        else:
            sim_expansion.style('background-color: transparent')
        if dis_expansion.value:
            dis_expansion.style('background-color: #f0f0f0')
        else:
            dis_expansion.style('background-color: transparent')

with ui.splitter(value=12).classes('w-full h-full') as splitter:
    with splitter.before:
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            dash_board = ui.tab('Dash Board', icon='dashboard')
            playground = ui.tab('Playground', icon='terminal')
            galley = ui.tab('Galley', icon='browse_gallery')
            settings = ui.tab('Settings', icon='settings')

    with splitter.after:
        with ui.tab_panels(tabs, value=dash_board).props('vertical').classes('w-full h-full'):

            #---------------------------------------------------------------------------------------------------------------------------------------------------#

            with ui.tab_panel(dash_board):
                # ui.label('Dash Board').classes('text-h4')
                ui.label('Content of Dash Board')
            
            #---------------------------------------------------------------------------------------------------------------------------------------------------#
                
            with ui.tab_panel(playground):
                with ui.expansion('Simulation', icon='token', on_value_change=on_expansion).classes('w-full') as sim_expansion:
                    options = ['Earthquake', 'Typhoon', 'Awesome']
                    with ui.input(label='Input a Disaster', placeholder='start typing', autocomplete=options).classes('w-full') as sim_input:
                        ui.button(icon='clear', on_click=lambda: sim_input.set_value(None)).props('flat color=warning').bind_visibility_from(sim_input, 'value')
                        ui.button(icon='send').props('flat color=primary').bind_visibility_from(sim_input, 'value')

                with ui.expansion('Dispatch', icon='psychology', on_value_change=on_expansion).classes('w-full') as dis_expansion:
                    ui.label('inside the expansion')

            #---------------------------------------------------------------------------------------------------------------------------------------------------#
                    
            with ui.tab_panel(galley):
                ui.label('Galley').classes('text-h6')
                ui.label('History of Satellite-Dispatch processing...')
                
                # 获取output_path路径下的所有文件夹
                folders = [folder for folder in os.listdir(output_path) if os.path.isdir(os.path.join(output_path, folder))]

                # 为每个文件夹创建一个ui.expansion
                for folder in folders:
                    with ui.expansion(folder, icon='folder').classes('w-full'):
                        # 获取output_path + folder文件夹下的所有文件
                        folder_path = os.path.join(output_path, folder)
                        files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
                        # 为每个文件创建一个ui.expansion
                        for file in files:
                            file_path = os.path.join(folder_path, file)
                            file_extension = os.path.splitext(file)[1]
                            if file_extension == '.md':
                                icon = 'summarize'
                            elif file_extension == '.txt':
                                icon = 'text_snippet'
                            else:
                                icon = 'file'
                                pass
                            # Add file content here
                            
                            with open(file_path, 'r') as f:
                                content = f.read()
                            with ui.expansion(file, icon=icon).classes('w-full'):
                                ui.markdown(content)

            #---------------------------------------------------------------------------------------------------------------------------------------------------#
                
            with ui.tab_panel(settings):
                # ui.label('Settings').classes('text-h4')
                ui.label('Content of settings')

class DarkButton(ui.button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._state = False
        self.props('flat color=white no-border')
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        self._state = not self._state
        dark.toggle()
        self.update()

    def update(self) -> None:
        self.props(f'icon={"dark_mode" if self._state else "light_mode"}')
        ui_header.style(f'background-color: {"#1f4e88" if self._state else "#3874c8"}')
        ui_footer.style(f'background-color: {"#1f4e88" if self._state else "#3874c8"}')
        ui_left_drawer.style(f'background-color: {"#b0b9cf" if self._state else "#ebf1fa"}')
        on_expansion()
        # self.props(f'color={"grey" if self._state else "white"}')
        super().update()

with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between') as ui_header:
    ui.button(on_click=lambda: ui_left_drawer.toggle(), icon='menu').props('flat color=white')
    ui.label(name_title).classes('text-h5 bold')
    ui.space()
    # ui.button(icon='dark_mode', on_click=lambda: dark.toggle()).props('flat color=white no-border')
    DarkButton('')

ui.run()