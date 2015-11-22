import os
#web app module 
from flask import Flask, url_for, render_template, request
#module for processing html and xml 
from lxml import html 
import requests
import bs4 
from bs4 import BeautifulSoup

#base url for dining halls 
menuUrl = "http://menu.ha.ucla.edu/foodpro/default.asp"

#requests webpage 
page = requests.get(menuUrl)
#utilizes requests/tree to scrape
soup = bs4.BeautifulSoup(page.text)
links = soup.select('div.menucontent a[class="itemlinkt"]')

menuItemsXPath = ('//div[@id="globalwrapper"]/div[@class="divider_menu"]' + 
                    '/div[@class="menucontent"]' + 
                    #'/table[@class="menugridtable' + str(mealCont) + '"]' + 
                    '/table[@class="menugridtable"]' + 
                    '/tr/td[@class="menugridcell"]' + 
                    '/ul' + 
                    '/li[@class="level5"]' +
                    '/a[@class="itemlinkt"]' + 
                    '/text()')

def getMenuItems():
  return [a.get_text() for a in links]

def mealXPath (): 
  tree = html.fromstring(page.text)  
  return tree.xpath(menuItemsXPath)


menuCont = { 1: "", 2: "_last" } 

#firstHalf = tree.xpath(mealXPath(''))
secondHalf = mealXPath()

if __name__ == "__main__":
  #print str(firstHalf)
  #print str(secondHalf)
  #print str(tree)
  print getMenuItems()
