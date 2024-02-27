## Azure Playlist Function Guide

# Requirements 
- An Azure student account with 
- Python 3.9
- Visual Studio Code
- The Python Extention for Visual Studio Code
- The Azure function extention for Visual Studio Code, 1.8.1 or later
- The Azurite Function extention
- Spotify account (free or premium)
- installed spotipy and azure-functions:

``` 
$ pip install spotipy
$ pip install azure-functions
```


# Getting started
Go to this site and follow the steps until "Clean up the resources"
https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators


# Getting started with Spotify
1. Go to https://developer.spotify.com/
2. Log in with your Spotify account
3. Go to Dashboard, click on Create an app button and enter the following:
   - App Name: My App
   - App Description: This is my first Spotify app
   - Website: The local host for your Azure function. Find it by running your Azure Funciton: Run -> Start Debugging. In the terminal you can find the correct URL. Also available on your azure functions dashboard
      Redirect URI: Equal as website e.g https://<YOUR_WEBISTE_NAME>.azurewebsites.net/api/spotify
   - Redirect URI: Same as website
   - Which API/SDKs are you planning to use: Web API
4. Save 
5. Dashboard => Click on your app => Settings
   In settings you can find the Client ID and Client secret you will need to connect you Azure function to Spotify.


# Connecting your Function App with Spotify
1. In the terminal: pip install spotipy
2. In the requirements.txt file add this line: spotipy
3. In function_app.py:
   - Remove the generated text.
   - Replace the code with the code found at: Azure-function-Playlist/function_app.py 
4. Replace the client_id with your ClientID from Spotify
5. Replace the client_secret with your Client secret
6. Replace the redirect_uri with your own URI
7. Run the app through pressing F5 or the Run and Debug icon in the left-hand side Activity bar.


# Upload the updated code to Azure
1. Click on the Azure icon on the left side menu
2. Click on the Azure Function icon under Workspaces, click on Deploy to Function App
3. Choose your subscription, the correct resources and functions.
4. Click on Deploy


# Further implementation with the use of Spotify API
- Further documentation on the Python Spotify library can be found at [https://spotipy.readthedocs.io/en/2.22.1/](https://spotipy.readthedocs.io/en/2.22.1/)
- You can also find more information at [https://developer.spotify.com/documentation/web-api](https://developer.spotify.com/documentation/web-api)
- There are also information found at: [https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50](https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50)


