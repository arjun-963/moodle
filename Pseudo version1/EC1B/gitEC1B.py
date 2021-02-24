import pickle
import datetime

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


#Addng EC1B Class details
ec1b = aclass()
ec1b.addSub(['PHT 100 Engineering Physics EC1B','https://meet.google.com/ozb-ijdw-twq','http://moodle.mec.ac.in/course/view.php?id=242'])
ec1b.addSub(['Engineering Physics Lab PHL120','https://meet.google.com/nnt-vcto-ucv','http://moodle.mec.ac.in/course/view.php?id=245'])
ec1b.addSub(['Engineering Electronics, EST130, EC1B','https://meet.google.com/bqz-iage-bob','http://moodle.mec.ac.in/course/view.php?id=265'])
ec1b.addSub(['ENGINEERING MECHANICS EC1B','http://meet.google.com/bfm-oifc-exb','http://moodle.mec.ac.in/course/view.php?id=9'])
ec1b.addSub(['LIFE SKILL-EC1B_Jamshi','https://meet.google.com/vur-ddkq-tsi','http://moodle.mec.ac.in/course/view.php?id=310'])
ec1b.addSub(['LIFE SKILL-EC1B_Madhu','http://meet.google.com/mbx-sbkb-vhm','http://moodle.mec.ac.in/course/view.php?id=241'])
ec1b.addSub(['MAT 101 LINEAR ALGEBRA AND CALCULUS -EC1B','https://meet.google.com/rrt-eybp-ddm','http://moodle.mec.ac.in/course/view.php?id=255'])
ec1b.addSub(['1st Year Basic Electrical Engineering EC1B','https://meet.google.com/osx-zmqq-iko','http://moodle.mec.ac.in/course/view.php?id=302'])
ec1b.addSub(['ESL130 EC1B ELECTRICAL WORKSHOP','https://meet.google.com/bbp-ymvd-cgf','http://moodle.mec.ac.in/course/view.php?id=290'])
ec1b.addSub(['Engineering Electronics Workshop, ESL130, EC1B','https://meet.google.com/bqz-iage-bob','http://moodle.mec.ac.in/course/view.php?id=305'])

#Saving CS1A Details to file
fileObject = open('Subjects.dll','wb')
pickle.dump(cs1a, fileObject)
print('\n done')
fileObject.close()    


#_________TIMETABLE CS1A___________
row = []
cs1aTable = []

row = ['Day','08:30-09:20','09:30-10:20','10:30-11:20','11:30-12:20','12:30-13:20','13:30-15:30']
cs1aTable.append(row)
row = ['Mon','ENGINEERING GRAPHICS-CSA','BASIC MECHANICAL ENGINEERING CSA','Engineering Chemistry, CYT 100','LIFE SKILL-CSA_Raheena','Break','1st Year Basic Civil LAB Engineering C1A']
cs1aTable.append(row)
row = ['Tue','LIFE SKILL-CSA_Madhu','MAT 101 LINEAR ALGEBRA AND CALCULUS -CS A/CS B/ME','MAT 101 LINEAR ALGEBRA AND CALCULUS -CS A/CS B/ME','Engineering Chemistry, CYT 100, CSA','1st Year Basic Civil Engineering C1A','END']
cs1aTable.append(row)
row = ['Wed','Mentoring','BASIC MECHANICAL ENGINEERING CSA','ENGINEERING GRAPHICS-CSA','Engineering Chemistry, CYT 100, CSA','LIFE SKILL-CSA_Raheena','END']
cs1aTable.append(row)
row = ['Thu','MAT 101 LINEAR ALGEBRA AND CALCULUS -CS A/CS B/ME','BASIC MECHANICAL ENGINEERING CSA','Engineering Chemistry, CYT 100, CSA','Mentoring','Break','CYL120, Engineering Chemistry Lab, CSA']
cs1aTable.append(row)
row = ['Fri','1st Year Basic Civil Engineering C1A','MAT 101 LINEAR ALGEBRA AND CALCULUS -CS A/CS B/ME','ENGINEERING GRAPHICS-CSA','ENGINEERING GRAPHICS-CSA','LIFE SKILL-CSA_Madhu','END']
cs1aTable.append(row)
#  ADD MORE DAYS
#print (table[1][1])





#Save Timetable to Timetable csa
timetable = open('timetables.dll','wb')
pickle.dump(cs1aTable,timetable)



# STATUS FILE
# datereal = datetime.datetime.now()
statusclass = openStatus()
# statusclass.updateStatus(dateReal ,"opened:none")

statusfile = open('Status.dll','wb')
pickle.dump(statusclass,statusfile)
statusfile.close()

# statusfile = open('Pseudo version1/Status.dll','rb')
# statusclass2 = pickle.load(statusfile)
# print(statusclass2.lastOpened)
