import requests
import json

# Dummy values
controller_url = "https://avi-controller.local"
username = "dummy-user"
password = "dummy-pass"

# Disable warnings for demo (not recommended in production)
requests.packages.urllib3.disable_warnings()

# Authenticate
session = requests.session()
login_url = f"{controller_url}/login"
login_payload = {"username": username, "password": password}
resp = session.post(login_url, json=login_payload, verify=False)

if resp.ok:
    print("✅ Login Successful")

    # Create tenant
    tenant_url = f"{controller_url}/api/tenant"
    tenant_data = {
        "name": "test-tenant",
        "description": "Created via script",
    }
    create_resp = session.post(tenant_url, json=tenant_data, verify=False)

    if create_resp.ok:
        print("✅ Tenant Created")
        print(create_resp.json())
    else:
        print("❌ Failed to create tenant:", create_resp.text)
else:
    print("❌ Login failed:", resp.text)
