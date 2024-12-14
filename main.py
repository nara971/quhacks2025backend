from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model('base')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    filepath = file.filename
    file.save(filepath)
    
    try:
        result = model.transcribe(filepath)
        transcription = result['text']
        os.remove(filepath)
        
        return jsonify({
            'transcription': transcription
        })
        
    except Exception as e:
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
