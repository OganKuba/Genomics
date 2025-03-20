import matplotlib.pyplot as plt

def plot_loop_categories(ctcf_1anchor, ctcf_2anchors, rad21_1anchor, rad21_2anchors, out_plot):
    labels = [
        "CTCF ≥1 anchor",
        "CTCF 2 anchors",
        "Rad21 ≥1 anchor",
        "Rad21 2 anchors"
    ]
    sizes = [
        len(ctcf_1anchor),
        len(ctcf_2anchors),
        len(rad21_1anchor),
        len(rad21_2anchors)
    ]

    plt.bar(labels, sizes)
    plt.title("Loop count in different categories")
    plt.ylabel("Number of loops")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out_plot)
    plt.show()
    print(f"[INFO] Bar plot saved to: {out_plot}")
