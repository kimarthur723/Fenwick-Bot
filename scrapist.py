from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# set up chrome driver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# get room rental website
driver.get('https://gmu.libcal.com/spaces?lid=1205&gid=2117')

# create dict to store information on each room
# room will be {roomNumber:[time1,time2,time3...]...}
rooms = {}

# get a list of cell elements in the table
cells = driver.find_elements(By.CSS_SELECTOR, '.fc-timeline-events .fc-timeline-event-harness .fc-timeline-event')

for cell in cells:
    # split the cell title by whitespace
    # cell titles are in the format "hh:mmxm day, Month dd, yyyy - XXXX - XXXX"
    celtit = cell.get_attribute('title').split()
    roomNumber = int(celtit[6])
    day = int(celtit[3].strip(','))

    if celtit[8] == "Available":
        # with the given room number as a key, initialize a new dict
        if roomNumber not in rooms:
            rooms[roomNumber] = {}
        # with the given date, initialize a new list
        elif day not in rooms[roomNumber]:
            rooms[roomNumber][day] = []
        # add the time to the given day list and room number dict
        else:
            rooms[roomNumber][day].append(celtit[0])

print(rooms)



while True:
    pass