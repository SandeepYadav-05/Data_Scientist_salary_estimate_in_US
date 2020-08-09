# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:49:44 2020

@author: foxbee
"""

import glassdoor_scraper as gs
path = "C:/Users/foxbee/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 5)

df.to_csv('Salary_Data.csv', index = False)
