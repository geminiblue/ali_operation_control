FROM python:3.4
WORKDIR /application
ADD . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python server.py" ]