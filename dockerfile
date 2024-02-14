# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
ENV FLASK_APP run.py

COPY requirements.txt requirements.txt
COPY run.py /
RUN pip3 install -r requirements.txt

COPY . .

# final configuration
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]