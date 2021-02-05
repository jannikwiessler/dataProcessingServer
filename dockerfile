FROM python:3.7.9-slim-buster
RUN pip install swagger_parser geopy cherrypy parameterized
COPY trip_processor.py .
COPY web_service.py .
EXPOSE 8080
ENTRYPOINT ["python", "web_service.py"]