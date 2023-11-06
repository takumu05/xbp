import japanize_kivy
import urllib.parse
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser
kivy.require('1.11.1')

class HotelReservationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.location_input = TextInput(hint_text='目的の場所')
        self.check_in_input = TextInput(hint_text='チェックイン日（例: 2023-11-04）')
        self.check_out_input = TextInput(hint_text='チェックアウト日（例: 2023-11-07）')
        search_button = Button(text='検索', on_press=self.search_hotels)
        layout.add_widget(self.location_input)
        layout.add_widget(self.check_in_input)
        layout.add_widget(self.check_out_input)
        layout.add_widget(search_button)
        return layout

    def search_hotels(self, instance):
        location = urllib.parse.quote(self.location_input.text.strip())
        check_in_date = self.check_in_input.text.strip()
        check_out_date = self.check_out_input.text.strip()

        if location and check_in_date and check_out_date:
            search_url = 'https://www.trivago.co.jp/'
            webbrowser.open(search_url)

if __name__ == '__main__':
    HotelReservationApp().run()
