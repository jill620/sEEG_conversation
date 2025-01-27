import numpy as np
import pandas as pd
from scipy import stats

def align_to_word(time_start, data):
    '''
    Align data(sEEG signal) to word onset time by a window of 8 seconds.

    The function takes a time_start word onset time and a series of eeg signal,
    using a window of 8 seconds to capture the eeg signal 4 secs before the word onset time and 4 secs after the word.

    Args:
        time_start (float): word onset time in seconds
        data (np.ndarray): A 2D array of shape (m, 1) containing the time-series signal data.

    Returns:
        - self_words (np.ndarray): Signal segments for words spoken by sid == 0.

    Note:
        - data is m x 1 arrays of sEEG signal
    '''
    self_words = np.zeros([len(time_start), 8000])
    for iind, onsettime in enumerate( time_start ):
        onsettime = int(onsettime*1000)
        if onsettime > data.shape[0] - 4000:
            self_words[iind,:] = data[-4000:].mean()
            continue
        if onsettime < 4000:
            self_words[iind,:] = data[:4000].mean()
            continue
        self_words[iind,:] = data[(onsettime-4000):(onsettime+4000),0] 
    return self_words
    
def detect_outliers_iqr(data):
    '''
    Detects outliers in a dataset using the Interquartile Range (IQR) method.

    Args:
        - data (numpy.ndarray): The input data array.
        
    Returns:
        - upper_bound (float): The calculated upper bound for outliers.
        - lower_bound (float): The calculated lower bound for outliers.
    '''
    data = sorted(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    IQR = q3-q1
    upr_bound = q3+(1.5*IQR)
    lwr_bound = q1-(1.5*IQR)
    return upr_bound, lwr_bound

def get_transition_time(df):
    '''
    Extract speaker transition times from DataFrame

    This function identifies the time points in a conversation where the speaker changes
    between sid == 0 and sid != 0.

    Args:
        - df (DataFrame): The conversation data that contains:
            * start_time (float): Word onset time
            * sid (int): Speaker identifier

    Returns:
        - to_speak (np.ndarry): an array of times when "other" transitions to "self" or listening transitions to speaking.
        - to_listen (np.ndarry): an array of times when "self" transitions to "other" or speaking transition to listening.
    '''
    pre_sid = df.iloc[0].sid > 0
    to_speak = []
    to_listen = []
    for i in range(df.shape[0]):
        obs = df.iloc[i]
        if (obs.sid > 0) != pre_sid:
            if obs.sid == 0:
                to_speak.append(obs.start_time)
            else:
                to_listen.append(obs.start_time)
            pre_sid = obs.sid > 0
    return np.array(to_speak), np.array(to_listen)


combined = pd.read_csv('../parcellations/parcellation_cleaned.csv')                                                     # Load in detailed electrode data of participants

savepath = 'result/'                                                                                                    # Output file will be saved to analysis/result
filepath = '../'                                                                                                        # working path of this project


prepid = 'temp'                                                                                                         # temporary for tracking current participant
output_r = np.zeros([combined.shape[0], 2,5])                                                                           # initialize result matrix for selectivity sign
output_r[:] = np.nan                                                                                                    # fill result matrix with NA values
output_p = np.zeros([combined.shape[0], 2,5])                                                                           # initialize result matrix for p-values
output_p[:] = np.nan                                                                                                    # fill result matrix with NA values

for ii in range(combined.shape[0]):                                                                                     # Iterate through every electrode in combined

    obs1 = combined.iloc[ii]                                                                                            # Retrieve the current row containing electrode information

    ampl = np.load(filepath + 'data/envelope/' + obs1.pid+'/'+obs1.electrode+'_envelope.npy')

    if combined.iloc[ii].pid != prepid:                                                                                 # If the participant ID is different from the previous iteration, load transcription
        df0 = pd.read_csv(filepath + 'transcription/'+combined.iloc[ii].pid+'.csv')

    prepid = combined.iloc[ii].pid                                                                                      # Update the current participant id
    self_start, other_start = get_transition_time(df0)

    ss = [] 										                                                                    # Transition to speaking
    for tt in self_start:                                                                                               # Check if other stopped speaking before and self started speaking after the transition
        if df0[(df0.end_time > tt - 1) & (df0.end_time <= tt)].sid.min() > 0:         	                                # before tt, listen
            if df0[(df0.start_time >= tt) & (df0.start_time < tt + 1)].sid.max() == 0:                                  # after tt, speak
                ss.append(tt)

    os = [] 										                                                                    # Transition to listening
    for tt in other_start:
        if df0[(df0.end_time > tt - 1) & (df0.end_time <= tt)].sid.max() == 0:        	                                # before tt, participant speak
            if df0[(df0.start_time >= tt) & (df0.start_time < tt + 1)].sid.min() > 0:                                   # after tt, listen
                os.append(tt)

    # Neural activity during both transitions will be compared to established language comprehension periods
    osd = []                                                                                                            # Get time stamps during listening as a control variable
    for tt in os:
        ind = df0[df0.start_time == tt].index.values[0]                                                                 # index of the starting time
        while ind < len(df0)-1 and df0.loc[ind+1].sid != 0:                                                             # the end time of other speaking
            ind += 1
        tt_end = df0.loc[ind].end_time
        tt += 0.5
        while tt < tt_end:
            osd.append(tt)
            tt += 0.5

    for i in range(5):                                                                                                  # iteration, 5 frequency bands
        ampl_ss = align_to_word(ss, ampl[:,i].reshape([-1,1]))[:,3500:4000].mean(axis=1)                                # Get neural activity during transitions to speaking
        ub, lb = detect_outliers_iqr(ampl_ss)
        ampl_ss[ampl_ss > ub] = ub
        ampl_ss[ampl_ss < lb] = lb

        ampl_os = align_to_word(os, ampl[:,i].reshape([-1,1]))[:,4000:4500].mean(axis=1)                                # Get neural activity during transitions to listening
        ub, lb = detect_outliers_iqr(ampl_os)
        ampl_os[ampl_os > ub] = ub
        ampl_os[ampl_os < lb] = lb

        ampl_osd = align_to_word(osd, ampl[:,i].reshape([-1,1]))[:,4000:4500].mean(axis=1)                              # Extract and process osd signals
        ub, lb = detect_outliers_iqr(ampl_osd)
        ampl_osd[ampl_osd > ub] = ub
        ampl_osd[ampl_osd < lb] = lb

        output_r[ii,0,i] = (ampl_ss.mean() - ampl_osd.mean())/(ampl_ss.mean() + ampl_osd.mean())                        # Compute selectivity index for self speaking and other speaking
        output_r[ii,1,i] = (ampl_os.mean() - ampl_osd.mean())/(ampl_os.mean() + ampl_osd.mean())

        output_p[ii,0,i] = stats.ttest_ind(ampl_ss, ampl_osd)[1]                                                        # T-tests to examine whether neural activity during transition is significantly different from language comprehension period.
        output_p[ii,1,i] = stats.ttest_ind(ampl_os, ampl_osd)[1]

    if ii % 50 == 49:                                                                                                   # Save results every 50 iterations
        np.save(savepath + 'selectivity_during_transitions_sign.npy', output_r)
        np.save(savepath + 'selectivity_during_transitions_p.npy', output_p)

    if ii %100 == 0:                                                                                                    # Print iteration time every 100 iterations
        print(ii)


np.save(savepath + 'selectivity_during_transitions_sign.npy', output_r)                                                 # Save selectvity results
np.save(savepath + 'selectivity_during_transitions_p.npy', output_p)                                                    # Save p-value results
