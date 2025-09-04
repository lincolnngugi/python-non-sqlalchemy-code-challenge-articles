#!/usr/bin/env python3

from lib.classes.many_to_many import Author, Article, Magazine

# Create authors
author1 = Author("Stephen King")
author2 = Author("J.K. Rowling")

# Create magazines
tech_mag = Magazine("Wired", "Technology")
fiction_mag = Magazine("Fantasy Today", "Fiction")

# Create articles
article1 = author1.add_article(tech_mag, "The Future of Horror in VR")
article2 = author1.add_article(fiction_mag, "Writing Scary Stories")
article3 = author2.add_article(fiction_mag, "Magic in Modern Literature")

# Demonstrate functionality
print("=== Authors and their articles ===")
print(f"{author1.name} has written {len(author1.articles())} articles")
print(f"{author2.name} has written {len(author2.articles())} articles")

print("\n=== Magazines and their contributors ===")
print(f"{tech_mag.name} has {len(tech_mag.contributors())} contributors")
print(f"{fiction_mag.name} has {len(fiction_mag.contributors())} contributors")

print("\n=== Topic areas by author ===")
print(f"{author1.name} writes about: {author1.topic_areas()}")
print(f"{author2.name} writes about: {author2.topic_areas()}")

print("\n=== Article titles by magazine ===")
print(f"{tech_mag.name} articles: {tech_mag.article_titles()}")
print(f"{fiction_mag.name} articles: {fiction_mag.article_titles()}")

print(f"\n=== Top publisher ===")
print(f"Magazine with most articles: {Magazine.top_publisher().name}")