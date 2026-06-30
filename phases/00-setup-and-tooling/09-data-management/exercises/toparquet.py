from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

csv_size = dataset.to_csv("imdb_train.csv")
pqt_size = dataset.to_parquet("imdb_train.parquet")

print(csv_size, pqt_size)
