import requests
from django.conf import settings

BASE_URL = settings.CASHFREE_PAYOUT_BASE_URL
CLIENT_ID = settings.CASHFREE_CLIENT_ID
CLIENT_SECRET = settings.CASHFREE_CLIENT_SECRET

def get_auth_token():
    """ Get authentication token from Cashfree """
    url = f"{BASE_URL}/authorize"
    headers = {"Content-Type": "application/json"}
    payload = {
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("token")
    return None

def add_beneficiary(user):
    """ Register a seller as a Cashfree beneficiary """
    token = get_auth_token()
    if not token:
        return {"status": "error", "message": "Failed to get auth token"}

    bank_details = user.bank_details
    if not bank_details:
        return {"status": "error", "message": "No bank details found"}

    beneficiary_id = f"ben_{user.id}"
    url = f"{BASE_URL}/addBeneficiary"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "beneId": beneficiary_id,
        "name": bank_details.account_holder_name,
        "email": user.email,
        "phone": "6281650290",  # Replace with actual phone
        "bankAccount": bank_details.account_number,
        "ifsc": bank_details.ifsc_code,
        "address1": "Seller Address",
        "city": "City",
        "state": "State",
        "pincode": "123456"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        bank_details.cashfree_beneficiary_id = beneficiary_id
        bank_details.save()
        return {"status": "success", "message": "Beneficiary added"}
    return response.json()
