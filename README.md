<h1 align="center"> Lecture2Notes 📑</h1>

<p> Implementing a program that takes continues voice input and then write it in a text file which converted in
PDF notes. And then the notes can be distributed among the students.</p>

<h2> Modules Required ~ </h2>


  ```sh
     pip install SpeechRegonition
     pip install PyAudio
     pip install fpdf
 ```

<p><b><a href="#">Note ~ </a></b>

> Teacher must wears a headset or a Bluetooth headphones. And the Audio Input of the Laptop \ PC must set to headphones. So the Program can work perfectly</p>

<h2> How it works </h2>

<p><b>Step 1 : </b> First the program starts by importing the required modules</p>

  ```py
     import speech_recognition as sr
     from fpdf import FPDF
 ```


<p><b>Step 2 : </b>Then we have a function named Listen() that listen to teachers words. </p>

  ```py
     def listen(): 
     r = sr.Recognizer() 
     with sr.Microphone() as source: 
         r.adjust_for_ambient_noise(source) 
         audio = r.listen(source) 
     try: 
         query = r.recognize_google(audio, language='en-in') 
         query = query.lower() 
     except Exception as e: 
         print(e) 
         print("Unable to recognize") 
         return "none" 
  
     return query
 ```


<p><b>Step 3 : </b> </p>

  ```py
     pip install SpeechRegonition
     pip install PyAudio
 ```



<p><b>Step 4 : </b> </p>

  ```py
     pip install SpeechRegonition
     pip install PyAudio
 ```


<p><b>Step 5 : </b> </p>

  ```py
     pip install SpeechRegonition
     pip install PyAudio
 ```


