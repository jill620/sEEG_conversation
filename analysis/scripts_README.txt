functions:	custom-written PYTHON functions for the analysisscripts:	custom-written PYTHON scripts for the analysisEach .py file includes the necessary functions and scripts it requires,with detailed comments provided for each function.Simply set the appropriate paths, and the entire code in the file can be executed directly.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                               "Summary of the codes for the analysis"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


Data Access and Replacement Instructions

Due to the large size of the output, they have been uploaded to the DABI database with the following identifiers:

	Accession Code: M6RES1N4MVA3
	
	DOI: https://doi.org/10.18120/5jg5-j555
	
Follow these steps:

	1. Download the Data:

		Navigate to the DOI link above or search for the accession code M6RES1N4MVA3 in the DABI database.

		Download the folder: analysis/result from the repository.

	2. Replace Existing Files:

		Locate the analysis/result folder in your local directory.

		Replace its contents with the downloaded analysis/result files.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% get_correlation.py % This script analyzes the correlation between neuronal signals (sEEG data) and GPT-2 embeddings during natural conversation.% Neuronal signals were aligned to word onset times, preprocessed to remove autocorrelation and outliers,% and segmented by speaker role. Correlations were computed across time windows, frequency bands,% and GPT-2 layers/units using linear regression. Results were saved as .npy files for each participant and electrode. ----------------------------------------------------------------------------------------------------------------%% selectivity_during_transitions.py: Sentences% This script analyzes the selectivity of neuronal signals during speaker transitions in conversation.% It processes the data to identify time points when participants transition between speaking and listening.% For each transition type, neuronal signals (sEEG envelope data) are aligned to word onset times% and preprocessed to handle outliers.% The script calculates selectivity indices and performs statistical tests (t-tests) for five frequency bands.% Results, including selectivity indices and p-values, are saved as .npy files.----------------------------------------------------------------------------------------------------------------****************************************************************************************************************