# CSV -> Upload to GCS -> JSON
Download Image listed from a csv file, upload them to Google Cloud Storage, then export a JSON file for easier handling

## Introduction
This Python script converts a CSV file to a JSON file, downloads images from the web, and uploads them to a Google Cloud Storage bucket. The script uses the csv, json, requests, shutil, and google-cloud-storage libraries.

## Background
My cute juniors have this csv files after scraping the web. Since csv is slow and tedious to handle on nodejs, csv to json conversion is needed. In addition, image "proxy" is needed to ensure fast access to the media, hence the upload to Google Cloud Storage

## Prerequisites

- Python 3.x installed on your system
- Google Cloud account with a project set up
- Google Cloud Storage bucket created
- GOOGLE_APPLICATION_CREDENTIALS environment variable set with the path to your JSON key file (see [Google Cloud documentation](https://cloud.google.com/docs/authentication/getting-started) for more information)

## How to use
### Set up your Google Cloud environment

1. Run the following commands to authenticate with Google Cloud:
```bash
gcloud auth login
gcloud auth application-default login
```
2. Set your project ID:
```bash
gcloud config set project <project-id>
```
Replace <project-id> with your actual project ID.

### Run the script

1. Save this script as `csv_to_json.py` (or any other name you prefer).
2. Create a CSV file with the data you want to convert to JSON. The script assumes that the CSV file has a column named `Image` with URLs to download images.
3. Run the script with the following command:
```bash
python csv_to_json.py <csv_file_path> <json_file_path>
```
Replace <csv_file_path> with the path to your CSV file and <json_file_path> with the desired path for the output JSON file.

Example:
```bash
python csv_to_json.py sample.csv output.json
```
The script will convert the CSV file to a JSON file, download images from the web, and upload them to your Google Cloud Storage bucket.

## Note
Make sure to update the bucket_name variable in the script with your actual Google Cloud Storage bucket name.
