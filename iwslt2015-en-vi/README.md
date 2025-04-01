---
dataset_info:
  features:
  - name: en
    dtype: string
  - name: vi
    dtype: string
  splits:
  - name: train
    num_bytes: 32478162
    num_examples: 133317
  - name: validation
    num_bytes: 323727
    num_examples: 1268
  - name: test
    num_bytes: 323727
    num_examples: 1268
  download_size: 18133980
  dataset_size: 33125616
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---
