# Pokedex

Pokedex: A world of Pokemon in the form of REST API. Given a pokemon name Pokedex service will return some basic information about that pokemon.

## Getting Started

The service follows a simple setup to get it up and running.

### Prerequisites

Service requires following tech stack to be installed in the system before running.  If you do not have them installed already, follow the official documentation in the to do so:

- [python 3.9](https://www.python.org/downloads)
- [pipenv](https://pipenv.pypa.io/en/latest/install)

Optional requirement:

- [Docker](https://docs.docker.com/engine/install/) (for Option 2 below)

### Dependencies

Open up a terminal, move to the root of the project, and execute the following commands:

```sh
# shell will spawn a shell with the virtualenv activated.
$ pipenv shell

# install dependencies in the virtualenv
$ pipenv install

# make start script executable
$ chmod +x start
```

### Start the service

There are couple of options to start the service locally.

**Option 1:**
Run the start script from the terminal which will spin up the service.
  
```sh
# spins up the service 
$ ./start
```

**Option 2:**
Run as a containerised service. Execute the folllowing  commands from the root directory of the project.

```sh
# build the docker image. replace <image_name:tag> with a suitable name&tag of your choice
$ docker build -t <image_name:tag> .

# e.g.
$ docker build -t pokedex:latest .

# run the image in a container
$ docker run --name poke -it -dp 9000:9000 pokedex:latest
```

Once  the service is up and running successfully, browse the API documentation here:
[localhost:9000/docs](http://127.0.0.1:9000/docs)

### Testing

The application has its unit tests inside `tests` directory. Run the following commands to execute unit tests of the application.

```sh
# activate virtualenv
$ pipenv shell

$ python3 -m pytest tests
```

## Production setup

For a production API I would do following additional steps:

- Add a [pre-commit-configuration](https://pre-commit.com/#2-add-a-pre-commit-configuration) file.
- Tag container image with the following format: `<image_name>:YYYY-MM-DD_HH-MM-SS`
- Set up CI/CD pipeline to automate the testing, code coverage, and building of docker image.
- Deploy it as a containerised service in the cloud. Therefore I would set up a minimum of 3-node kubernetes cluster to deploy the service with a replica set of 3. An external load balancer in front the cluster.
- Keep the deployment of the prod environment to be triggered manually once container image is built successfully and pushed to the container registry.
- Update to the new version of the service as a rolling update so there's no downtime of the service.
