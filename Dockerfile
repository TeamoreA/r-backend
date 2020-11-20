# Set base image to be used as python 3.6.9 image
# It will be pulled from docker hub
FROM python:3.5-slim

# State the maintainer of the docker configs 
LABEL maintainer="Timothy Kamau <teamorekamau97@gmail.com>"

# Set up the working directory of the api where the code will be housed. :)
WORKDIR /integration-services

# For efficiency lets first copy the requirements.txt file that will be 
# used to install application dependencies in the next stage. It is good
# to handle alll installations before copying the files to be used.
# COPY /requirements/tests.txt /integration-services
COPY . .

# Update the base image with recent updates from the repository
# Install the package to create virtual environment in the app
# in this case pipenv. Then install dependancies from the requirements.txt
# file we copied earlier. This process always takes sometime. It depends on
# the internet connection speed you have..... :)
RUN apt-get update && \
    apt-get upgrade -y
#     pip install pipenv && \
#     pipenv install 
RUN pip3 install -r requirements/tests.txt
# Set the port to 8000. Port used by the application to serve requests.
# ENV PORT=8000

# Copy all the items from the current path to the working directory of the image
COPY . /integration-services