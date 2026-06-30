from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

# split ds to train and test - 0.7 train, 0.3 test
split = dataset.train_test_split(test_size=0.3, seed=15)

# split test in half, train_val = 0.15, test = 0.15
train_ds = split["train"]

validate_test_split = split["test"].train_test_split(test_size=0.5, seed=15)

validate_ds = validate_test_split["train"]
test_ds = validate_test_split["test"]

print(len(train_ds), len(validate_ds), len(test_ds))
