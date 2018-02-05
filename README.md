# SF Software Salary

## Summary
Many online tools and platforms exist online that help us determine our self worth.  However, most of these rely on the user creating cumbersome, complicated profiles.  The data they generate is produced from a possibly unreliable data source with a method unknown to the user.

The script in this repository is catered towards software developer jobs in San Francisco.

In order to help validate these results or even potentially replace them, we can compare one's salary against an accurate and representative set of H1B data.

For more information, feel free to visit my blog here:
https://leejustin.com/blog/3701016340289169098

## Design
The script is a simple Python script that uses the `requests` and `BeautifulSoup` libraries to scrape the H1B data source. Unwanted results such as manager positions are filtered out. The data is then adjusted for annual cost-of-living changes using the Bureau of Labor Statistics' Consumer Price Index.

## Usage
Use pip to install the `BeautifulSoup` `requests` and `statistics` libraries.

```python run.py COMPANY_NAME```
