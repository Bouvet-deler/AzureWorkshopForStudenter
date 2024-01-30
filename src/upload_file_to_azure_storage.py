#!/usr/bin/env python3
"""A script that uploads a image to an Azure Storage Account."""

from azure.storage.blob.aio import BlobServiceClient, ContainerClient
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import HTMLResponse

# Initialise the FastAPI app.
app = FastAPI()


@app.post('/uploadfile')
async def get_file_for_upload(file: UploadFile):
    """A function that gets the file that shall be uploaded to the our newly
    created Azure Storage Account."""
    filename = file.filename
    return await upload_file_to_azure(file, filename)


async def upload_file_to_azure(file: UploadFile, filename: str):
    """A function that uploads the file to our Azure Storage Account."""
    try:
        # Connect to the Storage Account in Azure.
        connection_string_for_storage_account = "<CONNECTION_STRING>"
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string_for_storage_account)

        # Create a container inside the Storage Account.
        container_name = "blob-container-for-file-upload"
        container_client = ContainerClient.from_connection_string(conn_str=connection_string_for_storage_account, container_name=container_name)
        if await container_client.exists():
            pass
        else:
            container_client = await blob_service_client.create_container(name=container_name, public_access='blob')

        # Try to upload the file to our newly created container inside our storage account.
        try:
            blob_client = container_client.get_blob_client(filename)
            file_to_upload = await file.read()
            await blob_client.upload_blob(file_to_upload)
        except Exception as ex:
            print("Exception: ", ex)

        return f"Your file has been uploaded to your Storage Account in Azure. It is stored inside the container named '{container_name}'"
    except Exception as ex:
        print("Exception: ", ex)
        return HTTPException(500, "Something went wrong...")


@app.get('/')
async def main():
    """Starting point of the program."""
    content = """
    <body>
    <h1>Upload file to a container inside Azure Blob Storage</h1>
    <form action="/uploadfile" enctype="multipart/form-data" method="post">
    <input name="file" type="file">
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
