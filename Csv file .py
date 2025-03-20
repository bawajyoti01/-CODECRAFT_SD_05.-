import csv

class Product:
    def __init__(self, name, brand, price, rating, reviews, availability, description, link):
        self.name = name
        self.brand = brand
        self.price = price
        self.rating = rating
        self.reviews = reviews
        self.availability = availability
        self.description = description
        self.link = link

    def to_list(self):
        return [self.name, self.brand, self.price, self.rating, self.reviews, self.availability, self.description, self.link]

# List of products
products = [
    Product("Plix Protein Powder - Chocolate", "Plix", "INR 2,499.00", "4.5 out of 5 stars", "1,245", "In Stock",
            "Delicious chocolate-flavored plant-based protein powder with essential amino acids and vitamins.", "https://www.amazon.in/dp/B08XYZ1234"),
    
    Product("Plix Vegan Protein - Vanilla", "Plix", "INR 2,899.00", "4.3 out of 5 stars", "982", "Only 5 left in stock",
            "Vanilla-flavored vegan protein made from organic peas and brown rice.", "https://www.amazon.in/dp/B08XYZ5678"),
    
    Product("Plix Plant-Based Protein - Berry", "Plix", "INR 2,299.00", "4.6 out of 5 stars", "1,560", "In Stock",
            "Berry blast plant-based protein with antioxidants and superfoods.", "https://www.amazon.in/dp/B08XYZ9101"),
    
    Product("Plix Superfood Protein - Mocha", "Plix", "INR 2,799.00", "4.7 out of 5 stars", "870", "Limited Stock",
            "Mocha-flavored protein blend with added superfoods for energy and recovery.", "https://www.amazon.in/dp/B08XYZ1123"),
    
    Product("Plix Whey-Free Protein - Coffee", "Plix", "INR 3,199.00", "4.2 out of 5 stars", "764", "Out of Stock",
            "Whey-free protein infused with real coffee extract for a morning boost.", "https://www.amazon.in/dp/B08XYZ1415"),
]

# Function to save products to CSV
def save_to_csv(filename="products.csv"):
    headers = ["Product Name", "Brand", "Price (INR)", "Rating", "Reviews", "Availability", "Description", "Link"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write column headers
        for product in products:
            writer.writerow(product.to_list())  # Write product data

# Save data to CSV
if __name__ == "__main__":
    save_to_csv("products.csv")
    print("Product data saved to 'products.csv' successfully!")
