FROM python:3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m nltk.downloader punkt

WORKDIR /app
ADD . /app

RUN python -m nltk.downloader punkt
# Entry Point
CMD ["python", "languageprocessor.py"]
