import pyranges as pr
import pandas as pd

def chia_pet_anchors_to_pyranges(chia_pet_df, anchor=1):
    """
        For a DataFrame with columns [chrom1, start1, end1, chrom2, start2, end2],
        extract one anchor (anchor=1 or anchor=2) and return a PyRanges object
        with columns [Chromosome, Start, End, loop_id].
    """
    anchor_data = []
    for loop_id, row in chia_pet_df.iterrows():
        if anchor == 1:
            chrom, start, end =  row["chrom1"], row["start1"], row["end1"]
        else:
            chrom, start, end = row["chrom2"], row["start2"], row["end2"]
        anchor_data.append([chrom, start, end, loop_id])

    anchor_df = pd.DataFrame(anchor_data, columns=["Chromosome", "Start", "End", "loop_id"])
    return pr.PyRanges(anchor_df)

def bed_df_to_pyranges(bed_df):
    """
        For a DataFrame with columns [chrom, start, end],
        return a PyRanges object with [Chromosome, Start, End].
        """
    pr_df = bed_df.rename(columns={
        "chrom": "Chromosome",
        "start": "Start",
        "end": "End"
    })
    return pr.PyRanges(pr_df)


def find_loops_with_peak(chia_pet_pyr, peak_pyr):
    """
        Intersect the ChIA-PET anchors PyRanges with the peak PyRanges.
        Return a set of loop_ids that have overlap with the peaks.
    """
    overlap_result = chia_pet_pyr.join(peak_pyr)
    loop_ids = set(overlap_result.df["loop_id"])
    return loop_ids