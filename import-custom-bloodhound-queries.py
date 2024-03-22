import json
import requests
import argparse

def parse_queries(file='./customqueries.json'):
    with open(file, 'r') as file:
        data = json.load(file)
    
    parsed_queries = {}
    for query in data['queries']:
        parsed_queries[query['name']] = query['queryList'][0]['query']
    
    return parsed_queries

def send_requests(parsed_queries, jwt, host, port):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % (jwt)
    }
    for name, query in parsed_queries.items():
        payload = {
            "name": name,
            "query": query
        }
        try:
            response = requests.post(f'http://{host}:{port}/api/v2/saved-queries', json=payload, headers=headers, verify=False)
            if response.status_code == 201:
                print(f"Successfully created query: '{name}'")
            else:
                print(f"Failed to create query: '{name}' with error code {response.status_code}")
        except Exception as e:
            print(f"Error occurred while sending request for '{name}': {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Import custom queries into BloodHound CE from a legacy BloodHound JSON file.', usage='python import-custom-bloodhound-queries.py --jwt eyJhbGciOiJIUz... [--host localhost] [--port 8080] [--file ./customqueries.json]')
    parser.add_argument('--jwt', type=str, required=True, help='Required: The JWT used for authentication. Open the Network tab of your browser after authenticating to BloodHound.')
    parser.add_argument('--host', type=str, default='localhost', help='Optional: Bloodhound host. Default is localhost.')
    parser.add_argument('--port', type=str, default='8080', help='Optional: BloodHound port. Default is 8080.')
    parser.add_argument('--file', type=str, default='./customqueries.json', help='Optional: path to JSON file containing custom queries. Default is ./customqueries.json.')
    args = parser.parse_args()

    parsed_queries = parse_queries(args.file)
    send_requests(parsed_queries, args.jwt, args.host, args.port)

if __name__ == "__main__":
    main()
