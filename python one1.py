# ==========================================================
# Project: Product Recommendation System
# PS Number: 88
# Student Name: Dharmendra Singh
# ERP ID: RU-2026-00944
# Branch: BCA
# Semester: 1
# ==========================================================

# Store products purchased by each customer
purchases = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}


# Calculate Jaccard similarity between two customers
def jaccard_similarity(items1, items2):
    set1 = set(items1)
    set2 = set(items2)

    intersection = set1 & set2
    union = set1 | set2

    if not union:
        return 0.0

    return len(intersection) / len(union)


# Find the most popular product
def find_popular_product():
    popularity = {}

    for items in purchases.values():
        for product in set(items):
            popularity[product] = popularity.get(product, 0) + 1

    popular_product = max(
        popularity,
        key=popularity.get
    )

    return popular_product, popularity[popular_product]


# Recommend a product to the selected customer
def recommend_product(customer):

    # Handle empty input
    if not customer:
        print("Name cannot be empty.")
        return

    # Handle invalid customer names
    if customer not in purchases:
        print(f"Customer '{customer}' not found.")
        return

    customer_items = set(purchases[customer])
    similarities = {}

    # Calculate similarity with other customers
    for other in purchases:
        if other != customer:
            similarities[other] = jaccard_similarity(
                purchases[customer],
                purchases[other]
            )

    # Recommend the popular product if all scores are zero
    if all(score == 0 for score in similarities.values()):
        print("No similar customers found.")
        product, count = find_popular_product()
        print(
            f"Popular product: {product} "
            f"(bought by {count} customers)"
        )
        return

    # Sort customers by similarity, highest score first
    ranked = sorted(
        similarities.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Display similarity scores with two decimal places
    print("Similarity scores:")
    for name, score in ranked:
        print(f"{name} : {score:.2f}")

    # Select the most similar customer
    best_customer = ranked[0][0]
    print(f"Most similar customer: {best_customer}")

    # Recommend a product not already purchased
    for product in purchases[best_customer]:
        if product not in customer_items:
            print(f"Recommended: {product}")
            return

    print("No new products to recommend.")


# Main program: accept multiple names in one run
while True:
    try:
        customer_name = input("Recommend for: ").strip()
    except EOFError:
        break

    # Type exit to stop the program
    if customer_name.lower() == "exit":
        break

    recommend_product(customer_name)