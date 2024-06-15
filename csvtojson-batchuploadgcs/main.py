import csv
import json
import requests # to get image from the web
import shutil # to save it locally
import os
from google.cloud import storage

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}

    image_folder = 'images'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    
    # Imports the Google Cloud client library
    client = storage.Client()

    # Instantiates a bucket
    bucket_name = "somethingaldieric"
    bucket = client.get_bucket(bucket_name)

    cstorage_base_url = f"https://storage.googleapis.com/{bucket_name}/"
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        i = 1
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = "R" + str(i)

            # download image
            url = rows['Image']
            savefile = url.split("/")[-1]
            filename = os.path.join(image_folder, url.split("/")[-1])

            r = requests.get(url, stream = True)

            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
                
                # Open a local file with wb ( write binary ) permission.
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    
                print('Image sucessfully Downloaded: ',filename)
            else:
                print('Image Couldn\'t be retreived')
            
            # uncomment this if you're on windows
            filename = filename.replace(os.sep, '/')
            print(filename)

            # Upload to bucket
            blob = bucket.blob(filename)
            blob.upload_from_filename(filename)

            # change Image url
            rows['Image'] = cstorage_base_url + filename

            temp = rows['Ingredients']
            templist = temp.split(", ")
            rows['Ingredients'] = templist
            data[key] = rows
            i=i+1
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
csvFilePath = r'sample.csv'
jsonFilePath = r'output.json'

if __name__ == "__main__":
    print("program running")
    make_json(csvFilePath, jsonFilePath)