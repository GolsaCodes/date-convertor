# Persian Date Normalizer using ParsT5

## Overview

Persian dates can appear in different formats, including:
- Numeric dates: `1402/07/15`
- Dates with Persian month names: `15 مهر 1402`
- Dates with written numbers: `پانزده مهر 1402`
- Informal expressions: `روز پانزده مهر سال 1402`
- Dot-separated dates: `1402.7.15`

This project fine-tunes a pretrained ParsT5 model to transform these different representations into a consistent format:

`YYYY/MM/DD`


## Repository Structure
```text
├── Final.ipynb                
├── data-generation.py         # Script for generating synthetic informal Persian date samples
└── persian_dates_dataset.csv  # Dataset containing informal phrases and formal target dates
```

## Model

- **Base Model:** [Ahmad/parsT5-base](https://huggingface.co/Ahmad/parsT5-base)
- **Architecture:** T5 (Text-to-Text Transfer Transformer)
- **Task:** Sequence-to-Sequence Text Generation
- **Framework:** Hugging Face Transformers
- **Dataset Size:** 10,000 samples

The model receives a prefixed input:

`normalize date: پانزده مهر 1402`

And generates:

`1402/07/15`

## Dataset

The dataset contains 10,000 samples and is divided into:

- Training set: 85% (8,500 samples)
- Test set: 15% (1,500 samples)

The dataset includes numeric and textual day representations, Persian month names, optional words such as `روز`, `ماه`, and `سال`, and dot-separated date formats.

## Training

The model is fine-tuned using the Hugging Face `Trainer` API.

The training process includes:

- Loading the pretrained ParsT5 model and tokenizer.
- Preparing input and target text.
- Splitting the dataset into training and test sets.
- Tokenizing the input and target sequences.
- Fine-tuning the model for 10 epochs.
- Evaluating the model after each epoch.
 
## Example

**Input:**
```text
normalize date: بیست و یک مهر سال 1402
```

**Expected Output:**
```text
1402/07/21
```
## Technologies

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- Pandas
- Scikit-learn
- Matplotlib
