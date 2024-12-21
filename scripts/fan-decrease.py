import requests

# Home Assistant URL and API Token
home_assistant_url = "http://localhost:8123"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmOWI1ODJiNmU2ZWE0NTE0ODllYTM3ODNkM2Y4MjBiZCIsImlhdCI6MTczNDgxOTE1OSwiZXhwIjoyMDUwMTc5MTU5fQ.YiUBTj8e1BJEFAddfU1QG0eiY6kavd-dhwF3wP9UW64"

# The API endpoint for scripts
url = f"{home_assistant_url}/api/states"

# Headers for Authorization (Bearer Token)
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}

# Send the GET request to Home Assistant
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON and filter for scripts
    data = response.json()
    
    # Print all the entities that are scripts
    scripts = [entity for entity in data if entity['entity_id'].startswith('script.')]
    
    if scripts:
        print("List of available scripts:")
        for script in scripts:
            #print(f"- {script['entity_id']}: {script['attributes'].get('friendly_name', 'No friendly name')}")
            print(script)
    else:
        print("No scripts found.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)


############################################################    

# The API endpoint for the script service
script_name = "skyfan1_decreasespeed"
url = f"{home_assistant_url}/api/services/script/{script_name}"
# Data (if needed) - If your script does not require parameters, leave this empty
#data = "{'entity_id': skyfan1_decreasespeed}"
data = ''

print(url)
# Send the POST request to Home Assistant to call the script
response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print(f"Script '{script_name}' executed successfully.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)