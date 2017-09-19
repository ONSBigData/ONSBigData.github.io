---
title: 'Happy campers: Using machine learning to identify caravans in Zoopla data'
excerpt: 'Using machine learning to extract holiday homes in Zoopla data'
---


![][1]

Our Big Data team has published a [report][2] about collecting and using data from the property website Zoopla to identify the location of caravan homes. This information could help to make the census more efficient.

Caravan homes are important because they are recorded either inconsistently or not at all in different data sources. During the 2011 Census, when 85,000 such homes were counted, it was difficult to correctly count the number of people living in caravan parks, holiday sites and other leisure parks, and we spent a lot of time trying to establish the facts (such as whether the caravan park was for holiday or residential purposes).

## **Why use data from property websites?**

Property websites such as Rightmove and Zoopla show a lot of information about properties including their location, number of bedrooms, type of property and descriptive information about the home. It could be useful for identifying a range of features such as whether the property is in a gated community (we may have difficulty in getting to the front door of properties) and caravan homes.

## **What did we do to identify the caravan homes?**

A limited amount of data about properties for sale or rent can be collected from Zoopla for free, by writing some code to obtain data from their Application Programming Interface (API). We collected data about 36,000 properties, around 500 of which were caravan homes.

We built different machine learning models to try to identify caravans in the data using information such as the price (caravan homes tend to be cheaper), number of bedrooms and whether certain phrases (such as "static caravan") are in the property description. Some interesting oddities arose, such as large properties for sale that included a static caravan on their land, but overall we were able to identify the location of caravan homes with good accuracy.

## **What's next?**

Since we did this piece of work ONS has acquired two much larger sets of Zoopla data. Using these, we'll be redoing some of the [above work][2] (to make sure our model is robust). We will extend it to identify caravan homes used for holiday or residential purposes, gated communities and retirement properties.

## **Obtain the code we used**

It is important for us to make as much code openly available as possible. The code used to extract property data from the Zoopla API and the machine learning code used in the report published (both written in Python) are available on [the ONS Big Data team GitHub pages][3].

## **Contact us**

We would also love to get your feedback on what we've done or for you to suggest further ways in which the methods or data could be used. Please do so by contacting [Karen Gask][4] or the [Big Data team][5]. We've also been working on using satellite imagery to identify the location of caravan homes so we'll be writing a blog about that soon.

> Written by [Karen Gask][https://twitter.com/GaskyK], Data Scientist, and originally posted in the [ONS Digital blog](https://digitalblog.ons.gov.uk/2017/06/21/happy-campers-using-machine-learning-to-identify-caravans-in-zoopla-data/)

[1]: https://digitalblog.ons.gov.uk/wp-content/uploads/sites/9/2017/06/80a4240c.png
[2]: https://www.ons.gov.uk/methodology/methodologicalpublications/generalmethodology/onsworkingpaperseries/onsmethodologyworkingpaperseriesno11identifyingcaravanhomesinzoopladatajune2017
[3]: https://github.com/ONSBigData/housing-websites
[4]: mailto:karen.gask%40ons.gov.uk
[5]: mailto:ons.big.data.project%40ons.gov.uk
