# Descscription
As of March 2024, [BloodHound CE](https://github.com/SpecterOps/BloodHound) does not feature an easy way of importing custom queries at scale. This small script solves that, by parsing a legacy BloodHound `customqueries.json` file and importing each query to a BloodHound CE instance using the `/api/v2/saved-queries` endpoint.

# Usage
```
python import-custom-bloodhound-queries.py --jwt eyJhbGciOiJIUz... [--host localhost] [--port 8080] [--file ./customqueries.json]

options:
  -h, --help   show this help message and exit
  --jwt JWT    Required: The JWT used for authentication. Open the Network tab of your browser after authenticating to BloodHound.
  --host HOST  Optional: Bloodhound host. Default is localhost.
  --port PORT  Optional: BloodHound port. Default is 8080.
  --file FILE  Optional: path to JSON file containing custom queries. Default is ./customqueries.json.
```