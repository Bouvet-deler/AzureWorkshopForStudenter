## Azure Playlist Function Guide

# Requirements

- An Azure student account
- Python 3.9
- Visual Studio Code
- The Python Extension for Visual Studio Code
- The Azure function extension for Visual Studio Code, 1.8.1 or later
- The Azurite Function extension
- Spotify account (free or premium)

# Getting started

Go to this site and follow the steps until "Clean up the resources"

- https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators

# Getting started with Spotify

1. Go to https://developer.spotify.com/
2. Log in with your Spotify account
3. Go to Dashboard, click on Create an app button and enter the following:
   - App Name: My App
   - App Description: This is my first Spotify app
   - Website: The url where your Azure function runs, in Azure. You can find it in the Azure Portal, in the funciton app.
     Example: https://the_name_of_your_function_app.azurewebsites.net/api/http_trigger
   - Redirect URI: Same as website
   - Which API/SDKs are you planning to use: Web API
4. Save 
5. Dashboard => Click on your app => Settings
   In settings you can find the Client ID and Client secret you will need to connect you Azure function to Spotify.

# Connecting your Function App with Spotify

1. Copy the code from function_app.py and paste it into your function_app.py file.
2. In the terminal: pip install spotipy
3. In the requirements.txt file add this line: spotipy
4. In function_app.py:
   - Remove the generated text.
   - Replace the code with the code found at: Azure-function-Playlist/function_app.py 
6. Replace the client_id with your ClientID from Spotify
7. Replace the client_secret with your Client secret
8. Replace the redirect_uri with your own URI
9. Run the app through pressing F5 or the Run and Debug icon in the left-hand side Activity bar.

# Upload the updated code to Azure

1. Click on the Azure icon on the left side menu
2. Click on the Azure Function icon under Workspaces, click on Deploy to Function App
3. Choose your subscription, the correct resources and functions.
4. Click on Deploy
