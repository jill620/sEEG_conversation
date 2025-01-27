

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



		"Summary of the data files used for the analysis"



The data files are in ".npy" format, stored in the "envelope" sub-folder.


Below is the detailed description of each file.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


The data folder includes 2 subfolders:

•	dataset: contains pre-processed neuronal activities for different task conditions.

•	envelope: envelope: contains band-specific neuronal activity envelopes processed from raw signal.




*dataset*

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Folder name:		envelope



Description: This folder contains sub-folders ranging from pt01 to pt14,

             each sub-folder containing neuronal activity envelopes of each participant.



•	pt##: sub-folder that contains envelopes data of this participant:

    - .npy files:

		- dimension: (n_samples, n_bands), where:

		        n_samples: The number of time points in the raw sEEG signal for the given electrode.

		        n_bands: The number of predefined frequency bands. [8,13], [13,30], [30,55], [70,110], [130,170]




----------------------------------------------------------------------------------------------------------------



