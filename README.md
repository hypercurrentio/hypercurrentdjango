# Revenium Middleware for Python Django

Django middleware to dispatch metering metadata for HTTP API calls to Revenium.


## Installation

```shell
pip install hypercurrent_metering
pip install hypercurrent_django
```

## Usage

In your `settings.py` file in your Django project directory, 
please add the following to the middleware array:

```python
'hypercurrentdjango.middleware.HyperCurrentMiddleware'
```

## Configuration

#### __`HYPERCURRENT_API_KEY`__
(__required__), _string_, 
your [Revenium API Integration Key](https://docs.hypercurrent.io/user-guide/manage/external-configurations/api-integration-keys)

#### __`HYPERCURRENT_APPLICATION_HEADER`__
(__optional__), _string_, the HTTP header to determine the API consumer.
The default is "clientId".

#### __`HYPERCURRENT_METADATA_HEADER`__
(__optional__), _string_, An optional response header to extract metering metadata from.


#### __`HYPERCURRENT_API_URL`__
(__optional__), _string_, the Revenium API URL. 
You should only need to change this if using a 
non-US based Revenium instance (ie, EMEA or customer compute.)


## Example Application
See hello_project base file folder to see an example of how the middle ware can be implemented.
