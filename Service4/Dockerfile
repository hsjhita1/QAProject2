FROM python:latest
RUN mkdir /opt/QAProject2/
COPY . /opt/QAProject2/
WORKDIR /opt/QAProject2/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]