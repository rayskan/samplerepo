# Learning python strings

uid="ray"
p="mypass"
response = requests.get("https://api.open-notify.org/astros.json?user"+uid+"&pwd="+p)
print(response.status_code)