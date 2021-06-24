FROM python:3.9

EXPOSE 9000

# updates and install packaging tool
RUN apt-get update
RUN pip3 install pipenv

# creates working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# copy all files to working directory
COPY . .

# makes script executable
RUN chmod +x start
RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["./start"]
