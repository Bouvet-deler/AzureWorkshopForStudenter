# Tutorial

Welcome!

In this tutorial, we will use Python and the web framework FastAPI to upload a file to a blob storage container that is within an Azure Storage Account.

## Prerequisite

There are few things that we have to install before we start this tutorial.

1. [Visual Studio Code](https://code.visualstudio.com/download)
2. An Azure account with some dineros (this will be provided for you)
3. [Python 3.10 or higher](https://www.python.org/downloads/release/python-31011/) (link is for 3.10.11)
4. [Git](https://git-scm.com/downloads)

## Important links

Some links that can be important to remember/keep open

- [Azure portal](https://portal.azure.com/#home)
- [GitHub repository for this tutorial](https://github.com/Burhan-Mohammad-Sarfraz/upload-file-to-azure-blob-storage-with-python-and-fastapi-and-azure-functions/tree/main)

## Create a workspace

First and foremost, we need to create a workspace.

Create a folder whereever you like with an appropriate name, such as _Bouvet-bedpres-2024_.

Open Visual Studio Code (referred to as VSCode) and open the folder you created inside VSCode (CTRL+K+O on Windows and CMD+O on Mac). Create a Python file (CTRL+N on Windows and CMD+N on Mac) inside the folder and name it _upload_file_to_azure_storage.py_.

In the GitHub repository, there is a file named _requirements.txt_. Download that file and put it inside your workspace folder.

## Enter the world of Azure

There are a few things we need to do in Azure before we can start to code. Open Azure portal link under [Important links](#markdown-header-important-links)

Here, you will see this beautiful website

![Azure portal home page](/docs/images/azure_portal.png)

There are a multitude of things that you can do, but we will do two thing; create a Azure Resource Group and Azure Storage Account

### Create Azure Resource Group

Azure Resource Group is a collection of resources. Usually, a resource group contains resources that have something to do with eachother. But, you might wonder; what is a _resource_? A resource can be though of as a service that Azure provides for you. One resource that Azure provides, that you might have heard of is virtual machines. Instead of having to use your computer's hardware to run a virtual machine, Microsoft uses its computers, or rather servers, to host a virtual machine for you. You only need to create it based on your needs and install the software and tools that you need.

So, lets start by creating a resource group. From the home page you can see that on the top of the screen, next to the large **+** icon, there is a Tesseract like object that says Resource groups. Click on it (and the world will not end).

Now you are transported to a rather empty page. At the top right corner, under the header Resource groups, there is a button that says **+ Create**. Press it.

This reveals a new, scary page. Give the Resource group a name, in the field called **Resource group**. You can name it something like _Bouvet-bedpres-2024_. Under **Region**, choose _Norway East_. Press the **Review+Create** at the bottom left of the screen, and you will see a new page. If it says at the top of the screen Validation passed with a green check next to it, press the **Create** button at the bottom. If a red cross comes up with the message _Validation failed. Required information is missing or not valid_, then press the **Previous** button twice and rename the resource group until it becomes green.

Great, you have now created a resource group in which you can store your resources. Lets create an Azure Storage Account inside this resource group.

## Create Storage Account and configure it

Now that you have created your Resource Group, you are sent to this page

![Azure portal after resource group creation](/docs/images/azure_portal_after_resource_group_creation.png)

Press on the resource group that you just created. We are now inside the resource group and here, we will create an Azure Storage Account.

A Storage Account is an account that contains all of the storage possibilities that Azure provides. If has various storage types, and the one we will use is called _blob storage_. Blob storage is an unstructured storage that can contains millions of files. Thing of it as your Downloads folder, where everything you have downloaded from the internet is. If you dont empty it often, or at all, it becomes unstructered with many different types of files. Blob storage is similar to that.

Now, you should have this page open in Azure portal

![Azure portal create resource](/docs/images/azure_portal_create_resource.png)

Click on the blue button on the middle of the screen that says **Create resources**. From there, if you cannot see Storage account as one of the options, search **Storage account** in the search field. It has an image of a table with a green background. Click on it. In the appearing page, click on the blue button named **Create**.

A new page arrives, which looks like this

![Azure portal create storage account](/docs/images/azure_portal_create_storage_account.png)

Double check that the resource group that you created previously is named in the **Resource group** field. Fill out the **Storage account name** field, with **ONLY** lowercase letters and numbers. Make sure that the **Region** field is set to _Norway East_. Leave everything else as is and press the blue button at the bottom named **Review**. Then, when it becomes blue, press the button named **Create** on the next page that comes up.

Great, we have now created our storage account. It takes a little time before it has been created, but at the page you are now, a blue button below the Deployment details named **Go to resource** will appear when it has created the storage account. When the button appears, press it.

From here we need to ensure that the storage account is accessible to us, i.e., we need to make sure that public access is allowed. As of now, the storage account cannot be accessed by others.

After you pressed the blue **Go to resource** button, you should be on a page like this

![Azure portal storage account home page](/docs/images/azure_portal_storage_account_home_page.png)

On the middle of the page to the right, there is a small headliner that says Security. Click it and many options appear. Under the **Allow Blob anonymous access** field, choose the Enabled radio button, then click on Save at the top of the page. After that, press the **Overview** button that is the top option on the left side.

This concludes what we needed to do in the Azure Portal. We will return to make sure that our Python Script works, so for now I would recommend that you keep the Azure portal tab open.

## Create a virtual environment in VSCode

To ensure that we don't destroy anything, we will create a virtual Python environment inside our workspace. This ensures that we use a isolated instance of Python and can control which packages are installed and used. The tutorial gives instructions for Mac and Windows.

Open VSCode if you closed it, and open the empty file that we created earlier. Then, open the Terminal inside VSCode and type

Windows

```
python -m venv venv
```

macOS

```
python3 -m venv venv
```

**NB! I am not completely sure if you have to type python3 on newer macOS, but I know that you had to previously.**

Now, if you downloaded the Python extension inside VSCode, you will get a prompt from VSCode at the bottom right that says _We noticed a new environment has been created. Do you want to select it for the workspace folder?_. Press yes and it automatically picks the version of Python that is from the newly created virtual environment.

Now, to activate the virtual environment inside the terminal you type

Windows

```
.\venv\Scripts\activate
```

macOS

```
source venv/bin/activate
```

Your virtual environment is now active! To double check that it has been activated, you can see that there is a (venv) behind the computer name on Windows, and on macOS you can type

```
which python3
```

and the path which is returned should be the same as your workspace path.

Now, we need to install the required packages. Type the following in the terminal

Windows

```
python -m pip install -r .\requirements.txt
```

macOS

```
python3 -m pip install -r requirements.txt
```

This should install a bunch of packages, which is a good sign. Now, we can actually do some coding!

## The fun part

Now, we can try and make our code.

Firstly, we need to import the packages we just installed.

We start by adding some imports

```
#!/usr/bin/env python3

from azure.storage.blob.aio import BlobServiceClient, ContainerClient
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
```

The top comment is called a _shebang_ and is there to specify which Python version we are using, in case both Python 2 and 3 are installed. The first import is for accessing the storage account we created in Azure, and the imports from FastAPI are for creating the website we will use to upload the images.

Next, we need to initialise the FastAPI web framework by typing

```
# Initialise the FastAPI app.
app = FastAPI()
```

This initialisation creates an app object from the Python script.

Next, we create our first function, which gets the image and uploads it to our Azure Storage Account.

```
# A function that gets the file that shall be uploaded to the our newly created Azure Storage Account.
@app.post('/uploadfile')
async def get_file_for_upload(file: UploadFile):
    filename = file.filename
    return await upload_file_to_azure(file, filename)
```

To explain what is means;

Firstly, we say that this function performs a HTTP POST method with `@app.post()`, which indicate that we are sending data from the website to the server. `('/uploadfile')` is the page url that for the POST method. Then, we define the function with a parameter named _file_, which is the file that we want to upload. The file has the type _UploadFile_, which comes from FastAPI.

The function is _async_, meaning that we can use _await_ to ensure that code is run in the correct order. This is needed, because some actions inside the code has to be run before others. Otherwise, the function doesn't do much except call another function that contains the logic behind uploading the file.

The next function that we need is

```
# A function that uploads the file to our Azure Storage Account.
async def upload_file_to_azure(file: UploadFile, filename: str):
```

This is the actual function where the magic happens. The function has the file we want to upload and the file name as parameters.

First, we need to try and connect to the storage account that we created earlier by doing so

```
try:
    # Connect to the Storage Account in Azure.
    connection_string_for_storage_account = "<CONNECTION_STRING>"
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string_for_storage_account)
```

Now, we need to go back to the Azure portal. From there, we need a _connection string_, that is used for connecting to our storage account. In the Azure Portal (hopefully you did not close the page from last time, and if you did, go back to see how you can find your storage account) on the left side, press the **Access keys** under **Security + networking**. From there, press the **Show** button that is next to **Connection string** field under **key1**. Copy that string and replace `"<CONNECTION_STRING>"` in your code. Remember to keep the `""`around the string.

The _blob_service_client_ is using the function that comes with the azure-blob-storage package to connect to the storage account via the connection string.

**To quickly explain try/except statement**. It essentially is a try and fail approach. In the try block, Python will try and perform the code. It is fails somewhere in the code, it will automatically go to the except statement (which is coming later), and display the error that occured.

From there, we can create a container inside our storage account where we will actually store our files. Type this in the file, and **remember to keep it inside the try statement**

```
    # Create a container inside the Storage Account.
    container_name = "<ENTER_CONTAINER_NAME_OF_CHOICE"
    container_client = ContainerClient.from_connection_string(conn_str=connection_string_for_storage_account, container_name=container_name)
    if await container_client.exists():
        pass
    else:
        container_client = await blob_service_client.create_container(name=container_name, public_access='blob')
```

So, here we are creating a container with a appropriate name. Container name rules are:

- Container names must start or end with a letter or number, and can contain only letters, numbers, and the hyphen/minus (-) character.
- Every hyphen/minus (-) character must be immediately preceded and followed by a letter or number; consecutive hyphens aren't permitted in container names.
- All letters in a container name must be lowercase.
- Container names must be from 3 through 63 characters long.

Then we connect to that container with the same _connection string_ for our storage account and with the container name that we chose. Then, we have a check that says if the container exists, we will not create it again, because that will result in an error. If the container does not exist, we create it.

Type this in the function and remember to be **keep it inside the try statement**

```
# Try to upload the file to our newly created container inside our storage account.
    try:
        blob_client = container_client.get_blob_client(filename)
        file_to_upload = await file.read()
        await blob_client.upload_blob(file_to_upload)
    except Exception as ex:
        print("Exception: ", ex)

    return f"Your file has been uploaded to your Storage Account in Azure. It is stored inside the container named '{container_name}'"
```

Now, we can actually do what we want; **to try and upload our file to the storage account and specified container**

Here, we get the container that we just created and in an orderly fashion, we are trying to read in the file data and upload it to the container that we created. If this fails in some way, Python will give us an error message which contains the error that occured. If everything goes as planned, we will get the message that is returned on a new webpage that has the _/uploadfile/_ path in the URL.

And lastly for this function, we need to have a except statement for the try statement we had in the start

```
except Exception as ex:
    print("Exception: ", ex)
    return HTTPException(500, "Something went wrong...")
```

That is the code that connects to the storage account, creates a container and tries to upload a file to it.

Lastly, we need to add some HTML code to make a basic, ugly HTML webpage that we can use as our frontend and GUI

```
@app.get('/')
async def main():
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
```

Now, lets try and see what happens when we run the Python program!

## Run this thing

So, in VSCode, this can be ran in two different ways;

- While having the Python file open, press the start/play/run button in the top right corner.
- Type in the terminal _uvicorn <filename>:app --reload_, which becomes `uvicorn upload_file_to_azure_storage:app --reload`.

In the terminal, the output will be something similar to this (the IP address and port might be different)

```
INFO:     Started server process [11448]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Copy and paste the link into a browser's address bar, or hold CTRL (CMD on macOS) and left click the address inside the terminal.

This will open a webpage that looks like this

![FastAPI webpage](/docs/images/fastapi_webpage.png)

Here, let us try and upload a file to our container in Azure. Choose a file and click on submit, and if you get this webpage back

![FastAPI completed upload](/docs/images/fastapi_completed_upload.png)

Then you have done it! **Congratulations, you have uploaded a file to Azure**.

Pretty cool, right? Maybe not, I dont know, but I find it interesting that there is a file in the clouds that you have uploaded, but don't really know where is....

Anyway, if we go back to the Azure portal (if you closed it again, shame on you) and press the **Container** button on the left side under **Data storage**, you will get a list of all the containers that have been created inside your storage account. In that list, there should be a container with the name you specified in our code. If you click on that container, there should be a file, which is the file that you uploaded! If you click on the file and choose **Edit**, four options to the right of **Overview** in the pop-up window, you will see the file that you uploaded. If it is a image, you will se the image and if it is text or code, than that will appear.

Now, this code is running on your computer. Which means that you have to start it every time you want to upload a file to Azure, but what if I told you that there is a way to use Azure Functions to make sure that everything continuously runs in the cloud? Let's have a look at that now, if you are up for it!

## Azure Functions

Firstly, lets stop the locally running code by pressing CTRL+C (CDM on macOS) in the terminal.

What is Azure Functions? Azure Functions is something that runs your code for you based on some events or triggers. It is not run locally on your machine (but we will start with that), it uses the capabilities of the cloud to run the code.

So, let us begin! For this we will use the same workspace, so keep everything as is.

## Install Node.js

For this, we need to install [Node.js](https://nodejs.org/en/download).

## Install more extensions

To do this, we need some extensions in VSCode. If you install the extension **Azure Functions**, you should get **Azure Resources** and **Azure Account** too. Additionally, install **Azure Storage**.

## Create local Azure Function

Now, on the right sidebar you should see what looks like a big A, or the Azure logo, as some would call it. Click on it and it will give you to divided groups. **RESOURCES**, which are the resources in Azure (the cloud) and **WORKSPACE**, which are your local resources. We will start by making our Azure Function locally, then deploy it into Azure.

Next to the workspace title, there is a lightning icon, click on it and choose _Create Function..._. From there, choose these options

- Select the folder that you are in, it should come up as an option below the _Browse_ option.
- Select _Python_.
- Select _Model V2_.
- Select _HTTP trigger_.
- Press enter on the default name that appears.
- Select _ANONYMOUS_.

A window will pop-up asking if you want to overwrite the existing _requirements.txt_ and _.gitignore_ files. Choose **not** to do so.

If you look inside the directory, there are now many new files, where the most important is _function_app.py_. This is the file that Azure Functions will run.

Remove everything that is insde the _function_app.py_ file and replace it with

```
import azure.functions as func

from src.upload_file_to_azure_storage import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
```

Here, we tell the Azure Function to use the FastAPI web framework from the other Python file as the main file to run. If you have called your file something else than replace _upload_file_to_azure_storage_ with the name of your file.

Now, we need to make a change to the _host.json_ and add that the function should run on a http trigger, which is what we choose as the event on which the Azure Function will run the code.

The _host.json_ file looks like this

```
{
  "version": "2.0",
  "logging": {
    "applicationInsights": {
      "samplingSettings": {
        "isEnabled": true,
        "excludedTypes": "Request"
      }
    }
  },
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[3.*, 4.0.0)"
  }
}
```

and with our addition, it looks like this

```
{
  "version": "2.0",
  "logging": {
    "applicationInsights": {
      "samplingSettings": {
        "isEnabled": true,
        "excludedTypes": "Request"
      }
    }
  },
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[3.*, 4.0.0)"
  },
  "extensions": {
    "http": {
      "routePrefix": ""
    }
  }
}
```

Now, we can run our Azure function locally!

## Run Azure Function locally

Firstly, we need to sign in. Press on the **Azure logo** on the left side and under **RESOURCES** in the Azure extension, press **Sign in to Azure...** and follow the steps.

When you have signed in, press F5 while having the _function_app.py_ file open and active (on some computers, you might have to press the **fn** button to do so). First, a pop-up window will appear that says _you must have Azure Functions Core Tools installed_. Press install on the pop-up window. Secondly, a pop-up window will appear asking you to connect a storage account. Press **Connect Storage Account**, and choose the storage account that you created earlier from the list. The list should contain one storage account.

Then, a lot of terminal stuff happens and the bar at the bottom of VSCode turns red (it does for me at least), and you can see some text inside the terminal that says

```
Found Python version 3.10.11 (py).

Azure Functions Core Tools
Core Tools Version:       4.0.5390 Commit hash: N/A  (64-bit)
Function Runtime Version: 4.25.3.21264

[2023-10-04T13:47:19.321Z] Worker process started and initialized.

Functions:

        http_app_func: [GET,POST,DELETE,HEAD,PATCH,PUT,OPTIONS] http://localhost:7071//{*route}

For detailed output, run func with --verbose flag.
[2023-10-04T13:47:24.842Z] Host lock lease acquired by instance ID '0000000000000000000000003C99FC0C'.
```

If a pop-up window similar to the image below appears

![Azure Function error when starting deployment](/docs/images/azure_function_error_when_starting.png)

Then you can press **Debug Anyways**

Just like earlier, copy and paste the URL into a browser or hold CTRL (CMD on macOS) and click on the link.

The webpage that you are seeing is probably saying something like **This localhost page can't be found**. That is fine. If we look at the URL, it is kind of wierd. Remove everything after 7071, **except** for one backslash, so the URL becomes http://localhost:7071/ (remember, that your URL might be different). I usually do this inside the browser.

And look at that, the same webpage as earlier appears. Lets try and upload a file again and verify by going to the Azure portal to see that the file has been uploaded inside your container.

**Great, you have now created an Azure Function!** Let's deploy it to Azure.

## Deploy Azure Function to Azure

Make sure that the Azure function is still running. Inside VSCode, press the Azure extension from the sidebar and press the big **+** next to the **RESOURCES** title. Then choose **Create Function App in Azure...**. Then, do the following

- Give it a cool name
- Choose _Python 3.10_ (**NB! I assume that you have downloaded the Python version that I listed under Important links. If not, choose the Python version you are using**)
- Select _Norway East_

What did we just do? We created a Azure Function App, that can contain many functions for different purposes. So, it is into this Function App that we are storing the function we just made. When the Function app has been created, a small notification window will appear on the bottom right side of VSCode. If you press the blue **View Output** button, you will see an **Output**. In there, you can see the URL that links to the function app we just created. The URL is the last line in the **Output** window. If you copy and paste that into the browser, you'll get a cool looking webpage that says _You Functions 4.0 app is up and running_.

Now, go down to **WORKSPACE** inside the Azure extension. Left click on the lightning icon next to the **WORKSPACE** title and press **Deploy to Function App...**. Choose the function app we just created and press **Deploy** on the pop-up window that appears. If you have the **Output** window open, you will see that we have started to deploy our Function App to the cloud (Azure). When the deployment is completed, a small notification will appear in the right bottom corner. Here, you can press the grey button named **View Output**.

We have now deployed our Azure Funtion to the cloud! If you press on the key that is under **RESOURCES**, then **Function App** &#8594; **<YOUR_FUNCTION_NAME_APP>** &#8594; **Functions**, you'll see that the function app that we had locally is now in the cloud. Go back into the **Output** tab, and copy the link that is at the bottom, it looks something like this, but with your function app name instead.

```
http_app_func: https://bouvet-function-app.azurewebsites.net//%7B*route%7D
```

Press CTRL+C (CMD on macOS) to turn off the locally running function app and paste the URL above into the browser. **Remember** to remove everything after and including the `//` in the URL. It might take a minute before the above URL is active.

And what do you see? The same webpage that we had when we were running locally! Now, try and upload another file and verify that the file has been uploaded to your container in the storage account.

**AND IT HAS! CONGRATULATIONS, you have created a web framework using FastAPI in Python that is 100% running in the cloud**.

## Clean up

It is always smart to delete unused resources, as they might be spending your dinerios. The awesome thing with Azure, is that if you delete a resource group, all the resources within that group is also deleted.

So, you have left the Azure portal, go back to it or if you still have it open, press the **Microsoft Azure** name at the top right of the page. Click on **Resource groups** and now you might see that there are two resource groups. One which we created in the begining and another one, which is the one that has been created when we deployed our function app to the cloud. Now we have our function app in one resource group and storage account and blob container in another group. Since it it possible to move resources between resource groups, this is not a big issue. Just remember to clean up afterwards and move the resources around to make it as you wish, or start by creating the function app in Azure first and then work on it locally.

Click on the resource group that you made want to delete. To the right of the **+ Create** button, there is a button with a trash can named **Delete resource group**. Press that, and you will get a pop-up window that shows all the resources in the resource group. Copy the resource groups name and paste it at the bottom of the pop-up window and press delete. This process might take some time, but you will get a notification when it has completed. You can delete multiple resource groups at the same time, so just go to the other resource group and delete that as well. You can go back by pressing the **Microsoft Azure** name at the top right (even while it is deleting the resource group(s)). If you click on **Resource groups** after the receiving the notification, the resource group(s) are gone and so are all the resources.

If you want to doublecheck that your resources are gone, press the big yellow key named **Subscriptions** and select the subscription that is in the list. In the navigation bar on the left, go down to _Settings_ and press **Resource groups** to see that it is empty. Then, press **Resources** to see that it is also empty, i.e., both resource groups and corresponing resources have been deleted.

I hope you enjoyed this tutorial!
