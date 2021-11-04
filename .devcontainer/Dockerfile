FROM mcr.microsoft.com/vscode/devcontainers/python:3.9-buster

RUN apt-get update \
    && apt-get install -y tesseract-ocr \
        tesseract-ocr-all

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm -rf ./google-chrome-stable_current_amd_64.deb

RUN VERSION=95.0.4638.17 \
    && wget https://chromedriver.storage.googleapis.com/$VERSION/chromedriver_linux64.zip \
    && unzip ./chromedriver_linux64.zip \
    && mv ./chromedriver /usr/bin/chromedriver \
    && chown root:root /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm -rf ./chromedriver_linux64.zip \
    && echo 'export PATH:$PATH:/usr/bin/chromedriver' >> ~/.profile

RUN python -m pip install --upgrade pip \
    && pip install pipx \
    && pipx install poetry