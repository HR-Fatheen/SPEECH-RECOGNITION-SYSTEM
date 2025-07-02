## 🛠 Installation & Setup

### Step 1: Clone the Repository

git clone https://github.com/your-username speech-to-text-transcriber.git
cd speech-to-text-transcriber

### Step 2: Create and Activate a Virtual Environment

For Windows (in Virtual Studio code):
python -m venv env
env\Scripts\activate

For macOS:
python3 -m venv env
source env/bin/activate

### Step 3: Install Required Packages

pip install -r requirements.txt
python -m textblob.download_corpora

requirments.txt:
transformers
torch
soundfile
pydub
symspellpy
textblob

### Step 4: Add Frequency Dictionary for SymSpell

Your script will automatically download the dictionary:

https://raw.githubusercontent.com/mammothb/symspellpy/master/symspellpy/frequency_dictionary_en_82_765.txt

### Step 5: Prepare the Audio File

Record your voice or use a .wav file (16kHz, mono).
Save the audio file in your project folder.

#### Rename it as:
example.wav

### Step 6: Run the Script
python coding.py