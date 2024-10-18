import streamlit as st

# Set page configuration
st.set_page_config(page_title="PeachFPV Drone Services", layout="wide")

# Title and introduction
st.title("PeachFPV - Drone Videography Services")
st.subheader("Aerial Videography for Extreme Sports")

# Introduction section
st.write("""
Welcome to PeachFPV's official page for showcasing aerial videography! 
We specialize in capturing high-energy action sports and drift cars from dynamic perspectives. 
Check out our latest video work below, and don't hesitate to contact us for more information on our services.
""")

# Video Section
st.header("Video Portfolio")

# Create columns to display videos side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Watercross")
    st.video("https://www.youtube.com/watch?v=FT0mK3k8gqc")  # Replace with your YouTube video URL

with col2:
    st.subheader("Drift")
    st.video("https://www.youtube.com/watch?v=LNw8Nl3uDsQ")  # Add more videos as needed

with col1:
    st.subheader("Cinematic")
    st.video("https://www.youtube.com/watch?v=ulDy7NVAvWM")  # Replace with your YouTube video URL

with col2:
    st.subheader("Business")
    st.video("https://www.youtube.com/watch?v=Bvofbvz3CHE")  # Add more videos as needed

# Instagram embedding (improved look)
st.header("Instagram Videos")
st.write("Check out our latest Instagram content directly from [PeachFPV](https://www.instagram.com/peachfpv/)")
instagram_posts = [
    "https://www.instagram.com/p/DAV1cuSPKSo/embed",  # Replace with actual post links
    "https://www.instagram.com/p/CyQWDZTpA7c/embed"   # Add more if needed
]

# Display Instagram posts in two columns dynamically
for index, post in enumerate(instagram_posts):
    if index % 2 == 0:
        col1, col2 = st.columns(2)
    with col1 if index % 2 == 0 else col2:
        st.components.v1.html(f"""
        <iframe width="320" height="440" src="{post}"
        frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, height=500)

# Service Packages Section with columns
st.header("Our Services")
st.write("""
**PeachFPV** offers a range of aerial videography services tailored for extreme sports enthusiasts. 
We specialize in drifting, watercross, snowmobiling, business, and even Real Estate.
""")

# Use columns for service packages
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Basic Package")
    st.write("""
    **$199**  
    - 2-3 short-form videos (30 to 60 seconds each)  
    - Raw footage included
    """)

with col2:
    st.subheader("Pro Package")
    st.write("""
    **$349**
    - All previously mentioned tiers
    - Extended video
    - Highlight reel included
    """)

with col3:
    st.subheader("Premium Package")
    st.write("""
    **$799**
    - All previously mentioned tiers
    - Full event coverage
    - In-depth editing  
    - Personalized video production
    """)

# Contact information
st.header("Get in Touch")
st.write("""
If you're interested in our services or have any questions, feel free to reach out via [Instagram](https://www.instagram.com/peachfpv/) 
or send us an email at: peach@impactmodulation.com.
""")

# Footer
st.write("Follow us on social media for the latest updates and behind-the-scenes footage of our shoots!")
