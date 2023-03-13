# 1. detect wake word,
# 2. prompt for question, 
# 3. pass query to OpenAi and 
# 4. speak response

import keys
import waitForWakeWord
import SpeechRec
import callOpenai
import openai
from gtts import gTTS
import playsound

def speak(text, filename):
  tts = gTTS(text=text, lang="en")
  tts.save(filename)

def play(filename):
  playsound.playsound(filename)

openai.api_key =  keys.key['OPEN_AI_KEY']
filename = "query.mp3"

def Gspeak(speech, filename):
	speak(speech, filename)
	play(filename)
	return

speech = "Waiting for the wake word - blueberry"
Gspeak(speech, filename)

success = waitForWakeWord.wait()

while success:
	Gspeak("Ask me a question or say quit", filename)
	query = SpeechRec.recognise()

	if query != "quit":
		Gspeak("I think you said " + str(query) + ". Asking chat g p t", filename)
		response = callOpenai.openai_create(query)
		Gspeak("The answer is", filename)
		Gspeak(response, filename)
	else:
		success = False

Gspeak("goodbye", filename)
