from tkinter import *
import tkinter as tk 

from PIL import Image,ImageTk

root=Tk()
root.geometry('1380x750')
root.title("SUMMARIZATION")
load=Image.open('D:\\SEM6PROJECT\\sumenv\\image\\bg.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
root.configure(bg='#000000')
summary=""

def summm():
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    text = ent.get(1.0,"end-1c")
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
                freqTable[word] = 1
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                          sentenceValue[sentence] += freq
                    else:
                         sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
        average = int(sumValues / len(sentenceValue))
        summary = ''
    for sentence in sentences:
         if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.10 * average)):
             summary += " " + sentence
    sumlabel=Label(root,font=("Times New Roman",16),text=str(summary),bg='White',fg='Red',wraplength=950,justify=LEFT).place(x=350,y=350)
    from googletrans import Translator
    translator = Translator()
    #you can specify the translate languege
    result1 = translator.translate(summary,dest='hi')
    translabel=Label(root,font=(16),wraplength=950,justify=LEFT,text=result1.text,bg='white',fg='Dark Blue').place(x=350,y=500)
    return summary

def aud():
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    text = ent.get(1.0,"end-1c")
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
                freqTable[word] = 1
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                          sentenceValue[sentence] += freq
                    else:
                         sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
        average = int(sumValues / len(sentenceValue))
        summary = ''
    for sentence in sentences:
         if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.10 * average)):
             summary += " " + sentence
    import gtts
    from playsound import playsound
    # make request to google to get synthesis
    tts = gtts.gTTS(summary)
    nameau=ent1.get(1.0,"end-1c")
    tts.save(nameau+".mp3")# play the audio file
    playsound(nameau+".mp3")

title_label=Label(text='''TEXT SUMMARY''',bg='Red',font=("Times New Roman",60,"bold"),borderwidth=3,relief=SUNKEN,padx=335)
title_label.place(x=10,y=10)

text_label=Label(text='''ENTER YOUR TEXT:''',bg="#AFEEEE",font=("Times New Roman",20,"bold")).place(x=40,y=150)
ent=Text(root,width=85,height=8,font=("Times New Roman",13),bg='white',fg='Black')
ent.place(x=350,y=120)


#text.pack()
text_label1=Label(text='''SUMMARIZED TEXT:''',bg="#AFEEEE",font=("Times New Roman",20,"bold")).place(x=40,y=350)
b1=Button(root,text="SUBMIT",bg="green",command=summm,font=("Times New Roman",20,"bold"),borderwidth=3).place(x=1220,y=250)
text_label2=Label(text='''TRANSALATED TEXT:''',bg="#AFEEEE",font=("Times New Roman",20,"bold")).place(x=40,y=500)

text_label3=Label(text='''NAME THE AUDIO FILE''',font=("Times New Roman",20)).place(x=40,y=640)
ent1=Text(root,width=30,height=2,font=("Times New Roman",15))
ent1.place(x=350,y=640)
b3=Button(root,text="PLAY NOW",bg="green",command=aud,font=("Times New Roman",15)).place(x=660,y=640)



root.mainloop()
