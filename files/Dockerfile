FROM python:3.8-buster

RUN pip install flask

WORKDIR /src

COPY app.py .

ENV FLASK_APP=/src/app.py

EXPOSE 5000/tcp

CMD python -m flask run --host=0.0.0.0
