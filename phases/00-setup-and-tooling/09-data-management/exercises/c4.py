import os
import time

from datasets import load_dataset
from dotenv import load_dotenv
from numpy import average

load_dotenv()

print(os.getenv("HF_TOKEN"))

ds = load_dataset(
    "allenai/c4",
    "en",
    split="train",
    streaming=True,
    token=os.getenv("HF_TOKEN"),
)

requests_per_10_sec = []
max_per_10_sec = 0
last_index = 0

start_time = time.perf_counter()
k = 0

for i, d in enumerate(ds):
    k += 1
    end_time = time.perf_counter()
    if int(end_time - start_time) == 10:
        start_time = time.perf_counter()
        max_per_10_sec = max(max_per_10_sec, k)
        requests_per_10_sec.append(k)
        print(f"Current max per 10 secs: {k}")
        k = 0

avg_per_10_sec = average(requests_per_10_sec)
print(max_per_10_sec)
print(avg_per_10_sec)
