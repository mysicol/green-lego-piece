# VeriFact

### Philly Codefest, April 2024 at Drexel University

## Overview
With misinformation rampant in this digital world, it is harder than ever to determine if what we come across is true or false. This can especially be an issue for aging adults, who typically have less experience with the internet and who may be the target of scams. VeriFact is an AI tool that easily presents news sources and their summaries related to information found on the web, rated in terms of bias, reliability, and relevance. It can be used to gain a clearer perspective on if a fact is true or false to combat digital misinformation. 

## Description

The dangers of misinformation on the internet have become more apparent in recent years, with fake news about current events exacerbating public health crises and security risks. 

VeriFact combats this issue by utilizing user input of information found on the internet to display a credibility report, including a measurement of bias, quantified reliability, and summaries of the top credible news articles.

First, the user enters a phrase describing a potential current event mentioned online, and search results are collected about the query. A database of 190 news websites along their reliabilities and political bias ratings from Ad Fontes Media was compiled and used to associate each of each output source with statistics and create summary statistics for the topic. Ninja’s Text Similarity AI tool was used to determine each article’s relevance to the search term, which is also shown next to each article in the VeriFact output. The ChatGPT API tool creates summaries for the articles from the most credible news sources to provide quick information to the user. 

VeriFact streamlines the fact-checking process to make credible information more accessible to all, which is very important to prevent the spread of confusing or dangerous misinformation. 

VeriFact's future involves converting it to a browser plug-in that would present news output based on highlighted text. It could also be adapted to analyze information presented in video format, such as TikTok or Youtube. 

![Input animation](/images/video-demo-1.gif)
![Results animation](/images/video-demo-2.gif)
![Results screenshot](/images/screenshot-demo.png)

## Setup

### Authentication keys

You must have valid authentication keys for Ninjas API, OpenAI API, and Serp API to run. Store them in a file called `back/.env` in the following format:

`OPENAI_API_KEY="[your OpenAI key]"`

`NINJAS_API_KEY="[your Ninjas key]"`

`SERP_API_KEY="[your Serp key]"`

### Running on Windows

In a terminal, run:

`cd back/`

`python -m venv venv` (only do the very first time to create venv)`

`venv/Scripts/activate`

`pip install -r requirements.txt`

`python server.py` <br><br>

In another terminal, run:

`cd front/`

`npm i`

`npm run dev`

Visit the localhost address generated to view the program.

### Running on Mac

In a terminal, run:

`cd back/`

`python3 -m venv venv` (only do the very first time to create venv)

`source venv/bin/activate`

`pip3 install -r requirements.txt`

`python3 server.py` <br><br>

In another terminal, run:

`cd front/`

`npm i` 

`npm run dev` <br>

Visit the localhost address generated to view the program.

## Authors
Francisco Cruz-Urbanc, fjc59@drexel.edu

William Dorman

Abigail Hatcher, ah3658@drexel.edu

Krisi Hristova

Charlie Meader
