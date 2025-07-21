import requests

def upload_to_gofile(filepath: str) -> str:
    # Step 1: Get best server
    server_res = requests.get("https://api.gofile.io/getServer")
    if server_res.status_code != 200:
        raise Exception(f"Failed to get server: {server_res.text}")

    server = server_res.json()["data"]["server"]

    # Step 2: Upload file to that server
    upload_url = f"https://{server}.gofile.io/uploadFile"

    with open(filepath, 'rb') as f:
        files = {'file': f}
        response = requests.post(upload_url, files=files)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["downloadPage"]
    else:
        raise Exception(f"Upload failed: {response.status_code} - {response.text}")
