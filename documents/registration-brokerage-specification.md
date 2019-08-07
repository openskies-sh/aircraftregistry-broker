## Aircraft Registry Brokerage

In the EU specifically and in other places around the world, there are existing and upcoming regulations that mean that member states will develop a digital registry of drone operators and equipment. The registry (schema and API) are out of scope for this document you can review the [registry whitepaper here](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md). What is important in this context, is recognizing the fact that there will be many registries at different administrative levels across the world: local, state and federal. This document is focused on how these different registries could connect and exchange data and information securely.

### The problem

We expect a majority of the queries to a registry will happen within a single administrative and jurisdictional setup, however there will be a significant number of queries would be made across different registries between national and administrative boundaries. This document details a system that enables communication between different registries regardless of where they are located. We assume that data in the registries will have to be queried securely and in realtime.

#### The problem: Querying many different registries

<img src="https://i.imgur.com/6qX5guv.jpg" height="500">

An entity (interested party) trying to query registries that implements a public API has to deal with the following issues:

1. How do they know if the registry exists and has a API endpoints to query? 

2. How do they manage identity and credentials and passing them as they are trying to query? Where do they get these credentials? This is both a problem of the technology and the mechanism of storing and passing credentials.

3. How are changes to registry API managed and communicated? e.g. if there are changes to a endpoint, data or credential requirements.

4. How does one know the URL of the registry services that are compatible and available?

5. How does a registry know if the entity querying it is indeed privileged? i.e. authenticated that the query is indeed coming from the police for e.g.

In some ways these are a combination of technical and procedural problems that will impact  any registry operator. In the worst case every operator will have to develop solutions independently for specific problems. These problems also span a number of domains: service discovery, identity and authentication and organization of registries.

### Example Use Case

A CAA or interested party in Geneva wants to query the French registry (neighboring country), given the proximity of France and Switzerland, the Swiss CAA might just make a special agreement with the French CAA and have logins and credentials for their registry. In such a case, there is no need for the Swiss CAA to use a general purpose system. However, if the CAA wants to query the registry in Estonia for e.g., they may not have contacts or credentials to query it in such a case they might use the broker. Another use case might be that a pilot registered and certified in France wants to fly his drone in Germany. German authorities might want to check his certifications and if they are valid (digitally).

These are some examples of querying a different registry and it trasnforms the role of a registry from a data store to making a active living system. It is important to consider the implications of a such a system since how this is done has important technical and architectural implementations. Specifically, deciding on the architectural direction will enable us to analyze the best way forward around difficult consideration around storing credentials and managing them.

#### How to address these problems?

There are many ways to address this problem, they are mainly of communication and co-ordination between the different entities. One argument is that this can be managed by people-to-people contact but for truly scalable solutions, a software based implementation is necessary. Let us begin with non-technical solutions:

1. Build a list of registries and their endpoints and API and maintain it as a organizational responsibility e.g. by ICAO, JARUS or other relevant national authorities.
2. Develop a forum / portal to share the latest in updates and between different entities. Allow the CAAs to engage and announce and clarify changes to their APIs.

While these methods are useful and can work, as mentioned earlier, they are not scalable. In addition, in a federated registration model the registry endpoint is decentralized and discovery of registries is a issue and co-ordinting this manually is a problematic task. A software solution to this problem is to build a bridge between the individual registries and the clients / interested parties querying it. Conceptually, it would look like the following:

<img src="https://i.imgur.com/7225wmh.jpg" height="500">

Figure 2: Decentralized Querying vs Centralized Querying

There are many advantages to building a system like this that reduces the engineering cost and provides certainty for interested parties when querying different registries. It ensures that the Broker / Brokerage takes care of the changes in the individual registries. In this case the interested party must implement just one API to the broker to ensure that queries would work without having to worry about implementing different API calls. As a broker the organization that runs it has an interest in working with the different CAAs to implement a common API to ensure that the re-work associated with the software is minimum. By having a central broker, the originating party consolidates the requests and has leverage over the registry operators.

#### Pros and cons

| Pros  | Cons |
| ------------- | ------------- |
| Individual Interested parties will not have to implement many calls to the registry    | If there is a brokerage, what is the incentive for individual registries to follow a standard API especially if it not backed by a trusted entity (e.g. ICAO)  |
|  A standard way to communicate and query different registries (like the VAT system) in EU, ICAO aircraft registry | This is a level of abstraction that might be unnecessary |
| A single point of contact for querying information like FAA  | The different entities running the registry might not talk to each other (they should) |
|A third party maintains the registry interoperability and provides the industry and other actors a standard way to query and access this data. |  Data storage vs. querying does the broker store the data or just query it?|
| | Security and confidentiality of the information is critical and the best way to ensure that no confidential data is compromised is by not storing it permanently.|

#### Authentication

The primary goal of this spec is to develop a brokerage layer where incoming requests are routed to the individual registry and then response queries are then routed to the registry operator. Following are the authentication credentials required for the parties in this ecosystem.

| Interested Party    | Broker | Registry Operator|
| ------------- | ------------- | ------------- |
| Authentication credentials for regular queries:<br> Account creation <br>Email contact address | If unprivileged entities are throttled then no need for any authentication information for regular interested parties, only the destination county and the type of information (API call) that is being made. | Maintain username and password for operators and any other interested party that wants to query the registry. | 
| Throttle all unprivileged requests | Maintain a list of privileged client access tokens (and documentation) | Maintain separate documentation and credentials for privileged access. |
| Privileged authentication credentials e.g. police, military etc. Some certificate authority to verify the keys that the party is indeed a privilaged entity and authorization keys for that entity (open question: how keys are recycled)| Maintain list of documentation and certificates etc. | Maintain credentials for Brokers to ensure that access is not broken |

#### Notes on privileged access

Given the complications of maintaining documentation and keys for privileged access, some ideas that could be pursued:

1. Privileged access should be made directly to the individual registry and not globally. 
2. Registry operators have access to a share with all the certification information and details as a shared library / document store.
3. In the case where privileged access requires querying many servers to generate a “merged” view of the information, this may need multiple queries.
4. For the first version, it maybe useful to not have privileged access as a part of the brokerage but have it as a feature for a later date.

#### Servers

This type of brokerage service will be hosted on servers in Europe and managed out of European data centers. The requirement would standard and in compliance with EU and other government data protection regulations.

<img src="https://i.imgur.com/Co9ZUzt.png" height="500">

Figure 3: Sample flow of queries and traffic

In this setup, no data is stored on the broker servers other than the credentials for queries to the national registries. The interested party makes a query to the broker who in turn passes the query to the appropriate registry.

#### Security

For most registry queries, security considerations are straight forward, in that it is a routine query with standard credentials and no sensitive information is transferred. Using standard internet-based security of web tokens should suffice in this case. Proper firewalling and management of data base is necessary.

#### Conceptual Architecture

This section details some of the architectures that can be pursued for this problem from the least data requirement to maximum data requirements for the solution. And a pros / cons analysis of each approach is conducted as well. An analysis based on data requirements is important because important confidential data is potentially passed through the system.

##### Option A: Apache Zookeeper 
A useful approach in this context is if the GUTMA API is successfully adopted, then to prevent duplication and re-architecting the API calls, a simple implementation of Zoo keeper would suffice where the individual registries are managed by the individual CAAs.

##### Option B: API Broker
A API broker architecture as described above, needs to store credential information but the actual data is stored in the database owned by the CAAs outside the system.

##### Option C: Data Scraping and storage
A alternative architecture to overcome the issue of data and external queries, is to scrape and have a dump of data and the broker stores it. This is a case where data is scraped from the registry and stored in a database owned by the broker.

##### Option A: Zookeeper Pros and Cons

| Pros  | Cons |
| ------------- | ------------- |
| No data storage  | All actors must implement standard API  |
| Simplest to implement  | No control over performance, if an API call breaks |
| Minimal software development  | Ecosystem not ready for a “hands-off” approach |
| Safest for Brokerage operator  | |


##### Option B: API Broker Pros and Cons

| Pros  | Cons |
| ------------- | ------------- |
| Flexible architecture  | Need to maintain credentials|
| Minimal data storage | Response times cannot be guaranteed |
| Frontend development flexibility | Duplication of query procedures + data|


##### Option C: Data Scraping / Storage Pros and Cons
Data scraping / storage involves taking a snapshot of the registries and building a "master" database. Setting aside the difficulty in achieving this, there are some benefits that need to be explored.

| Pros  | Cons |
| ------------- | ------------- |
| Fastest performance and query response | Data may not be “fresh” | 
| Most control for operator | Rigorous controls and data safety procedures necessary|
|Management of changes / updates | GDPR issues in addition to security and other issues of storing data in a central database|

### Integration with ICAO Trust Framework 

<img src="https://i.imgur.com/RMl4kGK.jpg" height="400">

Figure 4: A conceptual flow of secured endpoints.

The core addition in this figure is a Identity and Authentication provider that adopts the concepts of the ICAO Trust framework. The provider issues tokens and credentials to query the registry via the broker. The credentials and JavaScript Web Tokens (JWT) are securely passed to the broker and finally to the registry. The decryption and validation of the tokens happens at the registry level. 


#### Version History

| Date | Version | Comments | Author |
| ------------- | ------------- |------------- |------------- |
| 8-August-2019  | V4  | Reword introduction and sections   | Dr. Hrishikesh Ballal |
| 5-August-2019  | V3  | Formatting update and added integration with ICAO Trust Framework  | Dr. Hrishikesh Ballal |
| 14-March-2019  | V2  | Added Comments and review from NUAIR  | Dr. Hrishikesh Ballal / Andy Thurling |
| 23-Sep-2018   | V1  | Initial Draft  | Dr. Hrishikesh Ballal |
