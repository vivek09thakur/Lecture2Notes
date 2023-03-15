<h1 align="center">📒 Lecture2Notes</h1>

> Converts Words of Teacher into class notes live!
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


<p><b>Step 3 : </b>In the main loop , We have opened a text file in active mode in which we can write the recognised words of the teacher. </p>

  ```py
     while True: 
     with open("notes.txt", "a") as f: 
         data = listen().lower() 
         f.write(f"{data}\n") 
         pdf.multi_cell(0, 10, data)
 ```



<p><b>Step 4 : </b>Finally we converted the text file into notes.pdf which can be distributed among the students. </p>

  ```py
     # Convert the text file to PDF after writing 
     with open("notes.txt", "r") as file: 
         text = file.read() 
     pdf.output("notes.pdf")
 ```



