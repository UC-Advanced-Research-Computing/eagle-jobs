#!/usr/bin/env python
# coding: utf-8

# # Import necessary packages

import argparse

import pandas as pd
import datetime
import os

from hpc_runtime_prediction.model_optimization import optimize_recent_jobs


# Get split time and utput file name from arguments

parser = argparse.ArgumentParser()
parser.add_argument('--split-time', type=str, help='Split time in formate "YYYY-MM-DD"')
parser.add_argument('--output-file', type=str, help='Output file name')
args = parser.parse_args()

split_time = pd.Timestamp(args.split_time)
output_file = args.output_file

# # Import Eagle data

filepath = os.path.join('../data/', 'eagle_data.pkl')
eagle_df = pd.read_pickle(filepath)

# # Optimize Recent Jobs
n_max = 200

r2, rmse = optimize_recent_jobs(eagle_df, split_time, n_max)

optimize_recent_jobs_df = pd.DataFrame({'n': list(r2.keys()), 'r2': list(r2.values()), 'rmse': list(rmse.values())})

filename = output_file + '.pkl'
filepath = os.path.join('../results/recent_jobs/', filename)
optimize_recent_jobs_df.to_pickle(filepath)