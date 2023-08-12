import requests

class YaFolderUploader:
    def __init__(self, token: str) -> None:
        self.headers = {
            "Authorization": f"OAuth {token}",
            "Content-type": "application/json"
        }
    
    def make_folder(self, folder_name: str) -> requests.Response:
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": folder_name}

        responce = requests.put(url=upload_url, headers=self.headers, params=params)

        return responce
    
    def delete_folder(self, folder_name: str) -> requests.Response:
        url_for_delete = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": folder_name}

        responce = requests.delete(url=url_for_delete, headers=self.headers, params=params)

        return responce
