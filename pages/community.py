import streamlit as st
import datetime

# Page configuration
st.set_page_config(page_title="Community Forums", page_icon="👥", layout="wide")

# Initialize session state for posts if not exists
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = []

# Custom CSS
st.markdown("""
<style>
.forum-post {
    background: white;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.post-header {
    margin-bottom: 10px;
    color: #666;
    font-size: 0.9em;
}
.post-content {
    margin: 15px 0;
}
.post-footer {
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid #eee;
}
.category-tag {
    background: #e1e1e1;
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 0.8em;
}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Community Forums 👥")
st.markdown("""
Welcome to our community! Share your experiences and learn from others.
""")

# Create tabs
tab1, tab2 = st.tabs(["Browse Posts 📖", "Create Post ✍️"])

with tab1:
    # Display existing posts
    if not st.session_state.forum_posts:
        st.info("No posts yet! Be the first to share your experience.")
    
    for post in st.session_state.forum_posts:
        with st.container():
            st.markdown(f"""
            <div class="forum-post">
                <div class="post-header">Posted by {post['author']}</div>
                <h3>{post['title']}</h3>
                <span class="category-tag">{post['category']}</span>
                <div class="post-content">{post['content']}</div>
                <div class="post-footer">
                    ❤️ {post['likes']} likes • 💭 {len(post['comments'])} comments
                </div>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    # Create new post
    st.markdown("### Share Your Experience 📝")
    with st.form("new_post_form"):
        title = st.text_input("Title")
        category = st.selectbox(
            "Category",
            ["Disaster Experience", "Safety Tips", "Resources", "Recovery Story"]
        )
        content = st.text_area("Your Story")
        
        if st.form_submit_button("Post"):
            if title and content:
                new_post = {
                    "title": title,
                    "category": category,
                    "content": content,
                    "author": "Anonymous",
                    "timestamp": datetime.datetime.now(),
                    "likes": 0,
                    "comments": []
                }
                st.session_state.forum_posts.insert(0, new_post)
                st.success("Post created successfully!")
                st.experimental_rerun()
            else:
                st.error("Please fill in all fields!")