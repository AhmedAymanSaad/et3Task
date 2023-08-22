FOLDER_PATH = "../problem1/dairies"
IMG_EXT = ['jpg','png', 'jpeg', 'gif', 'bmp']
ZIP_EXT = ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz']
DST_PATH = "./problem1ImgsFolder"
CSV_PATH = "./problem1.csv"

import os
import zipfile
import shutil
import time

# input the folder path
FOLDER_PATH = input("Please input the folder path: ")

folder_queue = [FOLDER_PATH]
img_list = []

# Check if destination folder exists
if not os.path.exists(DST_PATH):
    os.mkdir(DST_PATH)
else:
    # Remove all files and directories in destination folder
    for root, dirs, files in os.walk(DST_PATH, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
# create a temp folder to store extracted files
os.mkdir(DST_PATH + "/temp")

# Check if CSV file exists
if os.path.exists(CSV_PATH):
    os.remove(CSV_PATH)
else:
    # Create CSV file
    with open(CSV_PATH, 'w') as f:
        f.write("Image, Image Size, Image Modification Data\n")

# Check the folder queue
while len(folder_queue) > 0:
    folder_current = folder_queue.pop(0)
    # extract folder if it is a zip file
    if folder_current.split('.')[-1] in ZIP_EXT:
        with zipfile.ZipFile(folder_current, 'r') as zip_ref:
            zip_ref.extractall(DST_PATH + "/temp")
        folder_current = DST_PATH + "/temp"
    for root, dirs, files in os.walk(folder_current):
        for name in files:
            ext = name.split('.')[-1]
            if ext in IMG_EXT:
                img_list.append(os.path.join(root, name))
            elif ext in ZIP_EXT:
                folder_queue.append(os.path.join(root, name))
        for name in dirs:
            folder_queue.append(os.path.join(root, name))

# Copy all images to destination folder
for img in img_list:
    shutil.copy(img, DST_PATH)
    # change the file name to remove the prefix before -
    new_name = img.split('-')[-1]
    try:
        os.rename(os.path.join(DST_PATH, img.split('\\')[-1]), os.path.join(DST_PATH, new_name))
    except FileExistsError:
        # check last count for duplicated name
        counter = 1
        new_name = new_name.split('.')[0] + "(" + str(counter) + ")." + new_name.split('.')[1]
        while os.path.exists(os.path.join(DST_PATH, new_name)):
            new_name = new_name.split('(')[0] + "(" + str(counter) + ")." + new_name.split('.')[1]
            counter += 1
        os.rename(os.path.join(DST_PATH, img.split('\\')[-1]), os.path.join(DST_PATH, new_name))
    # get the image name, size and last modified time
    img_name = new_name.split('.')[0]           # remove the extension
    img_size = os.path.getsize(os.path.join(DST_PATH, new_name))
    img_last_modified = os.path.getmtime(img)   # get the last modified time of original image
    # format the last modified time
    img_last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(img_last_modified))
    # write the image name, size and last modified time to a csv file
    with open(CSV_PATH, 'a') as f:
        f.write("{}, {}, {}\n".format(img_name, img_size, img_last_modified))

# delete the temp folder
shutil.rmtree(DST_PATH + "/temp")