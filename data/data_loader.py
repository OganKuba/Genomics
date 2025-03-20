import pandas as pd
import gzip

# Load CHiA-PET data and returns a pandas DataFrame
def load_bedpe(file_path):
    with gzip.open(file_path, 'rt') as f:
        columns = ["chrom1", "start1", "end1", "chrom2", "start2", "end2"]
        df = pd.read_csv(f, sep='\t', comment='#', header=None, usecols=range(6), names=columns)
    return df

# Load BED data and returns a pandas DataFrame
def load_bed(file_path):
    with gzip.open(file_path, 'rt') as f:
        columns = ["chrom", "start", "end"]
        df = pd.read_csv(f, sep='\t', comment='#', header=None, usecols=range(3), names=columns)
    return df

def summarize_data(df, name):
    print(f"Dataset: {name}")
    print(df.head())
    print(f"Number of records: {len(df)}")
    print("-" * 50)

