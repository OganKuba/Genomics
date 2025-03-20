import pandas as pd
from pybedtools import BedTool

# For DataFrame with columns [chrom1, start1, end1, chrom2, start2, end2] it takes out
# the anchor coordinates and returns a BedTool object with columns [chrom, start, end, loop_id]
def chia_pet_anchors_to_bedtool(chia_pet_df, anchor=1):
    anchor_data = []

    for loop_id, row in chia_pet_df.iterrows():
        if anchor == 1:
            chrom, start, end = row["chrom1"], row["start1"], row["end1"]
        else:
            chrom, start, end = row["chrom2"], row["start2"], row["end2"]

        anchor_data.append((chrom, start, end, loop_id))
    return BedTool(anchor_data)

# For DataFrame with columns [chrom, start, end] it returns a BedTool object
def bed_df_to_bedtool(bed_df):
    bed_data = []
    for _, row in bed_df.iterrows():
        bed_data.append((row["chrom"], row["start"], row["end"]))
    return BedTool(bed_data)


def find_loops_with_peak(chia_pet_bedtool, peak_bedtool):
    overlap_result = chia_pet_bedtool.intersect(peak_bedtool, wa=True, wb=False, u=True)
    loop_ids = set()
    for feature in overlap_result:
        loop_ids.add(int(feature[3]))
    return loop_ids