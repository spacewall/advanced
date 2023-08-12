from dotenv import dotenv_values

from ya_disk import YaFolderUploader

def make_folder(folder_name) -> str:
    config = dotenv_values(".env")
    TOKEN = config["TOKEN"]
    folder_uploader = YaFolderUploader(TOKEN)

    responce = folder_uploader.make_folder(folder_name)

    return responce.status_code

def delete_folder(folder_name, TOKEN=None) -> str:
    if TOKEN is None:
        config = dotenv_values(".env")
        TOKEN = config["TOKEN"]

    folder_uploader = YaFolderUploader(TOKEN)

    responce = folder_uploader.delete_folder(folder_name)

    return responce.status_code

if __name__ == "__main__":
    print(make_folder("test"))
    print(delete_folder("test"))