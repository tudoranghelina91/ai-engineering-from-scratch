from datasets import load_dataset

ds = load_dataset("gokuls/glue_augmented_mrpc", split="train", streaming=True)

for i, d in enumerate(ds):
    print(d)
    if i == 4:
        break
