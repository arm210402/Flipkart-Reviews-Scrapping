import requests
from bs4 import BeautifulSoup
import csv

def url_modifier(url):
    url_modified = url.replace("/p/", "/product-reviews/")
    third_ampersand = url_modified.find('&', url_modified.find('&', url_modified.find('&') + 1) + 1)
    if third_ampersand != -1:
        url_modified = url_modified[:third_ampersand]

    url_modified = url_modified + "&page="
    return url_modified

def get_reviews(start_page: int, end_page: int, url: str) -> list[tuple[str, str]]:
    url_i = url
    url_f = url_modifier(url_i)
    print(url_f)
    reviews = []
    prev_rev = ""
    for page in range(start_page, end_page + 1):
        url = f"{url_f}{page}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            # reviews_count = soup.find("span", class_="_2_R_DZ").text.strip().split("&")[1].strip().split()[0].replace(',','')
            # product_name = soup.find('span', {'class': 'B_NuCI'}).text
            # print("Product Name:", product_name)
            # print("Number of Reviews:", reviews_count)
            review_containers = soup.select(".t-ZTKy")

            rating_containers = soup.select("._3LWZlK")
            # Skip the first rating container (the average rating)
            for i in range(1, len(review_containers) - 1):
                review = review_containers[i].text.strip()

                rating = rating_containers[i].text.strip()
                if i == 1:
                    prev_rev = review
                else:
                    reviews.append((prev_rev, rating))
                    prev_rev = review
        except Exception as e:
            print(f"Error fetching reviews from page {page}: {e}")
    return reviews


user_link = input("Enter Product Url", "")
title = requests.get(user_link)
soup = BeautifulSoup(title.content, "html.parser")

# Replace '20' with any number of reviews you want 10 per page (here 20*10= 200 reviews will be generated)
reviews = get_reviews(1, 20, user_link)

# Save reviews to a CSV file
with open("flipkart_reviews.csv", mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Rating", "Review"])
    for review, rating in reviews:
        writer.writerow([rating, review])
