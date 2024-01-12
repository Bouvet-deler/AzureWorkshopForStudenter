## Azure Playlist Function Guide

# Requirements 
- An Azure student account with 
- Python 3.9
- Visual Studio Code
- The Python Extention for Visual Studio Code
- The Azure function extention for Visual Studio Code, 1.8.1 or later
- The Azurite Function extention
- Spotify account (free or premium)


# Getting started
Go to this site and follow the steps until "Clean up the resources"
- https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators


# Getting started with Spotify
1. Go to https://developer.spotify.com/
2. Log in with your Spotify account
3. Go to Dashboar, click on Create an app button and enter the following:
    - App Name: My App
    - App Description: This is my first Spotify app
    - Website: The local host for your Azure function. Find it by running your Azure Funciton: Run -> Start Debugging. In the terminal you can find the correct URL
    - Ridirect URI: Equal as website
    - Which API/SDKs are you planning to use : Web API
4. Save
5. Dashboard => Click on your app=>  Settings 
In settings you can find the Client ID and Client secret you will need to connect you Azure function to Spotify. 


# Connecting your Function App with Spotify
1. Copy the code from example_code.py and paste it into the file function_app.py. 
2. In the terminal: pip install spotipy
3. Replace the client_id with your ClientID from Spotify
4. Replace the client_secret with your Client secret
5. Replace the redirect_uri with your own URI
6. Run the app


# Upload the updated code to Azure
1. Click on the Azure icon on the left sidemenu
2. Click on the Azure Function icon, click on Deploy to Function App
3. Choose your subscription and the correct resources and functions.  
4. Click on Deploy