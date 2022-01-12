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

##### show the result and parse the Token and Set COOKIE #####
print(json.dumps(response, indent=2, sort_keys=True))

toekn = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookie = {}
cookie["APIC-cookie"] = toekn


url_tenant = "https://sandboxapicdc.cisco.com/api/class/fvTenant.json"

headers = {
    "cache-control": "no-cache"
}

response_tenant = requests.get(url_tenant, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(response_tenant, indent=2, sort_keys=True))