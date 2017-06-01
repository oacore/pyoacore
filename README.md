# pyoacore

[![Build Status](https://travis-ci.org/oacore/pyoacore.svg?branch=master)](https://travis-ci.org/oacore/pyoacore) 
[![Gitter chat](https://badges.gitter.im/org.png)](https://gitter.im/oacore-mozsprint17/Lobby)

Python client for the CORE APIs


## Mozilla Global Sprint '17
This repository is one of our project for the Mozilla Global Sprint '17. 
![Global Sprint](https://cloud.githubusercontent.com/assets/617994/24632585/b2b07dcc-1892-11e7-91cf-f9e473187cf7.png)
We started this project by generating a simple API client from the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/oacore/pyoacore`)

Then import the package:
```python
import pyoacore 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pyoacore
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from pyoacore.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = pyoacore.ArticlesApi()
core_id = '42' # str | The id of the article

try:
    # Get articles by ID
    api_instance.articles_get_core_id_get(core_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->articles_get_core_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All the APIs can be accessible here https://core.ac.uk/docs


## Documentation For Authorization

Coming soon

## Author

Matteo Cancellieri 



