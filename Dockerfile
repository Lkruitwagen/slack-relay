# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Install Git for pip git packages
#RUN apt-get -y update
#RUN apt-get -y install git

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

#
# Copy local code to the container image.
ENV APP_HOME /app


WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir .

#
CMD exec uvicorn slackrelay.app:app --host 0.0.0.0 --port $PORT --workers 1
