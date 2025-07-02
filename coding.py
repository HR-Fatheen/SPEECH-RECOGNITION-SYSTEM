from transformers import Wav2Vec2Processor , Wav2Vec2ForCTC
from symspellpy import SymSpell , Verbosity
from pydub import AudioSegment
from textblob import TextBlob
import soundfile as sf
import urllib.request
import numpy as np
import torch
import os 

os.chdir(os.path.dirname(__file__))

print("Step 1 : Loading the processor")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")

print("Step 2 : Loading the model")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print("Step 3 : Processor and Model loaded successfully")

input_file  = "example.wav"
converted_file = "cleaned_example.wav"

sym_spell = SymSpell(max_dictionary_edit_distance=2,prefix_length=7)
dictionary_path =  "https://raw.githubusercontent.com/mammothb/symspellpy/master/symspellpy/frequency_dictionary_en_82_765.txt"

urllib.request.urlretrieve(dictionary_path,"frequency_dict.txt")
sym_spell.load_dictionary("frequency_dict.txt",term_index=0,count_index=1)

def correct_spelling_symspell(text):
    corrected_words = []
    for word in text.split():
        suggestions = sym_spell.lookup(word,Verbosity.CLOSEST,max_edit_distance=2)
        if suggestions:
            corrected_words.append(suggestions[0].term)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)

def convert_to_mono_wav(input_path,output_path):
    try:
        print(f"Converting audio:{input_path} -> {output_path}")
        sound = AudioSegment.from_file(input_path)
        sound = sound.set_channels(1).set_frame_rate(16000)
        sound.export(output_path,format="wav")
        print("Audio converted to mono and 16000Hz")
        return True
    except Exception as e:
        print("Error converting audio: ",e)
        return False
    
if not os.path.exists(input_file):
    print(f"File not found:{input_file}")
    exit()

if not convert_to_mono_wav(input_file,converted_file):
    print(f"Audio conversion failed , Please check the file format")
    exit()

try:
    audio_input, sample_rate = sf.read(converted_file)
    print("Audio loaded successfully")
    print("Sample rate:", sample_rate)
    print("Audio shape:", audio_input.shape)
except Exception as e:
    print("Error loading audio:", e)
    exit()

try:
    input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values.to(device)
    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    raw = transcription.lower()
    corrected = correct_spelling_symspell(raw)

    print("\nRaw Transcription:")
    print(transcription)
    print("\nCorrected Transcription:")
    print(corrected)
    print("\nTranscription Completed Successfully!")

    final_output = str(TextBlob(corrected).correct())
    print("\nFinal Output with Basic Punctuation Fix:")
    print(final_output)

except Exception as e:
    print(f"Transcription error: {e}")

print("\n Note:")
print("The transcription may contain slight word variations,")
print("but it aims to preserve the overall meaning of the audio.")