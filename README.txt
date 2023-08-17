Note: This code was developed on Windows 11, using an environment set up through anaconda. Many courseworks throughout the entirety of this year have been done on this system and the linux systems in the bragg building interchangeably. There have been no problems with this form of development on either system. The only problem I could foresee occuring is with the file structure, since windows uses back slashes and unix systems use forwards slash. All code has been implemented to account for this by using the os python library to conform to the correct convention.

Also this README was written so that it looks best organized in full screen.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If any code breaking or runtime problems are encountered please do not hesitate to email me:

School email: fy18aol@leeds.ac.uk

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Description of the included files and folders:

1. (Folder) ./LSTM_Project/DatasetsTest - Contains the processed datasets in CSV format. Only reason to look in here is to see what a processed dataset looks like, or to see the result of running scripts: mat2csv.py, mat2csv-2017.py, or DetectNeuronVariance. Models look in this folder for specified training data

2. (Folder) ./LSTM_Project/MAT_Files - Contains the raw, unedited .mat files. These are downloaded straight from https://osf.io/a64uz/ .

3. (Folder) ./LSTM_Project/Predictions - All predictions are saved here when they are made, for both the MLP and the LSTM model

4. (Folder) ./LSTM_Project/Saved_Models - Contains the saved trained models. The name indicates what animal it was trained to test.

5. (Folder) ./LSTM_Project/Scripts - Contains all of the scripts developed

	- (File) ./LSTM_Project/Scripts/DetectNeuronVariance.py - Calculates the standard deviation of a given file, for each neuron in the file

	- (File) ./LSTM_Project/Scripts/mat2csv.py - Converts .mat files into CSV format with the required fields. !!IMPORTANT!! This particular file ONLY converts: ./LSTM_Project/MAT_Files/AVA_HisCl and ./LSTM_Project/MAT_Files/WT_Stim1

	- (File) ./LSTM_Project/Scripts/mat2csv-2017.py - Converts .mat files into CSV format with the required fields. !!IMPORTANT!! This particular file ONLY converts: ./LSTM_Project/MAT_Files/n2_prelet and ./LSTM_Project/MAT_Files/n2_let

	- (File) ./LSTM_Project/Scripts/testcsv2df.ipynb - Was used as a means of testing dataset length after processing to ensure it was executed correctly

6. (Folder) ./LSTM_Project/TestData - Contains all of the outputs of DetectNeuronVariance. For instance, if WT_Stim1 dataset is processed by the script, two new files called WT_Stim1_LargestRemoved and WT_Stim1_SmallestRemoved will be added to the folder

7. (File) ./LSTM_Project/MLPModel - Jupyter Notebook containing the entirety of the MLP model

8. (File) ./LSTM_Project/LSTM_Model - Jupyter Notebook containing the entirety of the LSTM model

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RUNNING THE PROGRAM

Cells have been numbered to make explanation easier

(MLP) If running the entire program (training included):

1. Every cell will be run, starting with both sets of imports

2. Run cells 1-3

3. In cell 4, select which dataset will be tested, this will withhold it from the training data. Select dataset by uncommenting one of the variables called "testFileName". The reason there are only 2 options available is because there are only 2 available pre trained models in Saved_Models folder, and it is for these two options. You can test whatever you want, the code is pretty straight forward to manipulate

4. Run cells 5 and 6

5. Run cell 7, which is the training loop. This might take a while depending on if the system you are on has a GPU. I assume if you are running the training loop you want to save the model as well. The line that saves the models is commented out currently in case it is run on accident so as to not overwite any previously saved models. If you do intend to save models, please uncomment this line.

6. **DO NOT** run cell 8

7. Run cells 9-12






(MLP) If running the entire program (using one of the saved models to cast new predictions (No training)):

1. Before you start, you need to already know which dataset will be used to test before running anything

2. Run cells 1, 2, and 4. 4 being the most important, it is necessary to set the testFileName variable

3. Run cell 6

4. Run cell 8, this will point the model to the correct pre trained model in the Saved_Models folder

5. Run cells 10, 11, and 12

7. Run cells 9-12

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Cells have been numbered to make explanation easier

(LSTM) If running the entire program (training included):

1. Every cell will be run, starting with both sets of imports

2. Run cells 1 and 2

3. In cell 3, select which dataset will be tested, this will withhold it from the training data. Select dataset by replacing the string in testFileName (located at the bottom of the cell) to any file name found in DatasetsTest. It is important to ONLY input the name of a file found in these folders and to MAKE SURE you replace the call to the main data_selection() function with the appropriate dataset. In the code, it has been marked with an 'Action Needed' comment.

4. Run cells 4 and 5

5. Run cell 6, which is the training loop. This might take a while depending on if the system you are on has a GPU. I assume if you are running the training loop you want to save the model as well. The line that saves the models is commented out currently in case it is run on accident so as to not overwite any previously saved models. If you do intend to save models, please uncomment this line.

6. Run cells 7-11







(LSTM) If running half the program (using one of the saved models to cast new predictions (No training)):

1. Before you start, you need to already know which dataset will be used to test before running anything

2. Run cells 1, 2, and 3. 3 being the most important, it is necessary to set the testFileName variable

3. Run cells 8-11

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Imports:

Most are pretty standard imports for python and can be easily installed with pip install.



