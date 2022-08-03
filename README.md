![banner image](https://www.eraa.org/sites/default/files/styles/lightwindow_banner/public/files/images/sponsor/era_website_-_rolls-royce_banner.jpg?itok=yc3b-8Xb)

# Rolls-Royce ParlAI ARP

## This project developed a chatbot prototype for MND patients as a part of Rolls-Royce AI for good project

prototype ver 1.0

important version info:
- python 3.8.13
- ubuntu 22.04
- pytorch 1.12.0
- cuda 11.3
- cudnn 8.3.2_0
- parlai 1.6.0

logic:
- this prototype is devided into 3 parts:
- __main__.py: interactive with 3 models, getting user input and output the response
- RRagent.py: the agent class, which is used to respond the question and detect the conversation condition
- verbdetect.py: the verb and noun detection function, which is used to detect the verb and noun in the user input

ashely 03 aug 2022