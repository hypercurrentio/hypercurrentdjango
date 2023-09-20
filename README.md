# HyperCurrent Middleware for Python Django

Django middleware to dispatch metering metadata for HTTP API calls to HyperCurrent.


## Installation

```shell
pip install hypercurrent_metering
pip install hypercurrent_django
```

## Usage

In your `settings.py` file in your Django project directory, 
please add the following to the middleware array:

```python
'hypercurrent_django.middleware.HyperCurrentMiddleware'
```

## Configuration

#### __`HYPERCURRENT_API_KEY`__
(__required__), _string_, 
your [HyperCurrent API Integration Key](https://docs.hypercurrent.io/user-guide/manage/external-configurations/api-integration-keys)

#### __`HYPERCURRENT_APPLICATION_HEADER`__
(__optional__), _string_, the HTTP header to determine the API consumer.
The default is "clientId".

#### __`HYPERCURRENT_METADATA_HEADER`__
(__optional__), _string_, An optional response header to extract metering metadata from.


#### __`HYPERCURRENT_API_URL`__
(__optional__), _string_, the HyperCurrent API URL. 
You should only need to change this if using a 
non-US based HyperCurrent instance (ie, EMEA or customer compute.)

