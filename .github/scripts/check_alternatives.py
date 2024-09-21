import os
import re
import fnmatch

def find_files(directory, pattern):
    matches = []
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

directory_to_search = 'charts/datahub-executor-worker/subcharts'
pattern = '*deployment-alternatives*'

matched_files = find_files(directory_to_search, pattern)
for file in matched_files:
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if re.compile("{{\s+.Values").search(line):
                raise Exception(f"Found problem in {file}: {line}. Please use  $.Values. instead of .Values.")
                