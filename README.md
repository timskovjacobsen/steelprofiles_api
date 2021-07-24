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

* `GET /api/{profile_type}`  
  E.g. to get data for all **HEA** profiles, visit `steelapi.timskovjacobsen.com/api/hea`

* `GET /api/{profile_type}/{dimension}`  
  E.g. to get data for the profile **HEA120**, visit `steelapi.timskovjacobsen.com/api/hea/120`

It's possible to use uppercase profile names in the URL, like HEA.

## API Docs

The swagger [API Docs](http://steelapi.timskovjacobsen/docs) for more info.
