

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



		Project title: Natural language processing models reveal neural dynamics of human conversation



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

----------------------------------------------------------------------------------------------------------------



Project description: Utilize artificial natural language processing model to study neural activity during 
natural conversation recorded by intracranial EEG.


----------------------------------------------------------------------------------------------------------------
Data Access and Replacement Instructions

Due to the large size of the processed data, they have been uploaded to the DABI database with the following identifiers:

	Accession Code: M6RES1N4MVA3
	
	DOI: https://doi.org/10.18120/5jg5-j555
	
Follow these steps:

	1. Download the Data:

		Navigate to the DOI link above or search for the accession code M6RES1N4MVA3 in the DABI database.

		Download the folder: processed_data/envelope from the repository.

	2. Replace Existing Files:

		Locate the data/envelope folder in your local directory.

		Replace its contents with the downloaded processed_data/envelope files.



----------------------------------------------------------------------------------------------------------------

Organization of materials: data files, custom-written codes, and the results used for the

analysis are provided in separate folders:




Data:		

1. neuronal data used in the analysis is provided in “data”. 

		
		The data folder includes 1 subfolder:

		•	envelope: contains band-specific neuronal activity envelopes processed from raw signal.



		A ‘datafolder_README.txt’ file provides summary information about each file, corresponding scripts, 

		figures, and panels. The data files are in ".npy" format. 

        The data for each participant is stored, with participant IDs ranging from pt01 to pt14.

        Each participant's data is saved in their respective numbered folder.

        The detailed description of each file and the variables

		contained within the files are provided within the 'datafolder_README.txt'.

2. The embeddings used in the analysis are provided in the "NLP".

        The "NLP" folder includes ".npy" files ranging from pt01_gpt2_cycle.npy to pt14_gpt2_cycle.npy.

        Each file contains GPT-2_small embeddings generated for each word in the conversation.


        A ‘NLP_README.txt’ file provides summary information about each file.

             - NLP/NLP_README.txt

3. The transcription data used in the analysis is provided in "transcription" folder.

        The "transcription" folder includeds ".csv" files ranging from pt01.csv to pt14.csv 

         corresponding to each participant.

        1. index: The order of each word's occurrence in conversation

        2. start_time: The word onset time in seconds

        3. end_time: The time at which the pronunciation of a words ends in seconds during the conversation

        4. sid: Boolean where 0 indicates the participant is speaking, 

         while 1 indicates the participant is listening.

4. The parcellations data used in the analysis and figure is provided in "parcellations" folder.

        The "parcellations" folder includes a ".csv" file containing detailed information about 

         the electrodes used in the study.

        A ".npy" file containing the position of each electrode.


        A ‘parcellations_README.txt’ file provides summary information about each file.

                - parcellations/parcellations_README.txt


Codes: 		A ‘scripts_README.txt’ file provides summary information about the custom-written codes used for the 

        analysis. Codes used in the analysis is provided as:


            functions:	custom-written PYTHON functions used within the scripts for the analysis which are

                            stored in get_electrode_correlation.py and selectivity_during_transitions_sign.py

            scripts:	custom-written PYTHON scripts for the analysis, along with the functions they rely on,
                
                            are stored together in the same file.



        figure. Codes used to generate figures are stored in files ranging from figure1.ipynb to figure4.ipynb, 

                and to produce the required visualization plots.


        A ‘scripts_README.txt’ file provides summary information about each file.

                - analysis/scripts_README.txt

		

figures:		Figures generated from the scripts figure1.ipynb to figure4.ipynb will be stored in their corresponding

        sub-folders (i.e. figure1, figure2,..., figure4 within the figure folder)




Results:	Results of analysis generated from the script will be directly stored in the corresponding

		sub-folders (i.e. pt01, pt02,..., pt14 within analysis/result folder).

----------------------------------------------------------------------------------------------------------------		

PYTHON (v 3.11.3) was used for the main analyses.

----------------------------------------------------------------------------------------------------------------

