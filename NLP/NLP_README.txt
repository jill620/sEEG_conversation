

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



		"Summary of the data files used for the analysis"



The data files are in ".npy" format and are stored in the NLP folder.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


Data Access and Replacement Instructions

Due to the large size of the NLP embeddings, they have been uploaded to the DABI database with the following identifiers:

	Accession Code: M6RES1N4MVA3
	
	DOI: https://doi.org/10.18120/5jg5-j555
	
Follow these steps:

	1. Download the Data:

		Navigate to the DOI link above or search for the accession code M6RES1N4MVA3 in the DABI database.

		Download the folder: /NLP/ from the repository.

	2. Replace Existing Files:

		Locate the /NLP/ folder in your local directory.

		Replace its contents with the downloaded /NLP/ files.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Below the detailed description of each file.



The NLP folder includes .npy files ranging from pt01_gpt2_cycle.npy to pt14_gpt2_cycle.npy:



*dataset*

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

File name:		pt##_gpt2_cycle.npy



Description: This file contains gpt2 embeddings for each word in conversation of participant id ##.



•	gpt2 embeddings: A 3D numpy array with:

		- shape: (N, 768, 13)

		    - N: Total number of words in the conversation

		    - 768: Hidden embedding size of GPT-2 for each layer

		    - 13: Total number of GPT-2 layers

		- values: These embeddings capture semantic and contextual information about the input conversation.



----------------------------------------------------------------------------------------------------------------

