#!/usr/bin/env python3

# Import necessary libraries
import requests
import argparse
import json
import os

# API key used to authenticate with the InsightCloudSec API
API_KEY = os.getenv("API_KEY")

# Base URL for the InsightCloudSec API
BASE_URL = "https://sedex.customer.divvycloud.com/v2/"

# Specific API endpoint for creating a bot via the BotFactory
ENDPOINT = "public/botfactory/bot/create"

# Combine base URL and endpoint to get the full request URL
URL = BASE_URL + ENDPOINT

parser = argparse.ArgumentParser()
parser.add_argument('--config', required=True)
args = parser.parse_args()
# Load the JSON payload from a file
# This file should contain the bot configuration in JSON format
with open(args.config) as f:
    config = json.load(f)

# Define the HTTP headers, including the API key and content type
headers = {
    "Content-Type": "application/json",
    "Api-Key": API_KEY
}

# Make the POST request to the API with the headers and JSON payload
response = requests.post(URL, headers=headers, json=config)

# Output the HTTP status code to see if the request was successful
print("Status Code:", response.status_code)

# Output the response body for debugging or confirmation
print("Response Body:", response.text)
