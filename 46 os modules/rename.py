import os

for i in range(1, 100):
    os.rename(f'data/Day{i}', f'data/Folder {i}')