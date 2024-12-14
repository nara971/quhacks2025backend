FROM python:3.9 

WORKDIR /app

COPY main.py .
COPY Recording.m4a .
RUN pip install openai-whisper numpy 
CMD ["python", "./main.py"] 