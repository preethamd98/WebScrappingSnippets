#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:33:16 2017

@author: preetham
"""

import unicodedata
import urllib2 as u
from bs4 import BeautifulSoup
Search="NewYork"
def search(Search):
      wikiFile = u.urlopen("https://en.wikipedia.org/wiki/"+Search)
      wikiHtml = wikiFile.read()
      wikiFile.close()
      soup = BeautifulSoup(wikiHtml,'html.parser')
#wikiAll = soup.find_all("a")
      A=soup.p.get_text()
      B=unicodedata.normalize('NFKD', A).encode('ascii','ignore')
      return B
