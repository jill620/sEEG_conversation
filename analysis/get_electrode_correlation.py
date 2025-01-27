import numpy as np
import pandas as pd
from scipy import stats
from joblib import Parallel, delayed
import os

def detect_outliers_iqr(data, thres=1.5):
    '''
    Detects outliers in a dataset using the Interquartile Range (IQR) method.

    Outliers are defined as values that are 1.5 times the IQR above the third quartile (Q3)
    or below the first quartile (Q1).

    Args:
        - data (numpy.ndarray): The input data array.
        - thres (float, Defaults to 1.5): The multiplier of IQR that determines outliers.

    Returns:
        - upper_bound (float): The calculated upper bound for outliers.
        - lower_bound (float): The calculated lower bound for outliers.

    Note:
        - Helper function of deauto_confineOutlier(data)
    '''
    data = sorted(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    IQR = q3-q1
    upr_bound = q3+(thres*IQR) 
    lwr_bound = q1-(thres*IQR)
    return upr_bound, lwr_bound
    
def align_to_word(df, data):
    '''
    Align data(sEEG signal) to word onset time by a window of 8 seconds.

    The function takes a DF containing word data where:
        - sid:
            * 0: speak
            * 1: listen
        - start_time:
            * word onset time in secs
    And a series of sEEG signal, using a window of 8 seconds to capture
    the eeg signal 4 secs before the word onset time and 4 secs after the word.

    Args:
        - df (pd.DataFrame): A DataFrame containing the following columns:
            * start_time (float): The word onset time in seconds.
            * end_time (float): The word end time in seconds.
            * sid (int): Speaker label (0 for "self" as the participant speaks, 1 for "other" as the participant listens).
        - data (np.ndarray): A 2D array of shape (m, 1) containing the time-series signal data.

    Returns:
        - self_words (np.ndarray): Signal segments for words spoken by the participant.
        - other_words (np.ndarray): Signal segments for words heard by the participant.

    Note:
        - df: df.start_time is the word onset time in second. data is m x 1 arrays of sEEG signal
    '''
    self_words = np.zeros([df[(df.sid==0)].shape[0], 8000])
    for iind, onsettime in enumerate(df[df.sid==0].start_time.values):
        onsettime = int(onsettime*1000)
        if onsettime > data.shape[0] - 4000:
            self_words[iind,:] = data[-4000:].mean()
            continue
        if onsettime < 4000:
            self_words[iind,:] = data[:4000].mean()
            continue
        
        self_words[iind,:] = data[(onsettime-4000):(onsettime+4000),0]

    other_words = np.zeros([df[(df.sid!=0)].shape[0], 8000])
    for iind, onsettime in enumerate(df[df.sid!=0].start_time.values):
        onsettime = int(onsettime*1000)
        if onsettime > data.shape[0] - 4000:
            other_words[iind,:] = data[-4000:].mean()
            continue
        if onsettime < 4000:
            other_words[iind,:] = data[:4000].mean()
            continue
        other_words[iind,:] = data[(onsettime-4000):(onsettime+4000),0]

    return self_words, other_words

def deauto_confineOutlier(data):
    '''
    Remove autocorrelation from the input data and handles outliers

    First removes AR(1) autocorrelation in the input array
    by subtracting the product of the auto correlation coef (rho) and the previous data point.
    After de-autocorrelation, then remove outliers.

    Args:
        - data (array)

    Returns:
        - np.array: array with de-autocorrelation and no outliers

    Note:
        - data type is array; perform de-autocorrelation first, then treat outliers
    '''
    rho = np.corrcoef(data[1:], data[:-1])[1,0]
    data_de = data[1:] - rho * data[:-1]
    ub, lb = detect_outliers_iqr(data_de)
    data_de[data_de > ub] = ub
    data_de[data_de < lb] = lb
    return data_de

def get_correlation(obs1, filepath, savepath):
    '''
    Computes the correlation between sEEG signal data(aligned) and GPT-2 embeddings.

    The function aligns time sEEG signal data and GPT-2 embedding data based on word onset time,
    capture and compute correlation coefficient by specific time windows.

    Args:
        - obs1 (object): An object contains data for current participant and electrode.
            * obs1.pid (str): The participant id
            * obs1.electrode (str): The electrode
        - filepath (str): Path to the root of the project
        - savepath (str): Path to the output directory where the results will be saved

    Returns:
        - None
            * Results will be saved in .npy format

    Note:
        - Checked if there is a existing folder for current participant
            * if not, create a folder by participant id
        - Checked if there is a existing file for current participant's electrode
        - NaN values are replaced by mean
        - Linear regression is performed for each combination of:
            * Five frequency bands.
            * 768 GPT-2 units.
            * 13 GPT-2 layers.
    '''

    save_dir = os.path.join(savepath, obs1.pid)
    os.makedirs(save_dir, exist_ok=True)

    output_file = os.path.join(save_dir, obs1.electrode + '_electrode_correlation.npy')
    if os.path.exists(output_file):
        print(f"File already exists: {output_file}")
        return

    ampl = np.load(filepath + 'data/envelope/' + obs1.pid + '/' + obs1.electrode + '_envelope.npy')

    df0 = pd.read_csv(filepath + 'transcription/' + obs1.pid + '.csv')

    gpt2 = np.load(filepath + 'NLP/' + obs1.pid + '_gpt2_cycle.npy')
    gpt2[0,:,:] = np.nan 				                                                                                
    nanind = np.isnan(gpt2.sum(1).sum(1))==1

    for qq in np.arange(nanind.shape[0])[nanind]: 	                                                                    # nan value replaced by mean
        gpt2[qq,:,:] = np.nanmean(gpt2,axis=0)

    amps = np.zeros([df0[df0.sid == 0].shape[0],1,5])                                                                   # speak
    ampo = np.zeros([df0[df0.sid != 0].shape[0],1,5])                                                                   # listen


    for i in range(5):
        temp1, temp2 = align_to_word(df0, ampl[:,i].reshape([-1,1]))
        amps[:,0,i] = temp1[:,3500:4000].mean(axis=1)                                                                   # speak
        ampo[:, 0, i] = temp2[:, 4000:4500].mean(axis=1)                                                                # listen
    
    sigs = np.zeros([1,5,768,13,5]) 			                                                                        # 1 x bands x nodes x layers x (linregress)
    sigs[:] = np.nan
    gpt_temp = gpt2[df0.sid==0,:,:]


    for j in range(5):
        amp_treated = deauto_confineOutlier(amps[:, 0, j])
        for k in range(768):
            for m in range(13):
                gpt_treated = deauto_confineOutlier(gpt_temp[:,k,m])
                sigs[0,j,k,m,:] = stats.linregress(amp_treated, gpt_treated)


    sigo = np.zeros([1,5,768,13,5]) 			                                                                        # 1 x bands x nodes x layers x (linregress)
    sigo[:] = np.nan
    gpt_temp = gpt2[df0.sid!=0,:,:]


    for j in range(5):
        amp_treated = deauto_confineOutlier(ampo[:, 0, j])
        for k in range(768):
            for m in range(13):
                gpt_treated = deauto_confineOutlier(gpt_temp[:,k,m])
                sigo[0,j,k,m,:] = stats.linregress(amp_treated, gpt_treated)

    with open(savepath + obs1.pid + '/' + obs1.electrode + '_electrode_correlation.npy','wb') as f:
        np.save(f, sigs)
        np.save(f, sigo)
        

savepath = 'result/'                                                                                                    # Output file will be saved to analysis/result
filepath = '../'                                                                                                        # root path


combined = pd.read_csv(filepath+'parcellations/parcellation_cleaned.csv')                                               # Load in detailed electrode data of participants
Parallel(n_jobs=8)(delayed(get_correlation)(combined.iloc[ii], filepath, savepath) for ii in range(combined.shape[0]))  # Parallel computation of correlations for each participant and electrode




