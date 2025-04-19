import openai

def generate_blog_post(product_name, keywords, api_key):
    if not api_key:
        raise ValueError("API key must be provided.")
    openai.api_key = api_key
    prompt = f"Write a 150-200 word SEO blog post about '{product_name}'. Naturally include the keywords: {', '.join(keywords)}."
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        blog_content = response.choices[0].text.strip()
        print(f"Generated blog content for {product_name}.")
        return blog_content
    except Exception as e:
        print(f"Error generating blog content for {product_name}: {e}")
        return "Error generating blog content."
