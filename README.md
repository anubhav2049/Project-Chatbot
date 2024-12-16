A chatbot still under development. Currently, very simplistic and limited in functionality, with only a handful of questions possible. Going to extend as I keep working on it. 

Version 2: Updated functionality with natural language processing. Added 'preprocess' script so chatbot can handle slightly more complex language. Still only can process basic commands, but now can tokenize from phrases and sentences. Updated from just one word commands. Now can process commands and reply to commands like "What's your name". Plan to add more functionality and extend this. 

Version 3 (12/16/2024): Updated functionality to use even better intent processing. Created a basic web application using Flask and Tailwind CSS to make the layout and handle the JavaScript. File "index.html" in templates gives the whole JavaScript as well as Tailwind CSS in the same file.

Version 3.1 (12/16/2024): Updated the overall look of the web application. Chatbot now fills the whole website instead of a small box in the middle of the screen.

A near future plan is to add weather detection/weather prediction functionality. Intend to also integrate neural networks into the chatbot to extend and enhance functionality.
A name for the Chatbot is also planned. 


(NOTE: Currently only runs in shell if you run the usual python command "python3 simple-chatbot.py".)

Utility: Make sure to use "pip install -r requirements.txt" so all python dependencies are installed and set up. Then, run "python app.py" and it'll run locally on your web server. "python chatbot.py" still works, but that will run the code in the terminal only.)
