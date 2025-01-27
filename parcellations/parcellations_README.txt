

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



		"Summary of the data files used for the analysis"



The data files are in ".npy" and ".csv" format and are stored in the parcellations folder.

Below the detailed description of each file and the variables contained within the files are provided.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



The data folder includes 2 files:

•	parcellation_cleaned.csv: Containing detailed information about the electrodes used in the study.

•	pos.npy: Electrode location in RAS.




*dataset*

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

File name:		parcellation_cleaned.csv



Description: This file contains 5 variables:



•	index: Sorted index of each electrode

•	electrode: electrode name

•	pid: participant's id ranging from pt01 to pt14

•	area: The brain area where the electrode is placed.
          This indicates the anatomical area being monitored for neuronal activity.

•	hemi: The hemisphere of the brain where the electrode is placed,

        - rh: right hemisphere

        - lh: left hemisphere




----------------------------------------------------------------------------------------------------------------

File name:		pos.npy


Description: The RAS location of each electrode. The order of the positions are the same as those listed in parcellation_cleaned.csv
	-dimension: (n_electrode, n_RAS_dim), where:
		n_electrode is the total number of channels.
		n_RAS_dim = 3 is the RAS coordinates.




----------------------------------------------------------------------------------------------------------------



