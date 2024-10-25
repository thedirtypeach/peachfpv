import streamlit as st

# Set page configuration
st.set_page_config(page_title="PeachFPV Drone Services", layout="wide")

# Main sections as functions for modularity

# Header and Title
def header():
    st.title("PeachFPV - Drone Videography Services")
    st.subheader("Aerial Videography for Extreme Sports")

def introduction():
    st.write("""
    Welcome to PeachFPV's official page for showcasing aerial videography!
    We specialize in capturing high-energy action sports and drift cars from dynamic perspectives.
    Check out our latest video work below, and don’t hesitate to reach out for more information on our services.
    """)

# Video Portfolio Section
def video_portfolio():
    st.header("Video Portfolio")
    col1, col2 = st.columns(2)

    # Video embeds with titles and descriptions
    videos = [
        {"title": "Watercross", "url": "https://www.youtube.com/watch?v=FT0mK3k8gqc", "description": "An intense watercross shoot with fast, dynamic shots."},
        {"title": "Drift", "url": "https://www.youtube.com/watch?v=LNw8Nl3uDsQ", "description": "Capturing drift cars in high-speed action."},
        {"title": "Cinematic", "url": "https://www.youtube.com/watch?v=ulDy7NVAvWM", "description": "Showcasing a cinematic perspective with drone footage."},
        {"title": "Business", "url": "https://www.youtube.com/watch?v=Bvofbvz3CHE", "description": "Drone videography for business applications."}
    ]

    # Loop through videos with alternating columns
    for i, video in enumerate(videos):
        with col1 if i % 2 == 0 else col2:
            st.subheader(video["title"])
            st.video(video["url"])
            st.caption(video["description"])

# Instagram Feed
def instagram_feed():
    st.header("Instagram Videos")
    st.write("Check out our latest Instagram content directly from [PeachFPV](https://www.instagram.com/peachfpv/)")
    instagram_posts = [
        "https://www.instagram.com/p/DAV1cuSPKSo/embed",  # Replace with actual post links
        "https://www.instagram.com/p/CyQWDZTpA7c/embed"
    ]

    for index, post in enumerate(instagram_posts):
        if index % 2 == 0:
            col1, col2 = st.columns(2)
        with col1 if index % 2 == 0 else col2:
            st.components.v1.html(f"""
            <iframe width="320" height="440" src="{post}"
            frameborder="0" scrolling="no" allowtransparency="true"></iframe>
            """, height=500)

# Service Packages Section
def service_packages():
    st.header("Our Services")
    st.write("""
    **PeachFPV** offers a range of aerial videography services tailored for extreme sports enthusiasts. 
    We specialize in drifting, watercross, snowmobiling, business, and even Real Estate.
    """)

    packages = [
        {
            "name": "Basic Package",
            "price": "$199",
            "details": [
                "2-3 short-form videos (30 to 60 seconds each)",
                "Raw footage included"
            ]
        },
        {
            "name": "Pro Package",
            "price": "$349",
            "details": [
                "All features of Basic Package",
                "Extended video",
                "Highlight reel included"
            ]
        },
        {
            "name": "Premium Package",
            "price": "$799",
            "details": [
                "All features of Pro Package",
                "Full event coverage",
                "In-depth editing",
                "Personalized video production"
            ]
        }
    ]

    # Columns for service packages
    cols = st.columns(3)
    for col, package in zip(cols, packages):
        with col:
            st.subheader(package["name"])
            st.write(f"**{package['price']}**")
            for detail in package["details"]:
                st.write(f"- {detail}")

# Contact Information Section
def contact_section():
    st.header("Get in Touch")
    st.write("""
    Interested in our services or have questions? Reach out via [Instagram](https://www.instagram.com/peachfpv/)
    or or [Facebook](https://www.facebook.com/profile.php?id=61560869693299)
    """)
    # Subscription form for updates
    #st.subheader("Stay Updated")
    #email = st.text_input("Enter your email to subscribe:")
    #if st.button("Subscribe"):
        #if email:
        #    st.write(f"Thank you for subscribing, {email}!")
        #else:
        #    st.write("Please enter a valid email address.")

# Main Page Layout
header()
introduction()
video_portfolio()
instagram_feed()
service_packages()
contact_section()
