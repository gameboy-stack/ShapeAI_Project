import requests as re


req = re.get("https://github.com/gameboy-stack/ShapeAI_Project")


print(req.status_code)

#change