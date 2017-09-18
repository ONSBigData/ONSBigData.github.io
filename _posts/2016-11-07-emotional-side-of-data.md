---
title: 'The ‘emotional’ side of data'
---

Working in our Big Data team means working with large datasets and looking at a wider variety of data sources than in traditional statistical work. This includes data from images and from text. We have been exploring how to analyse and use such sources in the team. We have been learning Natural Language Processing techniques to improve our skills in text analysis and text mining. Here are a few ways we have been getting our hands dirty with this type of data.

## What is Natural Language Processing?

Natural Language Processing can help us understand lots of text in an automated way, especially where the text might be so big that it might be infeasible for us to read it all. Some methods are aimed at differentiating between emotions while other methods are better for classifying text talking about different things or for retrieving the answer to a question.

## So how can Natural Language Processing be applied in official statistics?

Here are some examples from our work:

### Classification problems

It is important for Census Field Operations to know where people are living and where they are not. During the 2011 Census we repeatedly tried to contact people in properties which were actually vacant. If we can identify vacant properties in advance, we'll save money.

We manually classified 500 descriptions of caravans for sale or rent from property websites (such as Rightmove or Zoopla) into whether they were for holiday or residential use. From that we could see which words were most correlated with being in a holiday or residential description. Unsurprisingly, the words most correlated with holiday caravans included "pool", "bar", "restaurant" and "beach" and we were able to classify about 90% of descriptions accurately based on what we found. We are working with the Census Transformation Programme at ONS to evaluate whether this approach can be used on a larger scale.

### Automated thematic analysis of text

The [Sustainable Development Goals][2] (SDGs) aim to end poverty, fight inequality and injustice, and tackle climate change by 2030. Goal 12 is to ensure sustainable consumption and production patterns. One of the indicators is "To encourage companies, especially large and transnational companies, to adopt sustainable practices and to integrate sustainability information into their reporting cycle". This is an area for which no official data is collected. The data science techniques we have developed could fill that gap.

We've built programs to automatically find sustainability reports on the websites of 100 of the UK's largest companies and found that 59 out of 100 had sustainability reports. We then analysed the sustainability text on their websites and found that the focus of their efforts varied depending on the industrial sector of the company. For example:

* construction companies are more likely to focus on their environmental policies
* the service sector is more likely to focus on charitable work

[Explore an interactive visualisation][3] of the words identified in the main 15 topics.

### Analysing written responses to qualitative survey questions

Over the summer, a review of our Methodology divisions was undertaken and we were asked to provide a sentiment analysis from a survey of 120 staff. We found the majority of people like working in Methodology and find the work challenging.

We used the same methods for this work as [this data scientist][4], who discovered that 2 people write Donald Trump's tweets and that he writes the angrier ones.

## Summary

Natural Language Processing is a growing area and we think there are opportunities for using these techniques in official statistics; either for producing new statistics or for improving operational processes such as coding.

Our next steps are working with internal crime and health teams … watch this space!

Can you think of any opportunities for analysing text in your work? We would love to hear examples of how these techniques are being applied! To share ideas, examples or chat about Natural Language Processing, contact [Karen Gask][5] or our [Big Data team][6].

> Written by [Karen Gask][1], Data Scientist, and originally posted in the [ONS Digital blog](https://digitalblog.ons.gov.uk/2016/11/07/the-emotional-side-of-data/)


[1]: https://twitter.com/GaskyK
[2]: http://www.un.org/sustainabledevelopment/sustainable-development-goals/
[3]: http://bl.ocks.org/AlessandraSozzi/raw/ce1ace56e4aed6f2d614ae2243aab5a5/#topic=0&lambda=1&term=https://goo.gl/NZH7ql
[4]: https://www.washingtonpost.com/posteverything/wp/2016/08/12/two-people-write-trumps-tweets-he-writes-the-angrier-ones/?utm_term=.b086dc08d9c5
[5]: mailto:karen.gask%40ons.gov.uk
[6]: mailto:ons.big.data.project%40ons.gov.uk
