def annotate_and_save_results(chia_pet_df, ctcf_anchor1, ctcf_anchor2, rad21_anchor1, rad21_anchor2, out_file):

    ctcf_1anchor_set = ctcf_anchor1.union(ctcf_anchor2)
    ctcf_2anchors_set = ctcf_anchor1.intersection(ctcf_anchor2)

    rad21_1anchor_set = rad21_anchor1.union(rad21_anchor2)
    rad21_2anchors_set = rad21_anchor1.intersection(rad21_anchor2)

    chia_pet_df['CTCF_1anchor'] = chia_pet_df.index.map(lambda i: i in ctcf_1anchor_set)
    chia_pet_df['CTCF_2anchors'] = chia_pet_df.index.map(lambda i: i in ctcf_2anchors_set)
    chia_pet_df['Rad21_1anchor'] = chia_pet_df.index.map(lambda i: i in rad21_1anchor_set)
    chia_pet_df['Rad21_2anchors'] = chia_pet_df.index.map(lambda i: i in rad21_2anchors_set)

    chia_pet_df.to_csv(out_file, index=False)
    print(f"[INFO] Wyniki z adnotacjami zapisane do: {out_file}")