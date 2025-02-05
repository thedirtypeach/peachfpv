import streamlit as st

# Set page configuration
st.set_page_config(page_title="PeachFPV", layout="wide")

# Main sections as functions for modularity

# Header and Title
def header():
    # Hero section
    st.header('Capturing the Extreme', divider='rainbow')

def introduction():
    st.write("""
    Welcome to PeachFPV's official page for showcasing FPV video!
    We specialize in capturing high-energy action sports and drift cars from dynamic perspectives.
    Check out our latest videos below or click [here](https://www.instagram.com/peachfpv/) to send
    us a message!
    """)

# Video Portfolio Section
def video_portfolio():
    col1, col2 = st.columns(2)

    # Video embeds with titles and descriptions
    videos = [
        {"title": "Watercross", "url": "https://www.youtube.com/watch?v=FT0mK3k8gqc", "description": "An intense watercross shoot with fast, dynamic shots."},
        {"title": "Drift", "url": "https://www.youtube.com/watch?v=LNw8Nl3uDsQ", "description": "Capturing drift cars in high-speed action."},
        {"title": "Cinematic", "url": "https://www.youtube.com/watch?v=ulDy7NVAvWM", "description": "Showcasing a cinematic perspective with drone footage."},
        {"title": "Business", "url": "https://www.youtube.com/watch?v=Bvofbvz3CHE", "description": "Drone videography for business applications."}
    ]

    # Create a grid layout for videos
    cols = st.columns(2)  # Adjust the number for layout
    for index, video in enumerate(videos):
        with cols[index % 2]:  # Adjust based on the column count
            st.markdown(f"### {video['title']}")
            st.video(video['url'])
            st.caption(video["description"])

# Instagram Feed
def instagram_feed():
    st.header("Instagram Videos")
    st.write("Check out our latest Instagram content directly from [PeachFPV](https://www.instagram.com/peachfpv/)")
    instagram_posts = [
        "https://www.instagram.com/p/DAV1cuSPKSo/embed",
        "https://www.instagram.com/p/CyQWDZTpA7c/embed"
    ]

# Service Packages Section
def service_packages():
    st.header("Our Services")
    st.write("""
    **PeachFPV** offers a range of aerial videography services tailored for extreme sports enthusiasts. 
    We specialize in drifting, watercross, snowmobiling, business applications, and even Real Estate.
    """)

    packages = [
        {
            "name": "Basic Package",
            "price": "Message for pricing",
            "details": [
                "Aerial video of your choosing",
                "1 to 2 hours of fly time",
                "2-3 short-form videos (30 to 60 seconds each)",
                "Raw footage shared via Google Drive"
            ]
        },
        {
            "name": "Pro Package",
            "price": "Message for pricing",
            "details": [
                "All previous tiers",
                "2 to 4 hours of fly time",
                "2-3 additional videos (or longer formatted videos depending on application)",
                "Highlight reel"
            ]
        },
        {
            "name": "Premium Package",
            "price": "Message for pricing",
            "details": [
                "All previous tiers",
                "6+ hours fly time",
                "8-10 short-form videos",
                "Full event coverage",
                "In-depth editing",
                "Personalized video production"
            ]
        }
    ]

    # Display packages with expanders, iterating through details
    for package in packages:
        with st.expander(f"{package['name']} - {package['price']}"):
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
#instagram_feed()
service_packages()
contact_section()
