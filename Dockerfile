# Dockerfile for a Python Behave testing environment with Selenium and Allure reporting

# Use an official Python runtime as a parent image
FROM python:3.10.2-bullseye



# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y wget xvfb unzip curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    selenium \
    behave \
    mysql-connector-python \
    pyyaml \
    allure-behave \
    behave-html-pretty-formatter

# Install Google Chrome and Chromedriver
ENV CHROMEDRIVER_VERSION 97.0.4692.71
ENV CHROMEDRIVER_DIR /chromedriver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    mkdir $CHROMEDRIVER_DIR && \
    wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR && \
    rm -rf /var/lib/apt/lists/* $CHROMEDRIVER_DIR/chromedriver*.zip

# Set up Chromedriver Environment variables
ENV PATH $CHROMEDRIVER_DIR:$PATH

# Install OpenJDK 11 and set JAVA_HOME environment variable
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

# Install Allure for test reporting
RUN curl -Ls https://github.com/allure-framework/allure2/releases/download/2.26.0/allure-2.26.0.tgz | tar xz -C /opt && \
    ln -s /opt/allure-2.26.0/bin/allure /usr/bin/allure

# Install Allure plugin for Behave
RUN pip install allure-behave

# Install ChromeDriver using webdriver_manager
RUN python -m pip install webdriver_manager

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the allure-config folder Override the default config
COPY /allure-config/allure.yml /opt/allure-2.26.0/config/allure.yml
COPY /allure-config/styles.css /opt/allure-2.26.0/plugins/custom-logo-plugin/static/styles.css
COPY /allure-config/mdw-logo.jpg /opt/allure-2.26.0/plugins/custom-logo-plugin/static/mdw-logo.jpg

# Copy the local code to the container
COPY . /app
# Create a non-root user
RUN useradd -ms /bin/bash tester

# Set permissions for the tester user
RUN chown -R tester:tester /app

# Set permissions for the logs directory
RUN mkdir -p /app/logs && chown -R tester:tester /app/logs && chmod -R 755 /app/logs

# Switch to the non-root user
USER tester
# Uncomment the following line if you want to run Behave when the container launches
# CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "--outfile=./allure-results"]
# Set the logging environment variable (you can adjust the level as needed)
ENV LOG_LEVEL=INFO
# Keep the container running and allow entering it
CMD ["/bin/bash", "-c", "while true; do sleep 1; done"]


