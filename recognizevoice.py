import azure.cognitiveservices.speech as speechsdk
import speech2text
import texttospeech
import chat
from datetime import datetime
from playsound import playsound


class recognizevoice():
    # override the constructor of thread/process
    def __init__(self,glblvrbllist,glblvrbldict):
        # first execute the base constructor
        #Thread.__init__(self)
        # now store the additional value you need in this class
        self.secdelay = 5
        self.question=glblvrbldict['question']
        self.answer=glblvrbldict['answer']
        self.transcript=glblvrbldict['transcript']
        #self.glblvrbllist=glblvrbllist

        #print ("Initialing variable... Looping through a Global Variable List")
        #for i in range(len(glblvrbllist)):
        #    print("Came in with variables : " + glblvrbllist[i])

    #override the run function of thread/process
    #def run(self):
    #    self.speech_recognize_keyword_locally_from_microphone()

    def recog_kywrd(self,glblvrbllist,glblvrbldict):
        speechregenabled=texttospeech.convert("Voice Recognition enabled")
        speechregenabled.readout()
        #print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time voice regn enabled\n"))
        # Creates an instance of a keyword recognition model. Update this to
        # point to the location of your keyword recognition model.
        #model = speechsdk.KeywordRecognitionModel("c:\\cutover\\ccHouston_0217.table")
        model=speechsdk.KeywordRecognitionModel("C:\\cutover\HeyHouston_02212023.table")
        # The phrase your keyword recognition model triggers on.
        keyword = "Hey Houston"

        # Create a local keyword recognizer with the default microphone device for input.
        keyword_recognizer = speechsdk.KeywordRecognizer()
        done = False
        #print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time after setting up KeyWord Recognizer \n"))
        def recognized_cb(evt):
            # Only a keyword phrase is recognized. The result cannot be 'NoMatch'
            # and there is no timeout. The recognizer runs until a keyword phrase
            # is detected or recognition is canceled (by stop_recognition_async()
            # or due to the end of an input file or stream).
            result = evt.result
            if result.reason == speechsdk.ResultReason.RecognizedKeyword:
                print("RECOGNIZED KEYWORD: {}".format(result.text))
            nonlocal done
            done = True

        def canceled_cb(evt):
            result = evt.result
            if result.reason == speechsdk.ResultReason.Canceled:
                print('CANCELED: {}'.format(result.cancellation_details.reason))
            nonlocal done
            done = True

        # Connect callbacks to the events fired by the keyword recognizer.
        keyword_recognizer.recognized.connect(recognized_cb)
        keyword_recognizer.canceled.connect(canceled_cb)
        recogctr=0
        while (recogctr<5):
            # Start keyword recognition.
            result_future = keyword_recognizer.recognize_once_async(model)
            print('Say something starting with "{}" followed by whatever you want...'.format(keyword))
            print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is when you can really speak\n"))
            result = result_future.get()

            # Read result audio (incl. the keyword).
            if result.reason == speechsdk.ResultReason.RecognizedKeyword:
                playsound('C:\\Users\\pradhip.swaminathan\\IdeaProjects\\heyjulie\\ding.mp3')
                print ("Recording started for transcription after keyword recognition")
                #print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the record start time \n"))
                strrecgzd=speech2text.from_mic()
                print ("Recording stopped for transcription after keyword recognition")
                print(strrecgzd)
                self.question=self.question+"\n"+strrecgzd
                self.transcript=self.transcript+"\n"+"------------"+"\n"+strrecgzd
                #scantask.email(scantask.tapwithoutchecks(self.strrecgzd, logfilename))
                #print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the record end time \n"))


                print ("Now asking this question to Chat GPT")
                answertoqn=chat.return_answer(strrecgzd)
                self.answer=self.answer+"\n"+answertoqn
                self.transcript=self.transcript+"\n"+"------------"+"\n"+answertoqn
                speechregenabled=texttospeech.convert(answertoqn).readout()
                glblvrbllist.append(str(strrecgzd))
                glblvrbldict['question'] =self.question
                glblvrbldict['answer'] =self.answer
                glblvrbldict['transcript'] =self.transcript

                # If active keyword recognition needs to be stopped before results, it can be done with
            #
            #   stop_future = keyword_recognizer.stop_recognition_async()
            #   print('Stopping...')
            #   stopped = stop_future.get()
            #print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time getting out \n"))
            recogctr=recogctr+1



    def speech_recognize_keyword_locally_from_microphone(self,glblvrbllist,glblvrbldict):
        y=0

        while(y<3):
            print ("the value of y is " + str(y))
            try:
                #print ("Starting y loop")
                #"""runs keyword spotting locally, with direct access to the result audio"""
                #speechregenabled=texttospeech.convert("Voice Recognition enabled. Please say Hey Houston followed by whatever text you need.")
                speechregenabled=texttospeech.convert("Voice Recognition enabled")
                speechregenabled.readout()
                print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time it enabled\n"))
                x=0
                while(x<1):
                    print ("Starting x loop")
                #while(True):

                    #while(x<10):
                    print(str(x) + " is the value of x")
                    print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time inside the function \n"))

                    # Creates an instance of a keyword recognition model. Update this to
                    # point to the location of your keyword recognition model.
                    #model = speechsdk.KeywordRecognitionModel("c:\\cutover\\ccHouston_0217.table")
                    model=speechsdk.KeywordRecognitionModel("C:\\cutover\HeyHouston_02212023.table")
                    # The phrase your keyword recognition model triggers on.
                    keyword = "Hey Houston"

                    # Create a local keyword recognizer with the default microphone device for input.
                    keyword_recognizer = speechsdk.KeywordRecognizer()
                    done = False
                    print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time after setting up KeyWord Recognizer \n"))
                    def recognized_cb(evt):
                        # Only a keyword phrase is recognized. The result cannot be 'NoMatch'
                        # and there is no timeout. The recognizer runs until a keyword phrase
                        # is detected or recognition is canceled (by stop_recognition_async()
                        # or due to the end of an input file or stream).
                        result = evt.result
                        if result.reason == speechsdk.ResultReason.RecognizedKeyword:
                            print("RECOGNIZED KEYWORD: {}".format(result.text))
                        nonlocal done
                        done = True

                    def canceled_cb(evt):
                        result = evt.result
                        if result.reason == speechsdk.ResultReason.Canceled:
                            print('CANCELED: {}'.format(result.cancellation_details.reason))
                        nonlocal done
                        done = True

                    # Connect callbacks to the events fired by the keyword recognizer.
                    keyword_recognizer.recognized.connect(recognized_cb)
                    keyword_recognizer.canceled.connect(canceled_cb)


                    # Start keyword recognition.
                    result_future = keyword_recognizer.recognize_once_async(model)
                    print('Say something starting with "{}" followed by whatever you want...'.format(keyword))
                    print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is when you can really speak\n"))
                    result = result_future.get()

                    # Read result audio (incl. the keyword).
                    if result.reason == speechsdk.ResultReason.RecognizedKeyword:
                        print ("Recording started for transcription after keyword recognition")
                        print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the record start time \n"))
                        self.strrecgzd=speech2text.from_mic()
                        self.incomingtransln=self.incomingtransln+"\n"+self.strrecgzd
                        #scantask.email(scantask.tapwithoutchecks(self.strrecgzd, logfilename))
                        print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the record end time \n"))
                        print ("Recording stopped for transcription after keyword recognition")
                        print(self.strrecgzd)
                        glblvrbllist.append(str(self.strrecgzd))
                        glblvrbldict['TranslatedLines'] =self.incomingtransln

                        # If active keyword recognition needs to be stopped before results, it can be done with
                    #
                    #   stop_future = keyword_recognizer.stop_recognition_async()
                    #   print('Stopping...')
                    #   stopped = stop_future.get()
                    print((datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))+(" is the time getting out \n"))
                    x=x+1


                speechregenabled=texttospeech.convert("Voice Recognition ended.")
                speechregenabled.readout()
                print("Out of X loop")
            except (NotImplementedError):
                print("Caught it.... This was missing")
            print("Out of try loop")
            y=y+1
        print("Out of Y loop")