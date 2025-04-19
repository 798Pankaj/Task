from blog_generator import generate_blog_post

def process_data():
    # Example dummy data for demonstration
    products = [
        {"product": "Product A", "keywords": ["keyword1", "keyword2"]},
        {"product": "Product B", "keywords": ["keyword3", "keyword4"]}
    ]
    blog_data = []
    for item in products:
        content = generate_blog_post(item["product"], item["keywords"])
        blog_data.append({
            "product": item["product"],
            "keywords": item["keywords"],
            "content": content
        })
    return blog_data

def run_pipeline():
    return process_data()
