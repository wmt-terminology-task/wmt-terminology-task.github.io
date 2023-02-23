####
# validation script for WMT23 Terminology Shared Task submission.
#
#
# this script assumes you are submitting for all translation directions and warns you for missing entries.
# 2. this script assumes you have the same metric name throughout the whole submission. (and you should)
# 3. this script checks if the score values are valid float.
#
# Usage: if your metric uses a reference translation:
# python validate.py BLEU.sys.score < your_metric.sys.score
# python validate.py BLEU.seg.score < your_metric.seg.score
#
# Usage: if your metric does not a reference translation (QE metric)
# python validate.py COMET-QE.sys.score < your_metric.sys.score
# python validate.py COMET-QE.seg.score < your_metric.seg.score
####
import sys
import math
from collections import defaultdict

gold=sys.argv[1]

data=defaultdict(dict)
with open(gold, mode="r", encoding="UTF-8") as GOL:
    for line in GOL:
        f = line.strip().split("\t")
        lp = f[1]
        k = " ".join(f[2:-1])
        data[lp][k] = f[0]
lps_present = set()
clear=True
mymetric=""
for line in sys.stdin:
    f = line.strip().split("\t")
    lp = f[1]
    lps_present.add(lp)
    k = " ".join(f[2:-1])
    if k not in data[lp].keys():
        print(k in data[lp].keys(), "ERROR: {", lp, k, "} is not a valid key for the test data.")
        clear=False
    try:
        if math.isnan(float(f[-1])): 
            raise ValueError
    except ValueError:
        print ("ERROR: for {",lp, k, "},", f[-1], "is not a valid score.")
        clear=False
    mymetric=f[0]
    data[lp][k]=f[0]

missing_lps = set()
for lp, lpdata in data.items():
    if lp not in lps_present:
        missing_lps.add(lp)
        continue
    for k in lpdata.keys():
        if lpdata[k] != mymetric:
            print ("WARNING: entry {", k, "} is missing.")
            clear=False
if missing_lps:
    print("WARNING: the following language pairs are missing:", missing_lps)

if clear:
    print ("All entries formated correctly. The file is ready for submission.")
