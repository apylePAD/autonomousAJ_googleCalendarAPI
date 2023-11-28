# autonomousAJ_googleCalendarAPI/run.py
import inquirer
from autonomousAJ_googleCalendarAPI.data.calendars_data import Calendars_Data
from autonomousAJ_googleCalendarAPI.data.colors_data import Colors_Data
from autonomousAJ_googleCalendarAPI.data.events_data import Events_Data

def main_menu():
    questions = [
        inquirer.List("choice",
                      message="What type of data would you like to interact with?",
                      choices=["Calendars", "Colors", "Events", "Exit"]),
    ]
    return inquirer.prompt(questions)["choice"]

def get_calendars_input():
    calendars_processor = Calendars_Data()
    calendars_processor.get_and_process_data()

def get_colors_input():
    colors_processor = Colors_Data()
    colors_processor.get_and_process_data()

def get_events_input():
    events_processor = Events_Data()
    events_processor.get_and_process_data()

def run():
    while True:
        choice = main_menu()
        if choice == "Calendars":
            get_calendars_input()
        elif choice == "Colors":
            get_colors_input()
        elif choice == "Events":
            get_events_input()
        elif choice == "Exit":
            break

if __name__ == "__main__":
    run()