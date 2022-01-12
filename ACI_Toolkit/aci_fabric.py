import sys
import acitoolkit.acitoolkit as aci
APIC_URL = "https://sandboxapicdc.cisco.com"
USERNAME = "admin"
PASSWORD = "ciscopsdt"

SESSION = aci.Session(APIC_URL, USERNAME, PASSWORD)
RESP = SESSION.login()

if not RESP.ok:
   print("cloud not login to APIC")
   sys.exit()

ENDPOINTS = aci.Endpoint.get(SESSION)

print("{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}".format("MAC ADD", "IP ADD", "ENCAP","TENANT","PP PROFILE","EGP"))

print("-"*80)

for EP in ENDPOINTS:
    epg= EP.get_parent()
    app= epg.get_parent()
    tenant= app.get_parent()
    print("{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}".format(EP.mac, EP.ip, EP.encap, tenant.name, app.name, epg.name))