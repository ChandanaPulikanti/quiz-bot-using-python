import pyttsx3
import datetime
import csv
import  random

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am QuizBot. Please tell me how can I help you?")
    
    
def quizing_bot():
    wishMe()
    print("lets start the quizing...")
    
    with open("quizbot\sample_quiz_questions.csv",encoding="utf8") as f:
        reader = csv.reader(f)
        quiz_qas = list(reader) 
    score=0
    questionsRight=0
    questionno=1
    for i in range(5):
        n,context,q,qid, a,text = random.choice(quiz_qas)
        data = [q,a,text]    
        question = data[0]
        CorrectAnswer = data[1]

        print("Question #",questionno)
        speak(question)
        print(question)
        answer = input("What is your answer? ")
        if answer == CorrectAnswer:
            print("Correct!")
            score=score+1
            questionsRight=questionsRight+1
            questionno = questionno+1

        else:
            print("Incorrect.")
            print("Correc answer should be: "+CorrectAnswer)
            questionno = questionno+1
        print()

    totalScore = (score / 10) * 100
    print("You got ",score," questions right, and a score of ",totalScore,"%.")
    
quizing_bot()

    

