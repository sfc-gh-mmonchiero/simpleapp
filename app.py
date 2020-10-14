import streamlit as st
import sys

st.title("Test App 11")

from multiprocessing import Pool


work_items = [
    (1, 'A', True),
    (2, 'X', False),
    (3, 'Y', True),
    (4, 'Z', False),
]
# Define a callable to do the work. It should take one work item.
def worker(arg):
    counter = 1
    while True:
      counter += 1

cpus = 3

# Create a ThreadPool (or a process Pool) of desired size.
# What size? Experiment. Slowly increase until it stops helping.
pool = Pool(cpus)

# Do work and collect results.
# Or use pool.imap() or pool.imap_unordered().
work_results = pool.map(worker, work_items[0:cpus])

# Wrap up.
pool.close()
pool.join()
