import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

def generate_blog_post(product_name, keywords):
    prompt = f"Write a 150-200 word SEO blog post about '{product_name}'. Naturally include the keywords: {', '.join(keywords)}."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes SEO blog posts."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        blog_content = response.choices[0].message.content.strip()
        print(f"Generated blog content for {product_name}.")
        return blog_content
    except Exception as e:
        print(f"Error generating blog content for {product_name}: {e}")
        return "Error generating blog content."
