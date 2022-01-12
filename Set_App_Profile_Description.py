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

##### SET APPLICATION PROFILE  Description#####
url_profile = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

headers = {
    "cache-control": "no-cache"
}

post_payload = {
    "fvAp": {
        "attributes": {
          "descr": "Save the planet edited by Python",
          "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }

}

response_set_desc = requests.post(url_profile, headers=headers, cookies=cookie, data=json.dumps(post_payload), verify=False).json()


response_profile = requests.get(url_profile, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(response_profile, indent=2, sort_keys=True))