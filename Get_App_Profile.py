import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###### prepare the URL #####
url= "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

##### credentials #####
payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}

##### headers #####
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

##### Parse the Token and Set COOKIE #####

toekn = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookie = {}
cookie["APIC-cookie"] = toekn

##### GET APPLICATION PROFILE #####
url_profile = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

headers = {
    "cache-control": "no-cache"
}

response_profile = requests.get(url_profile, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(response_profile, indent=2, sort_keys=True))