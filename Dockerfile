# start by pulling the python image
FROM python:3.9



# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

RUN wget https://github.com/sijanbhandari/en-stt-engine/releases/download/v0.9/large_vocabulary.scorer

# copy every content from the local file to the image
COPY . /app

RUN pip3 --no-cache-dir install uvicorn

# command line version
# CMD ["./stt.py"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
