import pickle        #for serialising class to store in file
import datetime      # current date-time-day
import time          # time.sleep(seconds)  delay execution
from selenium import webdriver 

from selenium.webdriver.support import expected_conditions as EC   #exception handling? 
from selenium.webdriver.support.ui import WebDriverWait as wait    #wait
from selenium.webdriver.common.by import By
import os                                    #clear terminal might not be required later

##################################
##########   MODIFY   ############
moodleUsername = "yourMoodleUsername"
moodlePassword = "yourMoodlePassword
##################################
##################################


#contains sub name, sub meet link and sub moodle link of one particular batch 
class aclass:
    def __init__(self):
        self.subs = []  #list of subjects : presently expected elements of type list itself

    def addSub(self, sub):        #adds a particular subject to subs list
        self.subs.append(sub)     


#not really required as a class but,
#intended to save status of last opened moodle link also saves last opened time
#problems : will not mark attendance for 2 consecutive periods, works for eg, not for maths....
#modify it
class openStatus:
    def __init__(self):
        self.dateOpened = datetime.datetime.now()
        self.lastOpened = "opened:none"

    def updateStatus(self, dateReal , lastopened):
        self.dateOpened = dateReal
        self.lastOpened = lastopened




def time_in_range(start, end, hour, minute):
    #start, end are start and endtime of a respective class as a list with
    #first element being hour and second element minute
    #start will be like say ['08','35']
    #end will be like say ['09','20']
    #both elements are strings

    #hour, min are present hour and minute in 24 hour format,  strings

    # returns True if in range False otherwise, hopefully
    if(start[0]> hour):
        return False
    elif(start[0] == hour):
        # print(start[0])
        # time.sleep(3)
        if(start[1]<= minute):
            # print('{}<={}'.format(start[1],minute))
            return True
    elif(hour < end[0]):
        return True
    elif(hour == end[0]):
        if(minute < end[1]):
            return True
    else:
        return False     


def markMoodle(link):
    #functions gets moodle link as input, opens chrome and marks moodle 


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







#stores timetable as sort of a matrix
#more bout it in mastersetup
timetablefile = open('timetables.dll','rb')
timetable = pickle.load(timetablefile)

#current date
dateReal = datetime.datetime.now()

#main loop
while(1):
    os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
    dateReal = datetime.datetime.now()      #get current date,time

    #https://www.w3schools.com/python/python_datetime.asp
    print(dateReal.strftime("%a") + "   " + dateReal.strftime("%H" ) +':'+ dateReal.strftime("%M")+':'+ dateReal.strftime("%S"))
    day = dateReal.strftime("%a")  #day => current day

    i=0
    dayindex = -1
    #Finding day index, 1st column of timetable matrix are days of form:"Mon","Tue" etc
    while(i<6):
        if(timetable[i][0] == day):
            dayindex = i
        i = i+1    

    # print("dayindex:{}".format(dayindex))
    todaytimtable = timetable[dayindex]    #day indexth row is that day's timetable, so,
                                           #todaytimetable is today's timtable, format: list of strings,(1st element is day name)


    #going to find which period is active now
    SubjectIndex = -1
    i=1   # i starts at 1 to avoid first column which is day name
    
    #loop through timetable 1st row to match current period time
    # i<7 as there are total 7 columns, including 1st column which is day name
    while(i<7):

        hour = dateReal.strftime("%H" )  # hour and min in 24 hour checkout 
        minute = dateReal.strftime("%M")  #https://www.w3schools.com/python/python_datetime.asp

        #timetable period in format: "8:30-09:20"
        #below code splits it into two parts, 8:30 and 9:30
        #periodtime is a list, 1st element: starttime, 2nd, end time
        periodtime = timetable[0][i].split('-')
        
        #start and end time is split into hour and min and stored in respective lists, start and end
        start = periodtime[0].split(':')  #gives start hour and min as list
        end = periodtime[1].split(':')    #gives end hour and min as list

        
        if(time_in_range(start, end, hour, minute)):
            SubjectIndex = i
            break
        
        i = i+1
    #end of finding which period loop

    #no class => subjectindex =-1        
    if(SubjectIndex == -1):
        print("Noclass Now")
    else:
        subjectFile = open('Subjects.dll','rb')
        subjects = pickle.load(subjectFile)
        print("Now we have: {}".format(timetable[dayindex][SubjectIndex]))  
        i=0  

        #loop thru subject list to find if current subject details available in subject.dll
        #i<9 as there are 9 subjects , will need to change to dynamic variable later
        #9 subject as in subjects having diff moodle links
        while(i<9):
            
            sub = subjects.subs[i]
            if(sub[0] == timetable[dayindex][SubjectIndex] ):

                #loading status file to check if moodle link for subject was already opened
                statusfile = open('Status.dll','rb')
                status = pickle.load(statusfile)
                statusfile.close()

                #setting strin in format to be inserted in status file upon successful attendance marking
                openedStatusSub = "opened:"+ sub[0]
                print(status.lastOpened)
                

                if(status.lastOpened != openedStatusSub ):
                    print("Opening  {}".format(sub[2]))
                    markMoodle(sub[2])
                    #excecutions gets stuck if unable to mark moodle

                    statusfile = open('Status.dll','wb')

                    #assigning last open status to variable upon successful marking
                    status.lastOpened = openedStatusSub
                    pickle.dump(status,statusfile)
                    statusfile.close()
                
            i=i+1  
    time.sleep(1)          





