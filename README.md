# Speech Recognition System using Wav2Vec2 and PyTorch

## Internship Credentials

- **Intern Name**: Mohamed Fatheen H.R  
- **Intern ID**: CT06DG2241  
- **Domain**: AI Developer Intern  
- **Company**: CodTech IT Solutions  
- **Internship Duration**: 4 Weeks  
- **Mentor**: Neela Santosh Kumar  

## Project Description

This project is a Speech Recognition System built using Hugging Face's pre-trained Wav2Vec2 model, specifically `facebook/wav2vec2-base-960h`. Its main goal is to turn spoken English audio into accurate written text by using the latest in deep learning technology. Created as part of an internship, the system is designed to transcribe short `.wav` files, correct spelling mistakes, and deliver easy-to-read, well-structured transcripts.

The Wav2Vec2 model is a transformer-based algorithm trained on over 960 hours of spoken English from the LibriSpeech dataset. It works directly on raw audio waveforms, making it suitable for real-world speech applications without needing manually crafted features like MFCCs. Users upload their audio, which then passes through a process that cleans the sound, converts speech into text, and performs smart post-processing.

To make the transcriptions clearer, the project uses SymSpell—a fast, memory-efficient spell correction tool that fixes common errors in the raw output. This step is important because sometimes the model merges words or misinterprets pronunciations (for example, turning "test adio" into "testaudio").

For an even cleaner output, TextBlob is optionally used to improve the grammar and add punctuation, making the final text more natural and professional.

The system also takes care of audio preprocessing. It automatically converts uploaded audio into a mono-channel, 16kHz WAV format using pydub, ensuring compatibility with the model. Errors related to file format, sampling rate, or inference are handled smoothly with clear messages

From a user’s perspective, the tool is simple yet powerful. You just provide an audio file (`.wav`), and the system returns three layers of output:
1. **Raw transcription** from the model.
2. **Corrected transcription** using spelling fixes.
3. **Final output** with grammar polishing.

This layered approach helps users understand how the model performs and how much improvement is made in each post-processing step.

## Coded Platform Details
- Language      : Python 3.x
- Framework     : PyTorch via Hugging Face Transformers"
- Libraries     : transformers, torch, soundfile, pydub, symspellpy, textblob"
- Model         : facebook/wav2vec2-base-960h (pretrained)
- Format        : .wav files (mono, 16kHz)
- Execution     : Compatible with CPU and GPU

## Project Structure
project folder 
- README.md             # Detailed documentation file (this file)
- coding.py             # Main Python script for summarization
- installation.txt      # Python dependencies 
- example1.wav          # Example input file
- example2.wav          # Example input file
- Outputs 

## Features

-  Accepts `.wav` audio files and auto-converts them to 16kHz mono format.
-  Uses Hugging Face’s `Wav2Vec2ForCTC` model for transcription.
-  Applies SymSpell to correct common misspellings.
-  Uses TextBlob for optional grammar correction.
-  Displays raw, corrected, and final transcriptions.
-  Handles invalid file formats or conversion failures with friendly errors.

## Limitations / Disadvantages 

-  Wav2Vec2 is case-insensitive and does not add punctuation by default.
-  Handling long audio clips or non-English languages — 
-  Spelling correction using SymSpell works best on single words, not compound or merged phrases.

## Example Output
![Image](https://github.com/user-attachments/assets/69d3e3d3-004f-416b-ba11-7ad882ff85e6)

## Supported Audio Format

- Format: `.wav`
- Channels: Mono
- Sample Rate: 16000 Hz
- Duration: Recommended ≤ 15 seconds for accurate results

## Developed By

**Mohamed Fatheen H.R**  
AI Developer Intern @ CodTech IT Solutions  
2025
