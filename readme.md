To run problem 1, run the following command:
```
python3 problem1.py
```
or run the executable file:

Then you will be asked to enter the full path of the images folder.

To run problem 2, run the following command:
```
python3 problem2.py
```
or run the executable file:

Then you will be asked to enter the full path of the txt file.

For problem 1, make sure the destination folder and csv file are empty and created, if not the program will create them for you.
Then the first folder is added to the queue, then we loop on the queue check if each folder needs to be extracted it will in the temp folder then we check the contents of the folder, any folder is added to the queue and any img file is added to the list.
The list is then looped through to copy the files and metadata is added to the csv file.

For problem 2, the txt file is read line by line and the line is split into a list of words, then parsed into a json object.