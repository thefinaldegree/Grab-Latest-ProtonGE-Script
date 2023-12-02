#!/usr/bin/env python3

from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import os
import re
import tarfile

#################################################################################################
###	User Settings Section:								      ###
#################################################################################################

# Steam Compatibility Tools Directory:
# This is the same one created during installation: https://github.com/GloriousEggroll/proton-ge-custom#installation
directory_path = "/home/tristan/.steam/compatibilitytools.d"



#################################################################################################
###	The Rest:									      ###
#################################################################################################

# URL of the GitHub releases json:
github_url = "https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases"

# Function to get the latest release object from the GitHub json:
def get_latest_release_link(url):
    response = requests.get(url)
    release_links = response.json()
    # Sanity check...just to be sure we've grabbed the right json
    if release_links[0]["author"]["login"] == "GloriousEggroll":
        return release_links[0]
    return None

# Function to extract version number from release string
def extract_version_from_link(link):
    match = re.search(r'GE-Proton(\d+-\d+)', link)
    if match:
        # print("Extracted Version:", match.group(1))
        return match.group(1)
    return None

# Function to check if there is a newer release
def is_newer_release(current_versions, latest_version):
    for version in current_versions:
        if version >= latest_version:
            return False
    return True

# Get the latest release link
latest_release_link = get_latest_release_link(github_url)

if latest_release_link:
    latest_version = extract_version_from_link(latest_release_link["tag_name"])
    #print("Latest Release Version:", latest_version)

    # Get the list of current versions in the directory
    current_versions = [extract_version_from_link(file) for file in os.listdir(directory_path)]
    # Give it a lil' tidy up
    current_versions = list(filter(lambda item: item is not None, current_versions))
    
    # Check if there is a newer release
    if is_newer_release(current_versions, latest_version):
        print("New version available: ", latest_version.replace("-", "."))
        for asset in latest_release_link["assets"]:
            if asset["browser_download_url"].endswith(".tar.gz"):
            	print("Downloading New Release:")
            	print("[", asset["browser_download_url"], "]")
            	response = requests.get(asset["browser_download_url"], stream=True)
            	if response.status_code == 200:
            	    total_size_in_bytes= int(response.headers.get('content-length', 0))
            	    block_size = 1024 #1 Kibibyte
            	    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, ncols=len(asset["browser_download_url"])+4, desc=asset["name"])
            	    with open(directory_path + "/" + asset["name"], 'wb') as f:
            	        for data in response.iter_content(block_size):
            	            progress_bar.update(len(data))
            	            f.write(data)
            	progress_bar.close()
            	print("\r\nDownload Complete! Saved to: " + directory_path + "/" + asset["name"])
            	print("Starting extraction to:" + latest_release_link["tag_name"] + "..	", end="")
            	
            	# open file 
            	archive = tarfile.open(directory_path + "/" + asset["name"])
            	# extract files 
            	archive.extractall(directory_path)
            	# close file 
            	archive.close()
            	
            	print("..success! Please restart Steam to see new version")
    else:
        print("No newer releases found.")
else:
    print("Unable to retrieve the latest release link.")

