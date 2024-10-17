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

# YouTube video embedding
st.subheader("YouTube Videos")
st.video("https://www.youtube.com/watch?v=FT0mK3k8gqc")  # Replace with your YouTube video URL
st.video("https://www.youtube.com/watch?v=LNw8Nl3uDsQ")  # Add more videos as needed

# Instagram embedding (Streamlit does not natively support Instagram embeds, so this uses an iframe)
st.subheader("Instagram Videos")
st.write("Instagram videos from PeachFPV")
st.components.v1.html("""
<iframe width="320" height="440" src="https://www.instagram.com/p/DAV1cuSPKSo/embed"
frameborder="0" scrolling="no" allowtransparency="true"></iframe>
""", height=500)  # Replace 'your_instagram_post_id' with actual Instagram post ID

# Service Packages Section
st.header("Our Services")
st.write("""
**PeachFPV** offers a range of aerial videography services tailored for extreme sports enthusiasts. 
Whether you're into drifting, skateboarding, or any action-packed sport, we can capture the moments from above!
""")

# Tiers of services with descriptions
st.subheader("Service Packages")
st.write("""
- **Basic Package ($199)**: Includes 2-3 short-form videos (up to 60 seconds each), and raw footage.
- **Pro Package**: Includes extended videos, advanced edits, and a highlight reel.
- **Premium Package**: Includes full event coverage, in-depth editing, and personalized video production.
""")

# Contact information
st.header("Get in Touch")
st.write("""
If you're interested in our services or have any questions, feel free to reach out via [Instagram](https://www.instagram.com/peachfpv/) 
or send us an email at: peachfpv@example.com.
""")

# Footer
st.write("Follow us on social media for the latest updates and behind-the-scenes footage of our shoots!")
