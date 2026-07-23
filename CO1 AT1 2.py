import re

products = [
    "Apple iPhone 15",
    "Apple Watch",
    "Samsung Galaxy S24",
    "Samsung Smart TV",
    "Dell Laptop",
    "HP Laptop",
    "Lenovo Laptop",
    "Sony Headphones",
    "Boat Headphones",
    "Apple AirPods",
    "LG Refrigerator",
    "Whirlpool Washing Machine",
    "Canon Camera",
    "Nikon Camera",
    "Python Programming Book"
]

# -----------------------------------------
# Exact Search
# -----------------------------------------
def exact_search(keyword):
    pattern = r'^' + re.escape(keyword) + r'$'
    return [p for p in products if re.search(pattern, p)]


# -----------------------------------------
# Prefix Search
# -----------------------------------------
def prefix_search(prefix):
    pattern = r'^' + re.escape(prefix)
    return [p for p in products if re.search(pattern, p)]


# -----------------------------------------
# Suffix Search
# -----------------------------------------
def suffix_search(suffix):
    pattern = re.escape(suffix) + r'$'
    return [p for p in products if re.search(pattern, p)]


# -----------------------------------------
# Partial Keyword Search
# -----------------------------------------
def partial_search(keyword):
    pattern = re.escape(keyword)
    return [p for p in products if re.search(pattern, p)]


# -----------------------------------------
# Case-Insensitive Search
# -----------------------------------------
def case_insensitive_search(keyword):
    pattern = re.escape(keyword)
    return [p for p in products if re.search(pattern, p, re.IGNORECASE)]


# -----------------------------------------
# Display Results
# -----------------------------------------
def display_results(title, result):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    if result:
        for product in result:
            print(product)
    else:
        print("No matching products found.")

    print("Total Matches:", len(result))


# -----------------------------------------
# Main Program
# -----------------------------------------
exact = exact_search("Dell Laptop")
prefix = prefix_search("Apple")
suffix = suffix_search("Laptop")
partial = partial_search("Camera")
case_insensitive = case_insensitive_search("python")

display_results("1. Exact Search", exact)
display_results("2. Prefix Search", prefix)
display_results("3. Suffix Search", suffix)
display_results("4. Partial Search", partial)
display_results("5. Case-Insensitive Search", case_insensitive)
