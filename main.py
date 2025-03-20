import argparse

from proccess.process import process_chia_pet


def main():
    parser = argparse.ArgumentParser(description="Filter ChIA-PET loops based on CTCF and Rad21 peaks.")
    parser.add_argument("--chia", required=True, help="Path to the ChIA-PET file (bedpe.gz).")
    parser.add_argument("--ctcf", required=True, help="Path to the CTCF peaks file (bed.gz).")
    parser.add_argument("--rad21", required=True, help="Path to the Rad21 peaks file (bed.gz).")
    parser.add_argument("--start", type=int, default=None, help="First loop index (optional).")
    parser.add_argument("--stop", type=int, default=None, help="Last loop index (optional).")
    parser.add_argument("--out_csv", default="chia_pet_annotated.csv", help="Output CSV file.")
    parser.add_argument("--out_plot", default="loop_categories_barplot.png", help="Output PNG file with bar plot.")

    args = parser.parse_args()

    process_chia_pet(
        chia_file=args.chia,
        ctcf_file=args.ctcf,
        rad21_file=args.rad21,
        start=args.start,
        stop=args.stop,
        out_csv=args.out_csv,
        out_plot=args.out_plot
    )

if __name__ == "__main__":
    main()
