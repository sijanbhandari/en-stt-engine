


FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN wget https://github.com/sijanbhandari/en-stt-engine/releases/download/v0.9/large_vocabulary.scorer
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
