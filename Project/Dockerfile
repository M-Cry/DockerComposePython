FROM python:3.10-alpine

WORKDIR /Project

ADD requirements.txt /Project

RUN pip install -r requirements.txt

COPY . /Project

# run the project
CMD ["python", "app.py"]