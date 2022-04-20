# Cosmetics-Recommendation
CMPE 255 - Term project

Cosmetics Recommendation

We are using the data that we got by web scraping and the data from OpenML.
The link for the data set in openML is https://www.openml.org/search?type=data&status=active&id=43481&sort=runs

It's always tough to try a new cosmetic product on your skin. It may react badly and cause skin inflammation. Consumers used to 
depend on recommended products from sellers i.e best selling products but these days one cannot blindly do this. The chemical 
components of products are identified using content-based filtering, and products with comparable constituent compositions are 
found using this method. If consumers lack information or have not found a product they like, they can use this method to enter 
their desired beauty impact instead of a product name. The goal of this proposal is to create a skincare product recommendation 
system based on the user's skin type and the product's ingredient composition.

Collaborative filters use the information provided by users, such as clicks, likes, purchases, etc. By using collaborative filtering 
we can identify similar users and suggest products that are being bought by similar users. So it might not recommend the products
that are suitable for the user's skin. Although a hybrid approach seems to have potential in the skincare domain, it requires a data 
set that involves both the behavioral information of the user as well as the product information. Such data set, however, is scarce
in skincare. so in the proposed method we are using content-based filtering which is unsupervised and t-SNE to plot the graphs and
get insight.