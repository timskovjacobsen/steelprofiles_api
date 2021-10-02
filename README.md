# Steel profiles API

API for requesting profile data for standard European construction steel profiles.

Currently supported profiles are:

* HEA
* HEB
* HEM
* IPE
* IPN
* UPN

API home page: [steelapi.timskovjacobsen.com](http://steelapi.timskovjacobsen.com)

## Endpoints

* **`GET /api/{profile_type}`**

  E.g. to get data for all **HEA** profiles,
   visit `steelapi.timskovjacobsen.com/api/hea`

* **`GET /api/{profile_type}/{dimension}`**

  E.g. to get data for the profile **HEA120**, visit `steelapi.timskovjacobsen.com/api/hea/120` and you will get this response:

  ```shell
  {
    "HEA120":{
      "index":1,
      "name":"HEA120"
      ,"h":114,
      "b":120,
      "tw":5.0,
      "tf":8.0,
      "r":12,
      "d":74,
      "A":25.3,
      "G":19.9,
      "Iy":606,
      "Wy":106.0,
      "iiy":4.89,
      "Iz":231,
      "Wz":38.5,
      "iiz":3.02
    }
  }
  ```

It's possible to use uppercase profile names in the URL, like HEA.

## API Docs

See the swagger [API Docs](https://steelapi.timskovjacobsen.com/docs) for more info.

## Miscellaneous

The REST API is built with Python and the FastAPI framework. It uses Nginx in front of the API as a reverse proxy. Nginx is configured with SSL certificates to provide a secure HTTPS connection protocol via Let's Encrypt.

The API is deployed on a virtual machine running Ubuntu 20.04 hosted with Digital Ocean.

Shout-out to the [Modern APIs with FastAPI and Python](https://training.talkpython.fm/courses/getting-started-with-fastapi?utm_source=fastapi) course for inspiring this project.

## Contributing

If you want to contribute it's greatly appreciated. Take a look at [CONTRIBUTING.md](CONTRIBUTING.md) to get started.
