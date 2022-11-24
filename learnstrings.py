# Learning python strings

uid="ray"
pwd="mypass"
response = requests.get("https://api.open-notify.org/astros.json?user"+uid+"&pwd="+pwd)
print(response.status_code)