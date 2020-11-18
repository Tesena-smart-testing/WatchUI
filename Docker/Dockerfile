FROM ubuntu

#=================================
# Enviroment variables
#=================================

ENV ROBOT_TESTS_FOLDER /tests
ENV ROBOT_WORK_DIR /temp
ENV ROBOT_REPORTS_DIR /reports
ENV BASH_FILE /bash

ENV SCREEN_WIDTH 1080
ENV SCREEN_HEIGHT 1920
ENV SCREEN_COLOUR_DEPTH 24
ENV DISPLAY=:99

#=================================
# SetUp Ubuntu
#=================================
ENV TZ=Europe/Prague
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get -y install sudo \
    wget \
    curl \
    unzip \
    gcc \
    libffi-dev \
    python \
    python-setuptools \
    python3-pip \
    xvfb

#=================================
# Install requirements
#=================================
RUN pip3 install robotframework-seleniumLibrary \
    robotframework \
    numpy \
    matplotlib \
    pandas \
    Pillow \
    imutils \
    scikit-learn \
    scikit-image \
    selenium \
    opencv-python

#=================================
# Install Chrome and driver
#=================================
RUN sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    sudo apt install -y ./google-chrome-stable_current_amd64.deb

RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#=================================
# Start RF
#=================================
ADD run-test.sh .
CMD ["chmod +x run-test.sh"]
CMD ["sh", "run-test.sh"]