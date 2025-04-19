from blog_generator import generate_blog_post

def process_data(products, api_key):
    blog_data = []
    for item in products:
        content = generate_blog_post(item["product"], item["keywords"], api_key)
        blog_data.append({
            "product": item["product"],
            "keywords": item["keywords"],
            "content": content
        })
    return blog_data

def run_pipeline(products, api_key):
    return process_data(products, api_key)
