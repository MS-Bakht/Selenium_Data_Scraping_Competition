#!/usr/bin/env python
# coding: utf-8

# # Data-Scraping Competition
# 
# Participants in Round 1 will be required to scrape the first 4 websites from the provided link. It is
# important to note that each website has a unique structure, and thus a different scraping approach will
# be expected for each site.
# 
# Website: https://www.scrapethissite.com/pages/
# 
# To ensure that participants follow the rules, they will be expected to maintain a 2-second delay
# between each request during both the development and submission phases. Failure to follow this
# instruction will lead to a reduction in marks.

# In[8]:


import time
import random
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import os
import urllib
# import defaultdict


# In[13]:


import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import random
#import string
#from more_itertools import random_permutation
#from datetime import datetime
import json


# In[32]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# set up the driver
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# navigate to the category page
url = 'https://www.scrapethissite.com/pages/'
driver.get(url)
pages = driver.find_elements(By.CLASS_NAME,'page-title')
print(pages)


# In[16]:


links = []
for i in pages:
    print(i.text)
    n = i.find_element(By.TAG_NAME,'a')
    print(n.get_attribute('href'))
    links.append(n.get_attribute('href'))

links=links[:-1]


# ### TASK 1      
# For the first website, &quot;Countries of the World&quot;, participants will be required to scrape the data
# and convert it into a tabular format, saving it in a CSV file. The only acceptable data format will
# include the columns Country Name, Capital, Population, and Area (km2). Any data outside of
# this format will not be accepted. The data should be stored in its own generated folder with the
# same name of the scraped website.

# In[17]:


driver.get(links[0])


# In[18]:


names = driver.find_elements(By.CLASS_NAME,'country-name')
names = [i.text for i in names]
capitals = driver.find_elements(By.CLASS_NAME,'country-capital')
capitals = [i.text for i in capitals]
population = driver.find_elements(By.CLASS_NAME,'country-population')
population = [i.text for i in population]
area = driver.find_elements(By.CLASS_NAME,'country-area')
area = [i.text for i in area]


# In[19]:


df = pd.DataFrame(np.array([names, capitals, population, area]).T,columns=['Country Name','Capital','Population','Area (km2)'])


# In[20]:


display(df)


# In[40]:


#os.mkdir('Countries Of The World')
df.to_csv('Countries Of The Worlddata.csv')


# # Task 2
# For the second website, &quot;Hockey Teams&quot;, participants will need to scrape the data and convert
# it into JSON format. They will also be required to implement pagination to scrape the entire
# dataset. The JSON entities for this website will include Team, Team Name, Year, Wins, Losses,
# OT Losses, Win %, Goals For (GF), Goals Against (GA), and + / -. The data should be stored in its
# own generated folder with the same name of the scraped website.

# In[23]:


def task2():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    url = 'https://www.scrapethissite.com/pages/'
    driver.get(url)
    link = driver.find_element(by=By.XPATH, value='//*[@id="pages"]/section/div/div/div/div[2]/h3/a')
    time.sleep(2)
    link.click() 
    time.sleep(2)
    page_exist = True

    team_names, years , team_wins , team_loss , ot_losses , win_percentage , gf ,ga,pnmf = [],[],[],[],[],[],[],[],[]
    while(page_exist):
        names = driver.find_elements(By.CLASS_NAME, "name")
        team_names.extend([i.text for i in names])
        time.sleep(2)
        
        year = driver.find_elements(By.CLASS_NAME, "year")
        years.extend([i.text for i in year])
        time.sleep(2)

        wins = driver.find_elements(By.CLASS_NAME, "wins")
        team_wins.extend([i.text for i in wins])
        time.sleep(2)

        loss = driver.find_elements(By.CLASS_NAME, "losses")
        team_loss.extend([i.text for i in loss])
        time.sleep(2)

        ot_l = driver.find_elements(By.CLASS_NAME, "ot-losses")
        ot_losses.extend([i.text for i in ot_l])
        time.sleep(2)

        win_p = driver.find_elements(By.CLASS_NAME, "pct")
        win_percentage.extend([i.text for i in win_p])
        time.sleep(2)

        gff = driver.find_elements(By.CLASS_NAME, "gf")
        gf.extend([i.text for i in gff])
        time.sleep(2)


        gaa = driver.find_elements(By.CLASS_NAME, "ga")
        ga.extend([i.text for i in gaa])
        time.sleep(2)

        pnm = driver.find_elements(By.CLASS_NAME, "diff")
        pnmf.extend([i.text for i in pnm])
        time.sleep(2)

        try:    
            link = driver.find_element_by_css_selector("[aria-label=Next]")
            time.sleep(2)
            link.click() 
        except:
            print("End of pages")
            page_exist= False
        
    time.sleep(2)
    driver.close()
    
    data = []
    for i in range (0, len(team_names)):
        info = {}
        info["team_name"]= team_names[i]
        info["year"]= years[i]
        info["wins"]= team_wins[i]
        info["losses"]= team_loss[i]
        info["ot_losses"]= ot_losses[i]
        info["win_percent"]= win_percentage[i]
        info["gf"]= gf[i]
        info["ga"]= ga[i]
        info["+/-"]= pnmf[i]
        data.append(info)
    
    
    task2_answer=[]
    for i in range (0, len(data)):
        final={}
        teamno= "team"+f"{(i+1)}"
        final[teamno]=data[i]
        task2_answer.append(final)
        
    with open("hockey_teams.json", "w") as outfile:
        json.dump(task2_answer, outfile)


# In[24]:


task2()


# In[25]:


df


# In[29]:


#JSON file is saved in the file directory with the name of hockey_teams.json


# # TASK 3
# The third website, &quot;Oscar Winning Films&quot;, will require participants to implement dynamic
# loading of HTML elements to scrape the data loaded through JavaScript. The data scraped will
# be stored in XML format, with the following entities: YearBlock, Year, Title, Nominations,
# Awards, and Best Picture. Best Picture will be a binary variable, and YearBlock will be the main
# entity, wrapping all other entities. The data should be stored in its own generated folder with
# the same name of the scraped website.

# In[50]:


options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(links[2])


# In[51]:


year=[]
titles=[]
nominations=[]
awards=[]
best_pic=[]

pages = driver.find_elements(By.CLASS_NAME,'year-link')
for p, page in enumerate(pages):
    print(p)
    
    time.sleep(2)
    page.click()
    time.sleep(4)
    title = driver.find_elements(By.CLASS_NAME,'film-title')
    title = [i.text for i in title]
    nomination = driver.find_elements(By.CLASS_NAME,'film-nominations')
    nomination = [i.text for i in nomination]
    award = driver.find_elements(By.CLASS_NAME,'film-awards')
    award = [i.text for i in award]
    best_picture = driver.find_elements(By.CLASS_NAME,'film-best-picture')
    for x,n in enumerate(best_picture):
        try:
            n.find_element(By.TAG_NAME,'i')
            best_picture[x]=True
        except:
            best_picture[x]=False
    titles.extend(title)
    
    nominations.extend(nomination)
    awards.extend(award)
    best_pic.extend(best_picture)
    year.extend([page.text for i in range(len(title))])
    pages = driver.find_elements(By.CLASS_NAME,'year-link')
driver.quit()


# In[52]:


print(np.array(year).shape)
print(np.array(titles).shape)
print(np.array(nominations).shape)
print(np.array(awards).shape)
print(np.array(best_pic).shape)


# In[53]:


data = pd.DataFrame(np.array([year, titles, nominations, awards, best_pic]).T,columns=['Year','Title','Nomination','Award','BestPicture'])


# In[54]:


data


# In[55]:


# os.mkdir('Oscar Winning Films')
data.to_csv('Oscar Winning Filmsdata.csv')

