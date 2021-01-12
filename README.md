# Scholar.ly Tool:

## Demo
 
 ![Scholarly](https://drive.google.com/uc?export=view&id=1VF196eZFm3BTFPvF0pA1MBWDPUya_Sre)
 
## Contents
* [Overview] (https://github.com/debapratim1234/Scholarly-Tool#Overview)
* Motivation
* Technologies Used

## Overview
 
 The interface ‘Scholar.ly’ is designed to automate the downloading of research articles from ‘PubMed’ repository. Any search query like corona virus, dengue, malaria etc., is the  input for the interface. The interface traces the search related articles from PubMed database and allows the user to monitor the backend downloading progress in a separate window.The downloaded data were collected in the folder name same as search query created in the path ‘C:\Research_Articles’. The interface downloads the entire pdf if it is freely available otherwise, only the abstracts are downloaded and stored in a text file. The Web-crawling and Web-scrapping concept was adapted for downloading pdfs/txt files. An excel file is generated in the same folder to maintain PubMed ID, title of the article, downloaded type (entire pdf or abstract) for the user’s future reference.
 
## Motivation
 
 Many sites like Library Genesis, SciHub, PubMed, Google Scholar are available for downloading of related research articles, which affords a link of search related papers and the user has to manually download or open the articles of interest. This way of collecting the research papers is time consuming and not efficient as there are many risks to neglect the papers. As of now, there is no interface for automatic downloading of the articles as ‘.pdf’ format and accumulating in a single location for further studies. This initiates us to develop an interface ‘Scholar.ly’ to facilitate the researchers to shorten the time taken to search the papers.

## Technologies Used

 * Biopython
 * Beautiful Soup
 * tkinter
