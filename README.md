# Final Project:Thirds-the-Charm
# <u>National Economic Accounts</u>
<hr> </hr>
## Description/Purpose

This project creates a database for purpose of comparing  worldwide national income account-type variables. To allow for accurate comparisons, some of our data has been converted to  converted to international prices. The homogenization of national accounts to a common numeraire allows for accurate comparisons of income between countries. Our database utilizes various comparable statistics to asses these differences. For the purpose of our project, we drew on data sets related to levels of education by gender and the ease of doing business in a country. We believe the information derived from these data sets provide meaningful insights into the economic realities of the nations examined. (ex: How levels of educational attainment, highest level of education completed, relate to household consumption. However, that is out-of-scope for now!).

## Our Data

Before explaining the data sets used in this project, it is important to understand how we chose the data. One factor we had to consider was the time period we would examine. Economic development in the 1950's was a lot different compared to that experience in the 1990's and today. Prior to wave of globalization at the end of the 20th century, markets were primarily local or regional. With the advent of communications and payment technologies, global markets experienced a flattening. New technologies, coupled with an increasing number of trade deals, lowered barriers of entry and allowed for nations to transition from regional to global market  participants. As a result, macroeconomic influences became more profound and common between national markets.

For the purpose of this project, we chose to explore data between the years of 2007-2009. Data from this period was abundant and recent. We also believed that global markets at this time were reaching maturity and influencers, while by no means uniform, would be more common among all participants. Data Science is also an emerging field, data sourced from earlier timeframes may not have exhibited best in practice techniques or been as complete for all our participants.    

#### National Economic Accounts

The foundation of our project, we were able to obtain National Economic Account data from the [Wharton Research Data Services](https://wrds-www.wharton.upenn.edu/pages/). National Income Accounts are means by which of government or NGO can measure the level of economic activity of a country within a given period of time. While not a complete measure, data sets like this provide useful insight into the such things as standards of living or dependence on foreign markets. In our dataset we were given information relating to population, consumption, government consumption, domestic investment, imports, exports, and type of currency.

Values for products were originally given in terms of that nations local currency. Given the need for a common metric, we utilized [myexchangerateapiutil.py](myexchangerateapiutil.py) to convert all currencies to a standard unit of measure. This was critical to bringing the data together. Without a common unit of measure, it would have been impossible to compare nations data.   


#### Ease of Business

Our Ease of Business data was also obtained through the [Wharton Research Data Services](https://wrds-www.wharton.upenn.edu/pages/).Data from this sheet covers traditional economic barriers of entry when starting a business. The data provided by WRDS covers variables such as time required to start a business (days), total tax as % of profit, and the average cost to register a property within the country.  

#### Education

Education data was sourced from [link](Iforgetwhereexactly.com). Given the importance of educated work force in the modern economy, we felt data related to the level of educational attainment vital to our work. Attributes gained from this data sheet included adjusted net enrolment rates by sex, literacy, graduation ratios, and education enrollment rates. However, this data sheet was far from perfect. Not all countries had kept or chose not to submit records for certain variables. While this was not ideal, we believed the effect was negligible. Drastic changes to levels of education are generational and, given the scope of our project, we did not believe it would impact our results.

----
  ## Designing the Database



#### ERD Diagram

(fix link first)
