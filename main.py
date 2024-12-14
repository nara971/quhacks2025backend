import whisper
import os.path

input_file = "Recording.m4a" # Load the Whisper model
model = whisper.load_model("base")

def transcribe_audio(input_file, output_file):
    print("Transcribing", input_file)
    print(os.path.exists(input_file))
    # Transcribe the audio file
    result = model.transcribe(input_file)
    transcription = result['text']
    
    # Save the transcription to a new text file
    with open(output_file, "w") as file:
        file.write(transcription)



if __name__ == "__main__":
    # Specify the input audio file and output text file
    input_audio_file = "Recording.m4a"  # Change this to your audio file path
    output_text_file = "transcription.txt"  # Output file for the transcription
    
    # Call the transcription function
    transcribe_audio(input_audio_file, output_text_file)
    print("Transcription completed and saved to", output_text_file)