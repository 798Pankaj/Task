import streamlit as st
from main import run_pipeline

st.set_page_config(page_title="AI SEO Blog Generator", layout="wide")
st.title("📝 AI SEO Blog Post Creator")

def main():
    st.sidebar.header("Input Parameters")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    products_input = st.sidebar.text_area("Products and Keywords (JSON format)", height=200, value='[{"product": "Product A", "keywords": ["keyword1", "keyword2"]}, {"product": "Product B", "keywords": ["keyword3", "keyword4"]}]')

    try:
        products = []
        if products_input:
            products = eval(products_input)  # Using eval for simplicity; in production use json.loads with validation

        if st.button("Generate Blog Posts"):
            if not api_key:
                st.error("Please enter your OpenAI API key.")
                return
            if not products:
                st.error("Please enter valid products and keywords.")
                return

            with st.spinner("Generating blog posts..."):
                blog_data = run_pipeline(products, api_key)
                
                if blog_data:
                    for entry in blog_data:
                        st.subheader(entry['product'])
                        st.write(f"**Keywords**: {', '.join(entry['keywords'])}")
                        st.write(entry['content'])
                else:
                    st.write("No blog data found. Check the logs for details.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
