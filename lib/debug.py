#!/usr/bin/env python3

import ipdb
from classes.many_to_many import *

if __name__ == '__main__':
    # Create sample instances for testing
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Fashion Weekly", "Fashion")
    
    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Spring Fashion Trends")
    article3 = Article(author2, magazine1, "Quantum Computing Basics")
    
    print("Sample data created:")
    print(f"Authors: {author1.name}, {author2.name}")
    print(f"Magazines: {magazine1.name}, {magazine2.name}")
    print(f"Articles: {article1.title}, {article2.title}, {article3.title}")
    print("\nStarting ipdb session...")
    
    ipdb.set_trace()