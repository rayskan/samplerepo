# Learning python strings

username="ray"
password="mypass"
response = requests.get("https://api.open-notify.org/astros.json?user"+username+"&pwd="+password)
print(response.status_code)