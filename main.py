import requests 

API_TOKEN = "kvVDk6bPlZ8WE305dH5EqtcMTG8tf0RkCvzJIeqL"
url="https://api.cloudflare.com/client/v4/user/tokens/verify"

headers={
    "Authorization": f"Bearer {API_TOKEN}"
}

response=requests.get(url=url,headers=headers)
print(response.status_code)
print(response.json())