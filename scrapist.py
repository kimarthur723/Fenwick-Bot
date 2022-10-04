from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Scrapist:
    def __init__(self, start=0) -> None:
        # set up chrome driver
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

        # get room rental website
        self.driver.get('https://gmu.libcal.com/spaces?lid=1205&gid=2117')

        # get the desired start time
        self.start = start

    def find_rooms(self) -> {int: {int: [str]}}:
        # create dict to store information on each room
        # room will be {roomNumber:[time1,time2,time3...]...}
        rooms = {}

        # get a list of cell elements in the table
        cells = self.driver.find_elements(By.CSS_SELECTOR,
                                          '.fc-timeline-events .fc-timeline-event-harness .fc-timeline-event')

        for cell in cells:
            # split the cell title by whitespace
            # cell titles are in the format "hh:mmxm day, Month dd, yyyy - XXXX - XXXX"
            celtit = cell.get_attribute('title').split()
            room_number = int(celtit[6])
            day = int(celtit[3].strip(','))

            if celtit[8] == "Available":
                # with the given room number as a key, initialize a new dict
                if room_number not in rooms:
                    rooms[room_number] = {}
                # with the given date, initialize a new list
                elif day not in rooms[room_number]:
                    rooms[room_number][day] = []
                # add the time to the given day list and room number dict
                else:
                    rooms[room_number][day].append(celtit[0])

    def parse_date(self) -> int:
        # TODO: parse a string in HH:MMxm to some data structure that makes it easier to deal with.
        return

    def get_time_slots(self):
        # TODO: find a room with the most consecutive time slots
        # - time slots have to be concurrent and in the same room.
        # - try to get as close to desired start time.
        # - return a list of
        return

    def reserve_slots(self):
        # TODO: click on the slots, do the duo push, etc.
        return
