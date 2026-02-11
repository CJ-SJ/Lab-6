# -*- coding: utf-8 -*-
"""
Created on Friday March 22 11:24:40 2024
"""

#The following code will work for Python 3.7.x+

#----------------------------------------------
#REMEMBER TO RUN THESE PIP COMMANDS if you have an older OpenAI:
#pip uninstall openai
#Note: the command may look like this in your venv  C:\Python310\Scripts\pip install openai pandas python-dotenv

#----------------------------------------------
#RUN THESE COMMANDS FROM THE TERMINAL
#Create the virtual environment called "venv"
#python -m venv venv   

#from venv
#pip install openai==0.28 pandas python-dotenv

#Activate the venv 
#Windows command:
#venv\Scripts\activate
#MacOS or Linix command: 
#source chatgpt_env/bin/activate



import os
import openai #remember to pip install pandas openai
from dotenv import load_dotenv  #remember to pip install python-dotenv
load_dotenv()

# Set the API key
"""
# Visit your API Keys page to retrieve the API key you'll use in your requests.
# Remember that your API key is a secret! Do not share it with others or expose 
#  it in any client-side code (browsers, apps).
https://platform.openai.com/account/api-keys 

You will need these two (both are confidential):
YOUR OPENAI ORG KEY (from the left panel, click on Settings)
OPENAI_API_KEY (from your picture on the top right of the browser, click on your organization, then click on View API keys)
"""
openai.api_key=os.getenv("OPENAI_API_KEY")

#Examples of messages being built with two parts: Role & Tasks
#---
#messages = [{"role": "system", "content": "You are a poet"}]
#messages.append({"role": "user", "content": "Get the sum of 5 and 5^2"})
#---
#messages = [{"role": "system", "content": "You are a mathematician"}]
#messages.append({"role": "user", "content": "Get the sum of 5 and 5^2"})

while (True):
    myrole = input("\nWhat is my role? (or type 'quitme' to quit): \n")
    if(myrole == 'quitme'):
        break
    mytask = input("\nWhat is my task? (or type 'quitme' to quit): \n")
    if(mytask == 'quitme'):
        break

    messages = [{"role": "assistant", "content": myrole}]
    messages.append({"role": "assistant", "content": mytask})
    
    answers = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        temperature = 0.5,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0,
        messages = messages
    )


    print("----------------\n")
    print(answers['choices'][0]['message']['content'])
    # same as print(answers.choices[0].message.content)

    print("----------------\n")
