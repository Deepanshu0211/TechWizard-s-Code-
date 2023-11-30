from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import speech_recognition as sr
import subprocess  # Import subprocess for running external commands

class VoiceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen_manager = ScreenManager()

        # Main Screen
        main_screen = Screen(name='main')
        layout = MDBoxLayout(orientation='vertical', padding=50)

        # Simulated Toolbar
        toolbar = MDBoxLayout(orientation='horizontal', adaptive_height=True)
        toolbar.add_widget(MDRaisedButton(text='Voice Assistant', size_hint_x=None, width=300))
        layout.add_widget(toolbar)

        button = MDRaisedButton(text="Tap and Speak", pos_hint={'center_x': 0.5})
        button.bind(on_press=self.listen_to_voice)
        layout.add_widget(button)

        # Add MDLabel for displaying response
        self.response_label = MDLabel(text="", halign='center', theme_text_color="Secondary")
        layout.add_widget(self.response_label)

        main_screen.add_widget(layout)
        self.screen_manager.add_widget(main_screen)

        return self.screen_manager

    def listen_to_voice(self, instance):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Custom Commands
            if "change song" in text.lower() and "spotify" in text.lower():
                self.change_spotify_song()
            elif "open whatsapp" in text.lower():
                self.open_whatsapp()
            else:
                self.respond("I didn't understand that.")

        except sr.UnknownValueError:
            print("Sorry, couldn't understand.")
            self.respond("I couldn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            self.respond("There was an error processing your request.")

    def change_spotify_song(self):
        # Specify the correct path to Spotify executable
        spotify_path = r"C:\Users\dy323\AppData\Roaming\Spotify\Spotify.exe"

        # Simulate key press for changing Spotify song
        subprocess.Popen([spotify_path])
        self.respond("Changing Spotify song.")

    def open_whatsapp(self):
        # Simulate key press for opening WhatsApp (assuming it's on the desktop)
        subprocess.Popen(["C:\\Users\\dy323\\AppData\\Roaming\\WhatsApp\\WhatsApp.exe"])
        self.respond("Opening WhatsApp.")

    def respond(self, text):
        # Schedule the label update after a short delay
        Clock.schedule_once(lambda dt: setattr(self.response_label, 'text', text))

if __name__ == '__main__':
    VoiceApp().run()
