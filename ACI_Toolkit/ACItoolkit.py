from acitoolkit.acitoolkit import *

url= "https://sandboxapicdc.cisco.com"
user = "admin"
pwd = "!v3G@!4@Y"

#Create the session object
session = Session(url, user, pwd)

# Login to the session
session.login()

#Get tenants
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print("*"* 50)
    print(" ")


# Create a new Tenant
new_tenant = Tenant("Tenant_ACI_1")
#new_tenant.get_url
#new_tenant.get_json()

# Create the application profile and the EPG
anp = AppProfile("Aci_APP", new_tenant)
epg = EPG("Aci_epg", anp)

# Create the L3 Namespace
context = Context("Aci_VRF", new_tenant)
bridge_domain = bridgeDomain("ACI_bd", new_tenant)

#Associate the BD with L3 Namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)


#### Tenant Creation is completed ####
print(new_tenant.get_url())
print(new_tenant.get_json())
response= session.push_to_apic(new_tenant.get_url, data=new_tenant.get_json())

tenants = Tenant.get(session)
for tn in tenants:
    if tenant.name == "Tenant_ACI_1":
        print(tn.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print("*"* 50)
        print(" ")

new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url, data=new_tenant.get_json())