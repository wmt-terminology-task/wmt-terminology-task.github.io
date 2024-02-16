# Submissions for WMT2023 Terminology Shared Task

## 1. Folder Structure
There are two folders:
1. [`submissions`](submissions.zip) folder contains all files in the exact form as they were submitted by the contestants;
2. [`split_submissions`](split_submissions.zip) folder contains the files from the first folder that are split and re-grouped for the simplicity of evaluation (see 2.2).

the name is organized the following way: 
in `submissions` folder: 
\{system\_name\}.\{dataset\}.\{lang\_pair\} (e.g. `DCU-TU-TR.blind.en-cs`)
in `split_submissions` folder:
\{mode\}.\{system\_name\}.\{dataset\}.\{lang-pair\}.tsv (e.g. `rand.DCU-TU-TR.blind.en-cs`)

Where:
* `system_name` is name of submitted system;
* `dataset` is in {`blind`, `test`} set and stands for the datasets used for evaluation. In the paper, we used the `blind` dataset unless noted otherwise;
* `lang-pair` is in {`en-cs`, `de-en`, `zh-en`} set and stands for the language pairs (ordered in translation direction). 
* `mode` is in {`base`, `term`, `rand`} set and stands for the testing modes of the system. `base` stands for no dictionary used, `term` stands for the terminology dictionary-aided translastion, and `rand` stands for random quasi-terminology dictionary.


## 2. File Format

### 2.1. Initial Submissions 
For the submitted files in `submissions` folder, each file is organized as following triplets of lines with input and output translations, according to the translation mode: 

```
source sentence ||| translation using no_terms_1
source sentence ||| translation using random_terms_1
source sentence ||| translation using terms_1
```

### 2.2. Pre-processed Submissions
For simplicity of evaluation, we split each submission into three files (according to translation mode) and provided it with the according terminology. Thus, in the `split_submissions` folder, the resulting `.tsv` files are organized as follows:
```
src              \t  ref               \t  terms      \t  mt
source sentence  \t reference sentence \t terminology \t MT system output
```
For `base` mode, we filled the `terms` column with the correct terminology (i.e., from `term` mode) for the sake of consistency. 

## 3. Sumbisssion Description

### 3.1. General Overview

Here, we specify the relation between the sumbitted systems, their references in the paper and the necessary notes. 

| System name  | Submitted by |  In Paper? |  Notes |
| --- | --- | --- | --- |
|	lc_wmt23_single	|	Lingua Custodia	|	x	|	in paper, referred to as Lingua Custodia	|
|	HW-TSC	|	Huawei	|	x	|	in paper, referred to as Huawei.	|
|	opuscat-terms	|	University of Helsinki	|	x	|	in blind datasets, the sentences were provided in a order: term->rand->base. In `split_submissions` folder, they are ordered in the correct way.	|
|	DCU-TU-TR	|	AdaptTerm (Yasmin Moslem; Gianfranco Romani; Mahdi Molaei)	|	x	|	in paper, referred to as AdaptTerm	|
|	TSSNMT	|	NCSOFT	|		|	most of the sentences from submission were not found in the source files from the datasets. We filtered them out and got only a small subset, around 57 sentences for blind dataset. This heavily influences the metrics of terminology consistency and success rate, thus the results should not be compared to other systems directly.	|
|	TSSNMT_filtered	|	NCSOFT	|	x	|	same problem as with as TSSNMT. In the paper, referred to as VARCO-MT_TSSNMT	|
|	BJTU-LB_system1	|	Beijing Jiaotong University	|		|		|
|	ForceGen_Transformer	|	NCSOFT	|		|		|
|	ForceGen_Transformer_filtered	|	NCSOFT	|	x	|	in paper, referred to as VARCO-MT_ForceGen	|
|	BJTU-LB_system2	|	Beijing Jiaotong University;	|	x	|	in paper, referred to as BJTU-LB	|
|	uedin_twoshot	|	University of Edinburgh	|	x	|		|
|	uedin_decode_tag	|	University of Edinburgh	|		|		|
|	uedin_decode_tag_improved	|	University of Edinburgh	|	x	|	in paper, referred to as UEDIN_tag	|
|	uedin_llm	|	University of Edinburgh	|		|		|
|	uedin_llm_improved	|	University of Edinburgh	|	x	|	in paper, referred to as UEDIN_LLM	|


### 3.2. Languages Covered
Not all systems covered all languages (and not both datasets). In the table below, we show which system covered which data (a cross means the data are covered). Below, the columns are called the following way: 
 - the `b:` prefix means the `blind` dataset
 - the `t:` prefix means the `test` dataset

|	system name	|	b:en-cs	|	b:de-en	|	b:zh-en	|	t:en-cs	|	t:de-en	|	t:zh-en	|	resume:	|
| --- | --- | --- | --- | --- | --- | --- | --- |
|	lc_wmt23_single	|	x	|	x	|	x	|	x	|	x	|	x	|		|
|	HW-TSC	|		|		|		|	x	|	x	|	x	|	only test set	|
|	opuscat-terms	|	x	|	x	|	x	|	x	|	x	|	x	|		|
|	DCU-TU-TR	|	x	|	x	|	x	|	x	|	x	|	x	|		|
|	TSSNMT	|		|		|	x	|		|		|	x	|	only Chinese	|
|	TSSNMT_filtered	|		|		|	x	|		|		|	x	|	only Chinese	|
|	BJTU-LB_system1	|		|		|	x	|		|		|	x	|	only Chinese	|
|	ForceGen_Transformer	|		|		|	x	|		|		|	x	|	only Chinese	|
|	ForceGen_Transformer_filtered	|		|		|	x	|		|		|	x	|	only Chinese	|
|	BJTU-LB_system2	|		|		|	x	|		|		|	x	|	only Chinese	|
|	uedin_twoshot	|	x	|	x	|	x	|	x	|	x	|		|	without test.zh-en	|
|	uedin_decode_tag	|	x	|	x	|	x	|	x	|	x	|		|	without test.zh-en	|
|	uedin_decode_tag_improved	|	x	|	x	|	x	|	x	|	x	|		|	without test.zh-en	|
|	uedin_llm	|	x	|	x	|	x	|	x	|	x	|		|	without test.zh-en	|
|	uedin_llm_improved	|	x	|	x	|	x	|	x	|	x	|		|	without test.zh-en	|

## 4. For further questions

If you have any uncertainty about the submissions their preprocessing, please contact Kirill Semenov by email kir ~dot~ semenow ~at~ yandex ~dot~ ru
