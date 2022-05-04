#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 22:22:23 2022

@author: 76327698468
"""

import glassdoor as gl
import pandas as pd
path = '/home/76327698468/Documentos/CienciaDados/Material Estudo Machine Learning/ds_salary_proj/scraping-glassdoor-selenium/chromedriver'

df = gl.get_jobs('data scientist', 15, False, )