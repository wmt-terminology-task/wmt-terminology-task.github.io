---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

# Welcome to the WMT 2023 Terminology Shared Task

<p class="message">
The accurate translation of technical terms and specialized vocabulary is a crucial aspect of determining the quality of machine translation output. The WMT 2023 Terminology Shared Task aims to assess the extent to which machine translation models can utilize additional information regarding the translation of terminologies.


Participants in this task will be provided with source text and possibly an associated segment-level terminology dictionary.
<!-- two dictionaries: (1) a `segment-level terminology dictionary` and (2) a  `segment-level randomly sampled translation dictionary`. -->
Evaluation of submissions will be based on both the general translation quality and the effectiveness of terminology translation.



We welcome submissions of both machine translation systems that incorporate terminology at inference time and those trained in a weakly supervised manner utilizing terminology information.
Have questions or suggestions? <a href="mailto:wmt-terminology@googlegroups.com">Contact Us</a>!
</p>

## Motivation

Consider the following English sentence and the hypothesis which is being updated based on incremental terminology information, which ultimately leads to the translation that is the closest to the reference.

|-|-|
| Source		| The report is in accordance with ROA. |
| Hypothesis 1	| Der Bericht steht im Einklang mit ROA. |
| Help 1 		| “ROA” → “FOG” |
| Hypothesis 2	| Der Bericht steht im Einklang mit FOG. |
| Help 2 		| “is in accordance” → “entspricht” |
| Hypothesis 3 (best)	| Der Bericht entspricht ROA. |

## Important links

- [Data](#data)
- [How to submit](#how-to-submit)

## Terminology Task Important Dates

|  | Date |
| ----------- | :-----------: |
| **Training data and test data ready to download** | **16th March, 2023** |
| **Submission deadline for the terminology task** |  **23th June, 2023** |
| **Paper submission deadline to WMT** | **TBA September, 2023** |
| WMT Notification of acceptance | TBA October, 2023 |
| WMT Camera-ready deadline | 16th October, 2023 |
| Conference | 	TBA December, 2023 |

All deadlines are in AoE (Anywhere on Earth). Dates are specified with respect to EMNLP 2023.

## Goals

The primary goal of the WMT 2023 Terminology Shared Task is to evaluate the ability of machine translation systems to accurately translate technical terms and specialized vocabulary. The task aims to assess the extent to which machine translation models can utilize additional information regarding the translation of terminologies.

Another important goal of the shared task is to encourage the development of machine translation systems that are better equipped to handle the complex vocabulary of technical and **specialized domains**. By providing participants with these resources and evaluating their performance on both general translation quality and the effectiveness of terminology translation, the task hopes to encourage the development of systems that can **accurately** and **consistently** translate these types of texts.


Overall, the WMT 2023 Terminology Shared Task seeks to improve the state-of-the-art in machine translation by challenging participants to develop systems that can accurately and effectively translate technical terms and specialized vocabulary, with the ultimate goal of improving communication and understanding in  specialized and emerging domains.


## Task Description

We focus on the following language pairs (one direction for each):
   - `zh-en`: Chinese → English
   - `cs-en`: English → Czech
   - `de-en`: German → English
  
<!-- and we provide two modes for each language pair:
- `annotated`: primary mode. In this mode, you will be provided with the source sentences along with a segment-level terminology dictionary annotated by human.
- `random`: secondary mode. In this mode, you will be provided with the source sentences along with a segment-level randomly-sampled dictionary. -->

<!-- Note that:
1. For each language pair, only one direction (the original direction) is considered.
2. The `random` is mainly useful for analysis. -->


### Evaluation Criteria 
Your submissions will be evaluated based on:

1. Translation Quality: The quality of the overall machine translation output will be evaluated both by standard human and automatic metrics.
   <!-- - For automatic evaluation, [`sacreBLEU`](https://github.com/mjpost/sacreBLEU), [`COMET`](https://github.com/Unbabel/COMET) and [`BlonDe`](https://github.com/EleanorJiang/BlonDe) will be adopted. -->
   For human evaluation, we will focus on **fluency**, **adequacy**, **grammaticality** and **coherence**. Fluency refers to the naturalness and readability of the translated text, while adequacy refers to the accuracy of the translated content, including the correct translation of words, phrases, and idioms. Grammaticality refers to the correctness of the grammar and sentence structure of the translated text. Coherence refers to the overall consistency and clarity of the translated text with respect to the document-level and corpus-level context. This will be evaluated based on the extent to which the translated text conveys the intended meaning of the source text in a way that is understandable and coherent with respect to the overall document context.
2. Terminology Translation:
   - **Success rate**: The success rate of terminology translation assesses the ability of the machine translation system to accurately translate technical terms and specialized vocabulary. This will be measured by comparing the machine's translation of technical terms to their corresponding translations in the provided dictionaries. The goal is to have a high success rate, indicating that the machine is able to accurately translate technical terms and specialized vocabulary.
 <!-- The success rate of terminology translation will be calculated as the number of correctly translated terms divided by the total number of terms.  -->
   - **Term consistency**: The consistency of terminology translations refers to the uniformity of the translations of technical terms across the entire corpus. In other words, the goal is to ensure that the same technical term is translated consistently throughout the text, rather than being translated differently in different parts of the text. This will be evaluated by comparing the machine's translation of technical terms to the translations in the provided dictionaries, and measuring the number of instances where the same term is translated differently. The goal is to have a high consistency rate, indicating that the machine is able to translate technical terms consistently.
3. Terminology Usage:
   The data is provided in three different modes. The first one corresponds to general MT and the second one has the terminology dictionary added. The last one (indistinguishable in the test data) has random, though correct, translations of words, which are not terminologies. If we observe improvement between the different modes, it means that the model is not just good on its own but can make good use of the terminology. This is included so that we can measure to what extent can the models leverage the terminology as opposed to just being good overall.
<!-- 3. Inference Speed: The amount of time it takes for the machine translation system to generate a translation output. The focus will be on the time efficiency of the machine translation system. The speed of the system will be evaluated by measuring the time it takes for the system to generate translations for a given input corpus ([test set]((https://drive.google.com/drive/folders/11YqeDAgJVOflw4npcaEZ0itKMh5nUwJ1?usp=share_link))). The goal is to have a fast translation speed while maintaining high translation quality and terminology translation success and consistency rates. This is particularly important for real-time translation applications, where speed is critical for ensuring effective communication. Additionally, a fast translation speed can also improve the productivity of translators who rely on machine translation systems to assist with their work. -->

The final ranking of the submissions will be ascertained through a weighted average of the scores obtained from both the **human** evaluation and terminology translation assessments.
<!-- , which will be conducted based on the machine's performance on the test sets in the `annotated`-mode. Kindly keep this in mind when submitting your system. -->


## Paper Describing Your System
You are invited to submit a short paper (4 to 6 pages) to WMT describing your system. Shared task submission description papers are non-archival, and you are not required to submit a paper if you do not want to. If you don't, we ask that you give an appropriate reference describing your metric that we can cite in the overview paper.

## Data

You download [the development data](https://drive.google.com/drive/folders/1dwaX0HANYAPGtfNYQqsRbc45Mab_CdV-?usp=share_link) and [the test data](https://drive.google.com/drive/folders/11YqeDAgJVOflw4npcaEZ0itKMh5nUwJ1?usp=share_link).
<!-- A development set is also included within this resource. -->
Please read the `README.md` in this folder for more information.

**❗IMPORTANT❗** The use of any additional terminology-specific data beyond that provided in these resources is strictly prohibited.

## Example segment

Considering the example in [motivation](#motivation), the following source could appear in `test.en-de.en`:

`The report is in accordance with ROA.`

Then, the corresponding line in `test.en-de.dict` can be empty or contain a JSON array, such as:

`[{"en": "ROA", "de": "FOG"}, {"en": "is in accordance", "de": "entspricht"}]`

It is then up to the model to utilize any part of this additional information.
Note that the spans in the dictionary do not have to appear as consecutive words in the text (e.g. `He turned around` → `Er drehte sich um.` and `turned` → `drehte um`).
Furthermore, it is possible that the alignment is not perfect (semi-automatic procedure), however it is guaranteed that the individual words appear in the text.

## How to submit: 

Before you submit, please make sure your submission follows the [submission format](#submission-format).
You can run your translation files through a validation script, which is now available [here](https://drive.google.com/file/d/12_uzUVUJAppN5PQLo1Uh8TK9UcwV0AfW/view?usp=sharing).

Your translations should be submitted through [this form](https://forms.gle/ziS7v3r9kxW5xJSx6).
- If your team already participated in [the WMT general task](http://www2.statmt.org/wmt23/translation-task.html), please use the same team name.
- Translations should be in the form that text is normally published, e.g. recased and detokenised.
- Each team is permitted to submit a maximum of 7 systems. If you are submitting multiple systems, we kindly request that you submit each system individually. In addition, we need you to indicate the primary system.
- Submissions should be uploaded by deadline stated above.
- If you have any questions regarding to the submission, please send an email to [wmt-terminology@googlegroups.com](mailto:wmt-terminology@googlegroups.com).

## Submission Format

An example submission is available [here](link).

## Sponsors

<style>
	.column {
	  float: left;
	  padding: 20px;
	}
	
</style>
<div style="position: relative; width: 700px; height: 100px; min-height: 200px">    
    <div style="position: relative; bottom: 0px;">
	   <div class="column">
	     <img src="/public/css/ETH-logo.png" height=50px width=auto>
	   </div>
	   <div class="column">
	     <img src="/public/css/microsoft.png" height=50px width=auto>
	   </div>
	</div>
