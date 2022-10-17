# start by pulling the python image
FROM python:3.9

RUN wget https://github.com/sijanbhandari/en-stt-engine/releases/download/v0.9/large_vocabulary.scorer

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 80

RUN pip3 --no-cache-dir install gunicorn

# command line version
# CMD ["./stt.py"]

CMD ["gunicorn", "--access-logfile=-", "-t", "120", "-b", "0.0.0.0:80", "main:app"]
