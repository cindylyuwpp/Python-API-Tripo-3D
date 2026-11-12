import requests
import time
from my_secret_api import MY_TRIPY_API_KEY

api_key = MY_TRIPY_API_KEY



headers = {
    "authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

rig_url = "https://openapi.tripo3d.ai/v3/animations/rig-check"

rig_data = {
    "input": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/Fox/glTF-Binary/Fox.glb"
}

response = requests.post(rig_url, headers=headers, json=rig_data)
if response.status_code == 200:
    data = response.json()
    task_id = data["data"]["task_id"]
else:
    print("Broken", response.status_code, response.text)
    exit()

task_url = "https://openapi.tripo3d.ai/v3/tasks/" + task_id

for i in range(20):
    response = requests.get(task_url, headers=headers)
    if response.status_code == 200:
        task = response.json()["data"]
        status = task["status"]
        print("Status:", status)
        if status == "success":
            break
        if status in ["failed", "cancelled", "banned", "expired"]:
            print("Task failed or cancelled")
            break
    else:
        print("Broken", response.status_code)
        break
    time.sleep(3)
        
if status == "success":
    output = task["output"]
    riggable = output["riggable"]
    rig_type = output["rig_type"]
    print("Can be rigged:", riggable)
    print("Rig type:", rig_type)

