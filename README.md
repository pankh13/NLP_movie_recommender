# Movie Recommender System Based on Paragraph to Vector


One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python (version from 2.7 to 3.6 will do) and PostgreSQL (or any powerful and efficient open source database).

### Built With

* [gensim](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [nltk](https://maven.apache.org/) - Dependency Management


## Data Manipulation

### Data Collection

Download the data source and get account for API (see Data Source part). Dump the data into database and start data collection from Amazon.

### Data Cleansing

Recorded in the sql and Python scripts. See [blog]() for details. 

## Model Training

Both single worker version (which eliminate randomness) and the fast version are included. See [blog]() for details. 

## Running the tests

The are various way of testing the model, but none of which are included. 

## Results

Results are dumped into file by the script. 

## Deployment

Deployed in AWS with a [whole website](http://movienet.us-west-2.elasticbeanstalk.com/). 

## Versioning

First version of the model.

## Authors

* **Eric Kehan Pan** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/pankh13/movienet/contributors) who participated in this project.

## Data Source 
* [Amazon movie reviews](https://snap.stanford.edu/data/web-Movies.html) - 8 million movie reviews
* [Amazon Advertising API](https://advertising.amazon.com/API) - Source for movie names and posters

## Acknowledgments

* J. McAuley and J. Leskovec. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. WWW, 2013.

