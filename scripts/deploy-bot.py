#!/usr/bin/env python3

import requests
import argparse
import json
import os

# API key used to authenticate with the InsightCloudSec API
API_KEY = os.getenv("API_KEY")

# Base URL and endpoint for the InsightCloudSec API
BASE_URL = "https://sedex.customer.divvycloud.com/v2/"
ENDPOINT = "public/botfactory/bot/create"
URL = BASE_URL + ENDPOINT

# Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', required=True, help="Name of the JSON config file (without path)")
args = parser.parse_args()

# Compute full path to config file
script_dir = os.path.dirname(os.path.realpath(__file__))  # scripts/
config_path = os.path.join(script_dir, '..', 'configuration-files', args.config)

# Load the JSON payload
with open(config_path) as f:
    config = json.load(f)

# Define headers with API key
headers = {
    "Content-Type": "application/json",
    "Api-Key": API_KEY
}

# Make the API request
response = requests.post(URL, headers=headers, json=config)

# Output results
print("Status Code:", response.status_code)
print("Response Body:", response.text)