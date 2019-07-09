**Update July 2019**: **This is a maintained fork of the [GUTMA Registry Broker](https://github.com/gutma-org/droneregistry-broker) that includes integration with OpenID and OpenID Connect usign OAuth**

## Key Changes
This fork includes significant changes and updates to the GUTMA broker:

1) Integration with Identification and Authentication
2) Updated URL endpoints of login and identity

This uses the Auth0 service to issue OpenID and OpenID Connect tokens to perform authentication and privilages. 

## Registry Broker

Welcome to the registry broker sandbox. This site has three things: 

1. [Registry Broker Whitepaper](https://github.com/gutma-org/droneregistry-broker/blob/master/documents/Registration-Brokerage-Specification.pdf), read this first to familiarize yourself with idea behind the broker. 


2. Two working registries with sample data. The first registry is `registryA`  and the second one is `registryB`. These are instances of the GUTMA aircraftregistry repository. You can explore operators in [registryA](http://registrya.herokuapp.com/api/v1/operators) or [registryB](http://registryb.herokuapp.com/api/v1/operators). These are independent registries and try to simulate national registries. 

3. The user enters a ID in the form and gets a token return that can be queried for status and results.



## Contribute

You can open issues to this repository, review the Landscape document to review the background and look at open issues to look at the current work in progress. 

## Technical Details  / Self-install

This is a Django project that uses Django, Django Rest Framework, Celery and Redis  

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