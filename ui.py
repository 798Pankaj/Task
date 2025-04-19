import streamlit as st
from main import process_data, run_pipeline

st.set_page_config(page_title="AI SEO Blog Generator", layout="wide")
st.title("📝 AI SEO Blog Post Creator")

def main():
    try:
        if st.button("Generate Blog Posts"):
            with st.spinner("Generating blog posts..."):
                blog_data = run_pipeline()
                
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
