from typing import Union
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker, MDColorPicker

class MainApp(MDApp):
    def build(self):
        Window.size = (360, 650)
        return Builder.load_string("""
MDFloatLayout:
	MDRaisedButton:
		text: "Выбрать время"
		pos_hint: {'center_x': .5, 'center_y': .8}
        size_hint: .5, .2
		on_release: app.show_time_picker()
	MDLabel:
		id: time_label
		text: "Выберите время!"
		pos_hint: {'center_x': .75, 'center_y': .65}

	MDRaisedButton:
		text: "Выбрать дату"
		pos_hint: {'center_x': .5, 'center_y': .3}
        size_hint: .5, .2
		on_release: app.show_date_picker()
	MDLabel:
		id: date_label
		text: "Выберите дату!"
		pos_hint: {'center_x': .75, 'center_y': .15}
""")

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.on_cancel_time, on_save=self.on_save_time)
        time_dialog.open()

    def on_save_time(self, instance, time):
        self.root.ids.time_label.text = str(time)
    def on_cancel_time(self, instance, time):
        self.root.ids.time_label.text = "Время не выбрано!"

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_date, on_cancel=self.on_cancel_date)
        date_dialog.open()

    def on_save_date(self, instance, value, date_range):
         self.root.ids.date_label.text = str(value)
    def on_cancel_date(self, instance, value):
        self.root.ids.date_label.text = "Дата не выбрана!"

if __name__ == '__main__':
    MainApp().run()