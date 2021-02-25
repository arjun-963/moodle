import pickle
import datetime
import time
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import os

###################################
##########   MODIFY   ############
moodleUsername = "moodleusername"
moodlePassword = "moodlepassword"
#################################
#################################


#contains sub name, sub meet link and sub moodle link of one particular batch
class aclass:
    def __init__(self):
        self.subs = []
        
    class sub:
        def __init__(self):
            self.name 
            self.meetlink 
            self.moodlelink

    def addSub(self, sub):
        self.subs.append(sub)


class openStatus:
    def __init__(self):
        self.dateOpened = datetime.datetime.now()
        self.lastOpened = "opened:none"

    def updateStatus(self, dateReal , lastopened):
        self.dateOpened = dateReal
        self.lastOpened = lastopened


def time_in_range(start, end, hour, minute):
    #"""Return true if x is in the range [start, end]"""
    if(start[0]> hour):
        # print("{} > {}".format(start[0], hour))
        return False
    elif(start[0] == hour):
        if(start[1]<= minute):
            return True
    elif(hour < end[0]):
        return True
    elif(hour == end[0]):
        if(minute < end[1]):
            return True
    else:
        return False     


def markMoodle(link):
    ###########################################################
    #                 HERE add path if required
    driver = webdriver.Chrome() 
    #
    ##########################################################
    driver.get(link)
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(moodleUsername)
    password.send_keys(moodlePassword)
    password = driver.find_element_by_id("loginbtn").click()

    wait(driver,50).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Attendance')))
    driver.find_element_by_partial_link_text('Attendance').click()

    wait(driver,50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Submit attendance')))
    driver.find_element_by_link_text('Submit attendance').click()

    wait(driver,50).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Present"]')))
    driver.find_element_by_xpath('//*[text()="Present"]').click()

    wait(driver,50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_submitbutton"]')))
    driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()








timetablefile = open('timetables.dll','rb')
timetable = pickle.load(timetablefile)


dateReal = datetime.datetime.now()

while(1):
    os.system('cls' if os.name == 'nt' else 'clear')
    dateReal = datetime.datetime.now()
    print(dateReal.strftime("%a") + "   " + dateReal.strftime("%H" ) +':'+ dateReal.strftime("%M")+':'+ dateReal.strftime("%S"))
    day = dateReal.strftime("%a")
    i=0
    dayindex = -1

    while(i<6):
        if(timetable[i][0] == day):
            dayindex = i
        i = i+1    

    # print("dayindex:{}".format(dayindex))
    todaytimtable = timetable[dayindex]
    SubjectIndex = -1
    i=1
    # if(dateReal.strftime("%p" ) == 'AM'):
    while(i<7):

        hour = dateReal.strftime("%H" )
        minute = dateReal.strftime("%M")
        # print("hour:{} , minute:{}".format(hour,minute))

        periodtime = timetable[0][i].split('-')
        start = periodtime[0].split(':')  #gives start hour and min as list
        end = periodtime[1].split(':')    #gives end hour and min as list

        
        if(time_in_range(start, end, hour, minute)):
            SubjectIndex = i
            break
        
        i = i+1

            
    if(SubjectIndex == -1):
        print("Noclass Now")
    else:
        subjectFile = open('Subjects.dll','rb')
        subjects = pickle.load(subjectFile)
        print("Now we have: {}".format(timetable[dayindex][SubjectIndex]))  
        i=0  
        while(i<9):
            # print(subjects.subs[i])
            # time.sleep(1)
            sub = subjects.subs[i]
            # print(sub[0])
            # time.sleep(3)

            if(sub[0] == timetable[dayindex][SubjectIndex] ):
                statusfile = open('Status.dll','rb')
                status = pickle.load(statusfile)
                statusfile.close()
                openedStatusSub = "opened:"+ sub[0]
                print(status.lastOpened)
                # time.sleep(1)
                if(status.lastOpened != openedStatusSub ):
                    print("Opening  {}".format(sub[2]))
                    markMoodle(sub[2])
                    statusfile = open('Status.dll','wb')
                    status.lastOpened = openedStatusSub
                    pickle.dump(status,statusfile)
                    statusfile.close()
                
            i=i+1  
    time.sleep(1)          





