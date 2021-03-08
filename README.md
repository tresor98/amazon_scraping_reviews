# Amazon Scraper
Scraping through reviews on amazon given a list of product ids.
The first code (amazon_reviews.ipynb) scrape syncronously thus is a bit slower
The second code(faster_webscraping) scrapes asyncrously thus going faster.

The code will fecth:
<ol>
  <li>Get through the pages of each product id comments section</li>
<li>Fetch each comment with its title, rating, verification status, author_url, author, review_date and the how many people found it helpful </li>
  <li>The code will go through all possible comments pages</li>
  <li>Comments related to each product id will be stored in a json file</li>
</ol>

It is recommend to use a VPN while using the codes for a better results.

You might need to rerun the code for the data that returned empty list as data for some product ids may not be fetched at the first attempt.
