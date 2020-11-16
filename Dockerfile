FROM ubuntu

#=================================
# Enviroment variables
#=================================


#=================================
# SetUp Ubuntu
#=================================

RUN apt-get update && \
    apt-get -y install sudo \
    wget \
    curl \
    unzip

RUN apt-get update && apt-get install -y \
    python \
    python-setuptools \
    python3-pip

RUN apt-get install -qy xvfb

ENV TZ=Europe/Prague
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
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

RUN CHROME_VERSION=$(google-chrome --version | cut -f 3 -d ' ' | cut -d '.' -f 1) \
    && CHROMEDRIVER_RELEASE=$(curl --location --fail --retry 3 http://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}) \
    && curl --silent --show-error --location --fail --retry 3 --output /tmp/chromedriver_linux64.zip "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_RELEASE/chromedriver_linux64.zip" \
    && cd /tmp \
    && unzip chromedriver_linux64.zip \
    && rm -rf chromedriver_linux64.zip \
    && sudo mv chromedriver /usr/local/bin/chromedriver \
    && sudo chmod +x /usr/local/bin/chromedriver \
    && chromedriver --version
