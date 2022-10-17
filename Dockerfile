# start by pulling the python image
FROM python:3.8-alpine

RUN wget https://github.com/sijanbhandari/en-stt-engine/releases/download/v0.9/large_vocabulary.scorer

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
