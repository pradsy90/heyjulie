import time
import recognizevoice
import multiprocessing
import os
from datetime import datetime

def launchjulie(glblvrbllist,glblvrbldict):

    glblvrbllist.append("Item #1 - Basic Chat Open")
    glblvrbldict['Item #1'] = 'Basic Chat Open'

    filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")

    p2 = multiprocessing.Process(target = basicchatopen, args=(glblvrbllist,glblvrbldict))
    p2.start()

    glblvrbllist.append("Item #2 - Call Recognize Open")
    glblvrbldict['Item #2'] = 'Call Recognize Open'
    p3= multiprocessing.Process(target = callrecognize, args=(glblvrbllist,glblvrbldict))
    p3.start()
    for i in range(100):
            time.sleep(5)
            #for i in range(len(glblvrbllist)):
            #    if(i>-1):
            #        print("variable : " + str(i) + " - " + glblvrbllist[i])
            #print("Questions")
            #print(glblvrbldict['question'])
            #print("---------------------")
            #print("Answers")
                #print(glblvrbldict['answer'])
            print(glblvrbldict['transcript'])
            try:
                with open("C:\\Users\\pradhip.swaminathan\\IdeaProjects\\heyjulie\\chatlogs\\"+filename1+".txt", "w+") as f:

                    # Do whatever with f
                    f.write(glblvrbldict['transcript'])
                    f.close()
            except:
                print("Found Exception")
    p2.join()
    p3.join()



def basicchatopen(glblvrbllist,glblvrbldict):

    #os.system('"dir C:\\Users\\pradhip.swaminathan\\IdeaProjects\\heyjulie"')
    #os.system('"streamlit run basicchatwindow.py"')

    # Perform some calculations
    print("Inside Basic chat open")
    print("got an incoming variable " + str(glblvrbllist[0]))
    result = "Item #3 - End of basic chat open"

    # Append the result to the shared list
    glblvrbllist.append(result)
    glblvrbldict['Item #3'] = 'End of basic chat open'

def callrecognize(glblvrbllist,glblvrbldict):

    print("Inside Call Recognize")
    #print("got an incoming variable " + str(glblvrbllist[1]))
    #result = "Item #4 - End of basic call recognize"
    question=""
    answer=""
    transcript="Start of Transcript"+"\n"+"------------"+"\n"

    #Append the result of shared list
    glblvrbllist.append(question)
    glblvrbldict['question'] = ''
    glblvrbllist.append(answer)
    glblvrbldict['answer'] = ''
    glblvrbldict['transcript']=transcript
    recg1=recognizevoice.recognizevoice(glblvrbllist,glblvrbldict)
    #recg1.speech_recognize_keyword_locally_from_microphone(glblvrbllist,glblvrbldict)
    recg1.recog_kywrd(glblvrbllist,glblvrbldict)


if __name__ == '__main__':
    glblvrbllist = multiprocessing.Manager().list()
    glblvrbldict= multiprocessing.Manager().dict()
    p1 = multiprocessing.Process(target = launchjulie, args=(glblvrbllist,glblvrbldict))
    p1.start()
    i=0
    while (True):
        i=i+.005

