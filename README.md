**Update July 2019**: **This is a maintained fork of the [GUTMA Registry Broker](https://github.com/gutma-org/droneregistry-broker) that includes integration with OpenID and OpenID Connect. It uses OAuth tokens to query the registries.**

## Read First and Key Changes
This fork includes significant changes and updates to the GUTMA repository:

1) Integration with Identification and Authentication, currently using Auth0 and JWT Tokens
2) Updated URL endpoints of login and identity

This uses the Auth0 service to issue OpenID and OpenID Connect tokens to perform authentication and privilages.

## Read First

Welcome to the registry broker sandbox. This site has three things:

1. [Registry Broker Whitepaper](https://github.com/openskies-sh/aircraftregistry-broker/blob/master/documents/registration-brokerage-specification.md), read this first to amiliarize yourself with idea and key concepts behind the broker.

2. This broker deployment queries one working registry with sample data (others can be added). Lets call this registry `registryA`, this is a instance of [aircraftregistry](https://github.com/openskies-sh/aircraftregistry) repository. You can explore operators in this [registryA](http://aircraftregistry.herokuapp.com/api/v1/operators). This registry is queried by this broker.

3. The logs in using their email ID in the form and gets a token return that can be queried for status and results.

## Contribute

You can open issues to this repository, review the Landscape document to review the background and look at open issues to look at the current work in progress.

## Technical Details  / Self-install
This is a Django project that uses Django, Django Rest Framework, Celery and Redis and can be deployed to for e.g. Heroku or other platforms. 

### 1. Install Dependencies
Python 3 is required for this and install dependencies using `pip install -r requirements.txt`.

### 2. Create Initial Database
Use `python manage.py migrate` to create the initial database tables locally. It will use the default SQLLite.

### 3. Populate initial data
Use `python manage.py loaddata switchboard/defaultbrokerdata.json` to populate initial data.

### 4. Run Application
1. You will need a redis install and also celery as a worker queue
2. Launch browser to http://localhost:8000/ to launch the Broker

## Trust Bridge
To install the trust bridge components you will need to create a account at Auth0 or other service to issue and manage OAuth Tokens.