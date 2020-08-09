# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:49:44 2020

@author: foxbee
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/foxbee/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 5)

df.to_csv('glassdoor_jobs.csv', index = False)
