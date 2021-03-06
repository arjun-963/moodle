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


#Addng CS1A Class details
cs1a = aclass()
cs1a.addSub(['1st Year Basic Civil Engineering C1A','https://meet.google.com/cqi-jquf-enk','http://moodle.mec.ac.in/course/view.php?id=315'])
cs1a.addSub(['BASIC MECHANICAL ENGINEERING CSA','https://meet.google.com/zki-opyw-dfq','http://moodle.mec.ac.in/course/view.php?id=288'])
cs1a.addSub(['CYL120, Engineering Chemistry Lab, CSA','https://meet.google.com/vws-pjfo-nok','http://moodle.mec.ac.in/course/view.php?id=252'])
cs1a.addSub(['Engineering Chemistry, CYT 100, CSA','https://meet.google.com/vws-pjfo-nok','http://moodle.mec.ac.in/course/view.php?id=248'])
cs1a.addSub(['ENGINEERING GRAPHICS-CSA','http://meet.google.com/osf-zwzb-pwc','http://moodle.mec.ac.in/course/view.php?id=296'])
cs1a.addSub(['LIFE SKILL-CSA_Raheena','https://meet.google.com/zik-rsyr-ptq','http://moodle.mec.ac.in/course/view.php?id=254'])
cs1a.addSub(['LIFE SKILL-CSA_Madhu','http://meet.google.com/div-mdjr-ykb','http://moodle.mec.ac.in/course/view.php?id=254'])
cs1a.addSub(['MAT 101 LINEAR ALGEBRA AND CALCULUS -CS A/CS B/ME','https://meet.google.com/suv-anxy-ssw','http://moodle.mec.ac.in/course/view.php?id=185'])
cs1a.addSub(['1st Year Basic Civil LAB Engineering C1A','https://meet.google.com/ukt-txfm-iir','http://moodle.mec.ac.in/course/view.php?id=315'])

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
