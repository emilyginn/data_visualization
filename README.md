# Data Visualization Projects

## Project 1: [African Sunlight Hours](data_visualization/africa_sunlight_hours.ipynb)

This data visualization presents the average number of sunlight hours by month in each African country. The link to the data can be found [here](https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration#Africa). The inspiration for this project comes from [a Tableau workbook](https://public.tableau.com/app/profile/owen.barnes/viz/SunlightinEurope/Dashboard5) I came across a couple of years ago and it's always stuck with me. I wanted to be able to create something similar using data visualization libraries in Python. One of the ways my adaptation differentiates from the inspiration, is that I chose to showcase sunlight hours for Africa instead of Europe. The idea behind this decision is that Africa splits along the equator, making for some interesting comparisons in sunlight hours among countries that fall above and below the equator.

The data is presented as a series of bar charts in a grid-like fashion using seaborn's 'FacetGrid' function. Each subplot represents a different country. The x-axis displays each month of the year, and the y-axis represents the average number of sunlight hours for each respective month, along with the coloring of the bars. This project effectively showcases skills in data manipulation and visualization using an array of Python libraries.

Moving forward, I plan to make the following updates in upcoming iterations:

1. Add hover features to the bar charts.
2. Include which month had the maximum amount of sunlight hours for each country.
3. Add an interactive time series heat map of Africa for the average monthly sunlight hours.
4. Incorporate visualizations into a web app format

![image](https://github.com/emilyginn/data_visualization/assets/122908049/32d390ea-efe5-47da-940b-6696d9510a58)
