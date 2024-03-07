from nicegui import ui
# https://fonts.google.com/icons?icon.set=Material+Icons

dark = ui.dark_mode()

# ui.label('CONTENT')
# [ui.label(f'Line {i}') for i in range(100)]

# with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4') as left_drawer:
#     ui.label('LEFT DRAWER')
with ui.left_drawer(value=False, bordered=True).style('background-color: #ebf1fa').props('bordered') as ui_left_drawer:
    ui.button('Dash Board').props('flat color=black')
    ui.button('Playground').props('flat color=black')
    ui.button('Gallery').props('flat color=black')

with ui.footer().style('background-color: #3874c8') as ui_footer:
    ui.label('Last build: ').props('color=white')
    ui.label('2021-10-10').props('color=white')

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
        # self.props(f'color={"grey" if self._state else "white"}')
        super().update()


with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between') as ui_header:
    ui.button(on_click=lambda: ui_left_drawer.toggle(), icon='menu').props('flat color=white')
    ui.label('HEADER')
    ui.space()
    # ui.button(icon='dark_mode', on_click=lambda: dark.toggle()).props('flat color=white no-border')
    DarkButton('')

with ui.splitter(value=12).classes('w-full h-full') as splitter:
    with splitter.before:
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            dash_board = ui.tab('Dash Board', icon='dashboard')
            playground = ui.tab('Playground', icon='terminal')
            galley = ui.tab('Galley', icon='browse_gallery')
            settings = ui.tab('Settings', icon='settings')

    with splitter.after:
        with ui.tab_panels(tabs, value=dash_board) \
                .props('vertical').classes('w-full h-full'):
            with ui.tab_panel(dash_board):
                ui.label('Dash Board').classes('text-h4')
                ui.label('Content of mails')
            with ui.tab_panel(playground):
                ui.label('Playground').classes('text-h4')
                ui.label('Content of alarms')
                                
                with ui.tabs().classes('justify-start') as tabs:
                    one = ui.tab('One')
                    two = ui.tab('Two')
                with ui.tab_panels(tabs, value=one).classes('w-full'):
                    with ui.tab_panel(one):
                        ui.label('First tab')
                        ui.label('CONTENT')
                        [ui.label(f'Line {i}') for i in range(100)]
                    with ui.tab_panel(two):
                        ui.label('Second tab')

            with ui.tab_panel(galley):
                ui.label('Galley').classes('text-h4')
                ui.label('Content of movies')

            with ui.tab_panel(settings):
                ui.label('Settings').classes('text-h4')
                ui.label('Content of settings')

ui.run()