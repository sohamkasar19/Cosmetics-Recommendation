# Cosmetics-Recommendation
## CMPE 255 - Term project

## Team members
* Shrisha Shridhar Hegde - shrishashegde
* Soham Chandrakant Kasar - sohamkasar19
* Sai Sri Harshini Kosuri - Harshinikosuri
* Srikanth Nimmagadda - nisrika1

We are using the data that we got by web scraping and the data from OpenML. The link for the data set in openML is https://www.openml.org/search?type=data&status=active&id=43481&sort=runs

# Introduction

A cosmetic recommendation concerning skin trouble is a complex issue. It may react badly and cause skin inflammation. Consumers usually depend on recommended products from sellers i.e best selling products but these days one cannot blindly do this. We know the information we need is on the back of each product, but it’s really hard to interpret those ingredient lists unless you’re a chemist. So we decided to create a cosmetic recommendation system.

There could be some people who share a very similar taste for cosmetics. And with user-user collaborative filtering, we can recommend new products based on the ranking values of this neighboring group. However, the skin type and feature of a person is a more sensitive and ticky problem than just recommending your tonight’s movie show.  To get the reliability and stability in the recommendation, we need to focus on the real content of each product, or the ingredients of products, and get the similarities based on them. Although a hybrid approach seems to have potential in the skincare domain, it requires a data set that involves both the behavioral information of the user as well as the product information. Such data set, however, is scarce in skincare.

# Procedure

As a first step, we would like to web scrap from Sephora. To focus on the skin care items, the dataset contains six different categories — moisturizing cream, facial treatments, cleanser, facial mask, eye treatment, and sun protection. We are aiming at restricting the dataset around 1500 items. We are thinking to also include the brand, the price, the rank(rating), skin types and ingredients for each item. These are the features included in the dataset link given above, for some reason if website does not mention some of these features we are thinking to replace it with any other feature or completely remove the feature.

In the second step we would like to use content-based recommendation system which is an unsupervised learningto cluster similar items together based on the ingredients in an item. The components of the content based recommender system would include creating Document Term Matrix (DTM). Here each cosmetic product will correspond to a document, and each chemical composition will correspond to a term. This means we can think of the matrix as a “cosmetic-ingredient” matrix.

As a final step we would like to use t-SNE dimensionality reduction technique to two dimensions and create a scatter plot. Each point in this scatter plot would indicate an item. The items having similar ingredients would appear closer to each other when compared to items having different ingredients.

# Data Pre-processing
## Data cleaning
Data cleaning is the process of removing the data which is incorrect, wrongly formatted, duplicate data or incomplete dats within the dataset.
When the data is combined from multiple resources there is lot of duplicate or mislabeled data in combined csv file.
It removes the data that should not be included in the dataset.
### STEPS FOR DATA CLEANING:
1. Remove duplicate and unwanted data
2. Structural errors must be corrected: you may find “N/A” and “Not Applicable” as different, but they should be analyzed as the same category.
3. Outliers must be filtered:  Irrelevant outliers must be removed.
4. Handling missing values:
- we can drop the missing values but there is a chance of loosing the information
- Missing values can be filled with the assumptions from the observations but then there a chance of loosing integrity of the data, because the values are filled from assumptions not observations.
- Can be filled with null values.
5. Validate the cleaned dataset: before using the cleaned data validate it if it make sense then proceed with the cleaned csv file.


