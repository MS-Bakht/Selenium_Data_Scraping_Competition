# Softec Data Scraping Competition
Welcome to the data scraping repository where i have uploaded the code submitted in Softec Data Scraping Competition held by FAST, NUCES Lahore! This repository contains the code for various tasks that demonstrate data scraping skills.

# Instructions 
Participants in will be required to scrape the first 4 websites from the provided link. It is
important to note that each website has a unique structure, and thus a different scraping approach will
be expected for each site.

Website: https://www.scrapethissite.com/pages/

To ensure that participants follow the rules, they will be expected to maintain a 2-second delay
between each request during both the development and submission phases. Failure to follow this
instruction will lead to a reduction in marks.

# Tasks
The repository includes code for the following tasks:

1. For the first website, &quot;Countries of the World&quot;, participants will be required to scrape the data
and convert it into a tabular format, saving it in a CSV file. The only acceptable data format will
include the columns Country Name, Capital, Population, and Area (km2). Any data outside of
this format will not be accepted. The data should be stored in its own generated folder with the
same name of the scraped website.

2. For the second website, &quot;Hockey Teams&quot;, participants will need to scrape the data and convert
it into JSON format. They will also be required to implement pagination to scrape the entire
dataset. The JSON entities for this website will include Team, Team Name, Year, Wins, Losses,
OT Losses, Win %, Goals For (GF), Goals Against (GA), and + / -. The data should be stored in its
own generated folder with the same name of the scraped website.

3. The third website, &quot;Oscar Winning Films&quot;, will require participants to implement dynamic
loading of HTML elements to scrape the data loaded through JavaScript. The data scraped will
be stored in XML format, with the following entities: YearBlock, Year, Title, Nominations,
Awards, and Best Picture. Best Picture will be a binary variable, and YearBlock will be the main
entity, wrapping all other entities. The data should be stored in its own generated folder with
the same name of the scraped website.
