from proccess.process import process_chia_pet

def main():
    # Tutaj ustawiasz ścieżki i parametry ręcznie
    chia_file = "/home/kubog/genomics_data/4DNFIS9CCN6R.bedpe.gz"
    ctcf_file = "/home/kubog/genomics_data/ENCFF356LIU.bed.gz"
    rad21_file = "/home/kubog/genomics_data/ENCFF834GOT.bed.gz"

    start = 0
    stop = None

    out_csv = "wyniki.csv"
    out_plot = "wykres.png"

    # Wywołanie głównej funkcji przetwarzającej
    process_chia_pet(
        chia_file=chia_file,
        ctcf_file=ctcf_file,
        rad21_file=rad21_file,
        start=start,
        stop=stop,
        out_csv=out_csv,
        out_plot=out_plot
    )

if __name__ == "__main__":
    main()
