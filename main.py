# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# Required libraries
# pip install mne-bids coloredlogs tqdm pandas scikit-learn json_tricks fire

# set up environment
#import mne-study-template
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


fname = config['ctf']
l_freq = config['l_freq'] # in seconds
h_freq = config['h_freq']


# CTF
raw = mne.io.read_raw_ctf(fname)

raw.filter(
    l_freq, h_freq, 
    picks=None, 
    filter_length='auto', 
    l_trans_bandwidth='auto', 
    h_trans_bandwidth='auto', 
    n_jobs=1, 
    method='fir', 
    iir_params=None, 
    phase='zero', 
    fir_window='hamming', 
    fir_design='firwin', 
    skip_by_annotation=('edge', 'bad_acq_skip'), 
    pad='reflect_limited', 
    verbose=None)


# save the first seconds of MEG data in FIF file 
raw.save(os.path.join('out_dir','meg.fif'))

