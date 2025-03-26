from convert.converter import (
    chia_pet_anchors_to_pyranges,
    bed_df_to_pyranges,
    find_loops_with_peak
)
from data.data_loader import load_bedpe, load_bed
from save_data.save_data import annotate_and_save_results
from visualize.plot_loop import plot_loop_categories


def process_chia_pet(chia_file, ctcf_file, rad21_file, start=None, stop=None,
                     out_csv="chia_pet_annotated.csv", out_plot="loop_categories_barplot.png"):

    #Load the data
    chia_pet_df = load_bedpe(chia_file)
    ctcf_df = load_bed(ctcf_file)
    rad21_df = load_bed(rad21_file)

    #Subset according to the parameters
    if start is not None or stop is not None:
        chia_pet_df = chia_pet_df[start:stop]

    #Index Reset
    chia_pet_df.reset_index(drop=True, inplace=True)

    #Convert the data to PyRanges objects
    anchor1_pyr = chia_pet_anchors_to_pyranges(chia_pet_df, anchor=1)
    anchor2_pyr = chia_pet_anchors_to_pyranges(chia_pet_df, anchor=2)

    #Convert the data to PyRanges objects
    ctcf_pyr = bed_df_to_pyranges(ctcf_df)
    rad21_pyr = bed_df_to_pyranges(rad21_df)

    ctcf_anchor1 = find_loops_with_peak(anchor1_pyr, ctcf_pyr)
    ctcf_anchor2 = find_loops_with_peak(anchor2_pyr, ctcf_pyr)
    rad21_anchor1 = find_loops_with_peak(anchor1_pyr, rad21_pyr)
    rad21_anchor2 = find_loops_with_peak(anchor2_pyr, rad21_pyr)

    all_loops = set(chia_pet_df.index)

    ctcf_1anchor = ctcf_anchor1.union(ctcf_anchor2)
    ctcf_2anchors = ctcf_anchor1.intersection(ctcf_anchor2)

    rad21_1anchor = rad21_anchor1.union(rad21_anchor2)
    rad21_2anchors = rad21_anchor1.intersection(rad21_anchor2)

    overlap_ctcf1_rad21_1 = ctcf_1anchor.intersection(rad21_1anchor)
    overlap_ctcf2_rad21_2 = ctcf_2anchors.intersection(rad21_2anchors)

    print(f"[INFO] Total number of analyzed loops          : {len(all_loops)}")
    print(f"[INFO] Loops with >=1 CTCF anchor              : {len(ctcf_1anchor)}")
    print(f"[INFO] Loops with 2 CTCF anchors               : {len(ctcf_2anchors)}")
    print(f"[INFO] Loops with >=1 Rad21 anchor             : {len(rad21_1anchor)}")
    print(f"[INFO] Loops with 2 Rad21 anchors              : {len(rad21_2anchors)}")
    print("--------------------------------------------------")
    print(f"[INFO] Overlapping loops: >=1 CTCF & Rad21 anchor : {len(overlap_ctcf1_rad21_1)}")
    print(f"[INFO] Overlapping loops: 2 CTCF & 2 Rad21 anchors : {len(overlap_ctcf2_rad21_2)}")

    annotate_and_save_results(chia_pet_df, ctcf_anchor1, ctcf_anchor2, rad21_anchor1, rad21_anchor2, out_csv)
    plot_loop_categories(ctcf_1anchor, ctcf_2anchors, rad21_1anchor, rad21_2anchors, out_plot)