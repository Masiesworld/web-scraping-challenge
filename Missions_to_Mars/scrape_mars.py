from flask import Flask, render_template, redirect
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
  # executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    executable_path = {'executable_path':ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
 
    # News title and paragraph
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    # Retrieve the latest news title and paragraph
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text


    return news_title, news_p

    # Image to scrap
    base_url = "https://www.jpl.nasa.gov"
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    img_page = bs(html,'html.parser')
   
    img_sec = img_page.select("footer a")
    img_path = img_section[0]['data-fancybox-href']
    featured_img_url = base_url + img_path
    return featured_img_url
    
    # Mars Facts
    facts_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(facts_url)[2]
    mars_facts.columns = ['Variables','Values']
    
    facts_html_table = mars_facts.to_html()
    return facts_html_table


    # Hemisphere
    base_url = "https://astrogeology.usgs.gov"
    hemi_url= "https://astrogeology.usgs.gov/search/resultsq=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)
    html = browser.html
    mars_hemispheres = bs(html,'html.parser')
    
    items = mars_hemispheres.select('div.item')
    hemisphere_image_urls = []

    for i in items:
        hemisphere_dict = {}
    
        title = i.find('h3').text
        hemisphere_dict['title']= title
        link = i.find('a')['href']
        page = base_url+link
    
    # Navigate the new page
        browser.visit(page)
        hemisphere_html = browser.html
        hemisphere_page = bs(hemisphere_html,'html.parser')
    
    # save img url
        img_url = hemisphere_page.find('li').a['href']
        hemisphere_dict['img_url']= img_url
        hemisphere_image_urls.append(hemisphere_dict)
        return hemisphere_image_urls

    # mars_info = {
    #     "news_title":news_title, 
    #     "news_p":news_p,
    #     "featured_img_url":featured_img_url,
    #     "facts_html_table":facts_html_table,
    #     "hemisphere_images":hemisphere_image_urls 
    # }
    

    mars_info = {}
    mars_info["news_title"] = news_title
    mars_info["news_p"] = news_p
    mars_info["featured_image_url"] = featured_image_url
    mars_info["marsfacts_html"] = facts_html_table
    mars_info["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_info
    
    
    
    
    
    
    