import cv2
import face_recognition
import pickle
import os
from datetime import datetime

def register():
    name = input("이름 입력: ")
    cap = cv2.VideoCapture(0)
    print("카메라 보고 있기~ 3초 후 촬영")
    cv2.waitKey(3000)
    ret, frame = cap.read()
    encoding = face_recognition.face_encodings(frame)[0]
    with open("faces.pkl", "ab") as f:
        pickle.dump((name, encoding), f)
    cap.release()
    print(f"{name}님 등록 완료!")

# 출석 체크
def check_attendance.py
def check():
    if not os.path.exists("faces.pkl"):
        print("등록된 얼굴 없음. 먼저 등록하세요!")
        return
    
    known = []
    names = []
    with open("faces.pkl", "rb") as f:
        while True:
            try:
                name, enc = pickle.load(f)
                known.append(enc)
                names.append(name)
            except:
                break
    
    cap = cv2.VideoCapture(0)
    print("출석 체크 시작! 카메라 보세요 (ESC로 종료)")
    
    while True:
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, locations)
        
        for (top, right, bottom, left), enc in zip(locations, encodings):
            matches = face_recognition.compare_faces(known, enc)
            name = "모르는 사람"
            if True in matches:
                idx = matches.index(True)
                name = names[idx]
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("attendance.txt", "a", encoding="utf-8") as f:
                    f.write(f"{now} - {name} 출석\n")
                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 3)
                cv2.putText(frame, f"{name} 출석!", (left, top-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 2)
            else:
                cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 3)
        
        cv2.imshow("AI 출석부 - ESC 종료", frame)
        if cv2.waitKey(1) == 27: break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("=== AI 얼굴 인식 출석부 ===")
    choice = input("1. 얼굴 등록  2. 출석 체크 : ")
    if choice == "1":
        register()
    else:
        check()