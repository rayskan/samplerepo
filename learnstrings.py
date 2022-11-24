# Learning python strings

uid="ray"
password="mypass"
response = requests.get("https://api.open-notify.org/astros.json?user"+uid+"&pwd="+password)
print(response.status_code)