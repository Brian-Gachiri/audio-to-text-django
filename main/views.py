from django.http import JsonResponse
from django.shortcuts import render
import speech_recognition as sr
from pydub import AudioSegment
import os


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def uploadFile(request):
    if request.method == 'POST':
        video_file = request.FILES['file']
        video = AudioSegment.from_file(video_file, format="mp4")
        audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
        audio.export("audio.wav", format="wav")

        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()

        # Open the audio file
        with sr.AudioFile("audio.wav") as source:
            audio_text = r.record(source)
        print(audio_text)
        # Recognize the speech in the audio
        text = r.recognize_vosk(audio_text, language='en-US')

        # Print the transcript
        file_name = "transcription.txt"

        with open(file_name, "w") as file:
            # Write to the file
            file.write(text)
        # Open the file for editing by the user
        os.system(f"start {file_name}")
        return JsonResponse({'status': 'success'})
    else:
        # Render the upload form
        return JsonResponse({'status': 'wrong method'})


def convertToText(file):
    pass