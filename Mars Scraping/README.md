# Mission to Mars

I've built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Step 1 - Scraping
My initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### Scraped Data:

NASA Mars News:

The code scrapes the NASA Mars News Site and collects the latest News Title and Paragragh Text.
```# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast." ```

JPL Mars Space Images - Featured Image

Using splinter, the app navigates to the JPL feature space image site and finds the image url for the current Featured Mars Image.
```# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'```

Mars Weather

The app also visits the Mars Weather twitter account and scrapes the latest Mars weather tweet from the page. 
```# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'```

Mars Facts

A Pandas DataFrame is used to store the scraped data from the Mars Facts site (planet including Diameter, Mass, etc). Pandas then converts the data to a HTML table string.
```# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]```

Mars Hemisperes

High resolution images of each of Mars Hemispheres are obtained from the USGS Astrogeology site. Each of the links to the images are clicked in order to find the image url to the full resolution image.

## Step 2 - MongoDB and Flask Application
Using MongoDB and Flask, a new HTML page is created that displays all of the information that was scraped from the URLs above.


