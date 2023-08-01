import cv2
import numpy as np
import face_recognition
import os
from datetime import date
from FaceR.models import AttendanceCS, AttendanceCE, AttendanceME, AttendanceEC
from Account.models import Student
from FaceR import views


Attend = []


class VideoCap(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        path = f'media/{views.org_u.name}'
        print(views.org_u.name)
        self.images = []
        self.classNames = []

        myList = os.listdir(path)
       
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        # print(self.classNames)

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        self.encodeListKnown = findEncodings(self.images)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while True:
            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "/haarcascade_frontalface_default.xml")

            ret, frame = self.video.read()
            gray = cv2.cvtColor(frame, 0)
            detections = face_cascade.detectMultiScale(
                gray, scaleFactor=1.3, minNeighbors=5)
            if (len(detections) > 0):
                (x, y, w, h) = detections[0]
                frame1 = cv2.rectangle(
                    frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            img = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(
                imgS, facesCurFrame)

            # Draw black background rectangle.........................................................
            x1, y1, w1, h1 = 0, 0, 175, 65
            cv2.rectangle(frame, (x1, x1), (x1 + w1, y1+ h1), (0, 0, 0), -1)

            # encode face features...........................................................................
            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(
                    self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(
                    self.encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = self.classNames[matchIndex].upper()
                    # Add text
                    image = cv2.putText(frame, "  Face Matched  ", (x1 + int(w1/10), 37), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
                    # image = cv2.putText(frame,"Face Matched",(50, 50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),2, cv2.LINE_AA)
                    newV = views.org_u
                    if "CS" in name:
                        stud = Student.objects.get(enrollment=name,org=newV)
                        S_Name = stud.name
                        S_branch = stud.branch
                        S_batch = stud.adm_year
                         # put text on focus rect...........
                        if (len(detections) > 0):
                            (x2, y2, w2, h2) = detections[0]
                            image = cv2.putText(
                                    frame, S_Name, (x2,y2-10), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255), 1, cv2.LINE_AA)
                        attend = AttendanceCS.objects.filter(
                            enrollment=name, Date=date.today())
                        #check the attedance of current date is exist or not 
                        if attend:
                            
                            text = "Your attendance is completed or already attended"
                            image = cv2.putText(
                                frame, text, (100, 450), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255), 1, cv2.LINE_AA)
                        else:
                            fm = AttendanceCS(org=newV, name=S_Name, enrollment=name, attendance_date=date.today(
                            ), branch=S_branch, adm_year=S_batch)
                            fm.save()
                    if "ME" in name:
                        stud = Student.objects.get(enrollment=name,org=newV)
                        S_Name = stud.name
                        S_branch = stud.branch
                        S_batch = stud.adm_year
                         # put text on focus rect...........
                        if (len(detections) > 0):
                            (x2, y2, w2, h2) = detections[0]
                            image = cv2.putText(
                                 frame, S_Name, (x2,y2-10), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255), 1, cv2.LINE_AA)
                        attend = AttendanceME.objects.filter(
                            enrollment=name, Date=date.today())
                        #check the attedance of current date is exist or not
                        if attend:
                           
                            text = "Your attendance is completed or already attended"
                            image = cv2.putText(
                                frame, text,  (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,255), 2, cv2.LINE_AA)
                        else:
                            fm = AttendanceME(org=newV, name=S_Name, enrollment=name, attendance_date=date.today(
                            ), branch=S_branch, adm_year=S_batch)
                            fm.save()
                    if "CE" in name:
                        stud = Student.objects.get(enrollment=name,org=newV)
                        S_Name = stud.name
                        S_branch = stud.branch
                        S_batch = stud.adm_year
                         # put text on focus rect...........
                        if (len(detections) > 0):
                            (x2, y2, w2, h2) = detections[0]
                            image = cv2.putText(
                                    frame, S_Name, (x2,y2-10), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255), 1, cv2.LINE_AA)
                        attend = AttendanceCE.objects.filter(
                            enrollment=name, Date=date.today())
                        #check the attedance of current date is exist or not
                        if attend:
                           
                            text = "Your attendance is completed or already attended"
                            image = cv2.putText(
                                frame, text, (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,255), 2, cv2.LINE_AA)
                        else:
                            fm = AttendanceCE(org=newV, name=S_Name, enrollment=name, attendance_date=date.today(
                            ), branch=S_branch, adm_year=S_batch)
                            fm.save()
                    if "EC" in name:
                        stud = Student.objects.get(enrollment=name,org=newV)
                        S_Name = stud.name
                        S_branch = stud.branch
                        S_batch = stud.adm_year
                        if (len(detections) > 0):
                            (x2, y2, w2, h2) = detections[0]
                            image = cv2.putText(
                                    frame, S_Name, (x2,y2-10), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255), 1, cv2.LINE_AA)
                        attend = AttendanceEC.objects.filter(
                            enrollment=name, Date=date.today())
                        #check the attedance of current date is exist or not
                        if attend:
                            
                            text = "Your attendance is completed or already attended"
                            image = cv2.putText(
                                frame, text,  (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,255), 2, cv2.LINE_AA)
                        else:
                            fm = AttendanceEC(org=newV, name=S_Name, enrollment=name, attendance_date=date.today(
                            ), branch=S_branch, adm_year=S_batch)
                            fm.save()

                    # break
                else:
                    # put text on focus rect...........
                    if (len(detections) > 0):
                        (x2, y2, w2, h2) = detections[0]
                        image1 = cv2.putText(frame,"Unknown", (x2,y2-10), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255), 1, cv2.LINE_AA)
                    image = cv2.putText(frame, "Face Not Matched! ", (x1 + int(w1/10), 37), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            ret, jpeg = cv2.imencode('.jpg', frame)

            return jpeg.tobytes()
