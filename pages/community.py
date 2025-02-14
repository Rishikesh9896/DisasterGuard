import streamlit as st
import datetime

# Page configuration
st.set_page_config(
    page_title="Community Forums",
    page_icon="👥",
    layout="wide"
)

# Initialize session state for posts if not exists
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = []

# Custom CSS to enforce white text visibility
st.markdown(f"""
    <style>
        .stApp {{
            background: url("https://wallpapercave.com/wp/wp11136313.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}
        .forum-post {{
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: all 0.3s ease-in-out;
            color: black;
        }}
        .forum-post:hover {{
            transform: scale(1.02);
            box-shadow: 0 6px 10px rgba(0,0,0,0.3);
        }}
        .post-header, .post-footer, .post-content {{
            color: black;
        }}
        .category-tag {{
            background: #3498db;
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 0.9em;
            color: white;
            font-weight: bold;
        }}
        .stButton > button {{
            width: 100%;
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #1f78c1;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }}
        /* Ensuring white text visibility for tabs & filters */
        .stTabs [role="tab"] > div {{
            color: white !important;
            font-weight: bold !important;
        }}
        .stSelectbox label, .stTextInput label, .stTextArea label {{
            color: white !important;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🌟 **Community Forums** 👥")
st.markdown("""  
### **Share your experiences, ask questions, and connect with others in our disaster preparedness community.**  
""")

# Create tabs with improved white text visibility
tab1, tab2, tab3 = st.tabs([
    "📢 **BROWSE POSTS**",  
    "📝 **CREATE A POST**",  
    "🔍 **SEARCH DISCUSSIONS**"
])

with tab1:
    if not st.session_state.forum_posts:
        st.info("🚀 **No posts yet! Be the first to share your experience.**")
    else:
        # **Filter section with white text**
        category_filter = st.selectbox(
            "📂 **FILTER BY CATEGORY**",
            ["All Categories", "Disaster Experience", "Safety Tips", "Resources", "Recovery Story"]
        )
        
        # **Display posts based on filtering**
        for post in st.session_state.forum_posts:
            if category_filter == "All Categories" or post["category"] == category_filter:
                with st.container():
                    st.markdown(f"""
                    <div class="forum-post">
                        <div class="post-header">
                            ✍️ <b>Posted by {post['author']} • {post['timestamp'].strftime('%Y-%m-%d %H:%M')}</b>
                        </div>
                        <h3><b>{post['title']}</b></h3>
                        <span class="category-tag">{post['category']}</span>
                        <div class="post-content">{post['content']}</div>
                        <div class="post-footer">
                            ❤️ {post['likes']} Likes • 💬 {len(post['comments'])} Comments
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Like button and comments
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if st.button("❤️ Like", key=f"like_{post['timestamp']}"):
                            post['likes'] += 1
                            st.rerun()
                    
                    # Comments section
                    with st.expander("💬 **VIEW & ADD COMMENTS**"):
                        for comment in post['comments']:
                            st.markdown(f"""
                            <div style='padding: 10px; border-left: 3px solid #3498db; margin: 5px 0; color: black; font-weight: bold;'>
                                <small>{comment['author']} • {comment['timestamp'].strftime('%Y-%m-%d %H:%M')}</small>
                                <p>{comment['content']}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Add new comment
                        new_comment = st.text_area("💭 **Write a comment**", key=f"comment_{post['timestamp']}")
                        if st.button("➕ **Submit Comment**", key=f"post_comment_{post['timestamp']}"):
                            if new_comment:
                                post['comments'].append({
                                    'author': 'Anonymous',
                                    'content': new_comment,
                                    'timestamp': datetime.datetime.now()
                                })
                                st.success("✅ **Comment added!**")
                                st.rerun()

with tab2:
    st.markdown("## **📝 SHARE YOUR STORY**")
    with st.form("new_post_form"):
        title = st.text_input("📝 **Title of Your Post**")
        category = st.selectbox(
            "📌 **Choose a Category**",
            ["Disaster Experience", "Safety Tips", "Resources", "Recovery Story"]
        )
        content = st.text_area("🖊️ **Describe Your Experience**")
        
        if st.form_submit_button("🚀 **Post Now**"):
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
                st.success("✅ **Post created successfully!**")
                st.rerun()
            else:
                st.error("⚠️ **Please complete all fields!**")

with tab3:
    st.markdown("## 🔍 **SEARCH FORUM POSTS**")
    search_term = st.text_input("🔎 **Enter a Keyword to Search**")
    if search_term:
        found_posts = False
        for post in st.session_state.forum_posts:
            if search_term.lower() in post['title'].lower() or search_term.lower() in post['content'].lower():
                found_posts = True
                st.markdown(f"""
                <div class="forum-post">
                    <div class="post-header">📌 <b>Posted by {post['author']}</b></div>
                    <h3><b>{post['title']}</b></h3>
                    <span class="category-tag">{post['category']}</span>
                    <div class="post-content">{post['content']}</div>
                </div>
                """, unsafe_allow_html=True)
        
        if not found_posts:
            st.info("⚠️ **No matching posts found. Try a different keyword!**")
