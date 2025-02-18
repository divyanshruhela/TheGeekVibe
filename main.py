import streamlit as st
import requests
from bs4 import BeautifulSoup

# Sample news data (Replace with actual news fetching logic)
# You'll likely want to use an API or web scraping to get real news
sample_news = [
    {"title": "AI Breakthrough Revolutionizes Healthcare", "category": "Trending", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "New Smartphone Unveiled with Groundbreaking Camera", "category": "Big Stories", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "Global Chip Shortage Eases", "category": "World", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "Indian Tech Startup Secures Major Funding", "category": "India", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "Scientists Discover New Exoplanet", "category": "Science", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "The Future of Quantum Computing", "category": "Innovation", "image": "https://via.placeholder.com/150", "link": "#"},
     {"title": "Metaverse Expands with New Virtual Worlds", "category": "Trending", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "Electric Vehicle Sales Surge Globally", "category": "Big Stories", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "Cybersecurity Threats on the Rise", "category": "World", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "India's Digital Economy Booms", "category": "India", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "Breakthrough in Renewable Energy Research", "category": "Science", "image": "https://via.placeholder.com/150", "link": "#"},
    {"title": "The Impact of Artificial Intelligence on Society", "category": "Innovation", "image": "https://via.placeholder.com/150", "link": "#"},
]

# Function to fetch news (Replace with your actual logic)
def fetch_news(category=None):
    if category:
        return [news for news in sample_news if news["category"] == category]
    return sample_news

# Sidebar
st.sidebar.title("Tech News Categories")
categories = ["All", "Trending", "Big Stories", "World", "India", "Innovation", "Science"]
category_tabs = {}  # Dictionary to store tab states

for category in categories:
    if category not in category_tabs:
        category_tabs[category] = False  # Initialize all tabs to False (unselected)

    if st.sidebar.button(category):  # Use buttons for tabs
        # Reset all other tabs
        for cat in category_tabs:
            category_tabs[cat] = False
        category_tabs[category] = True  # Select the clicked tab

selected_category = None  # To store the selected category

for category, is_selected in category_tabs.items():  # Find the selected category
    if is_selected:
        selected_category = category
        break

# Main content
st.title("The Geek Vibe")

if selected_category:  # Only fetch and display if a category is selected
    news_to_display = fetch_news(selected_category if selected_category != "All" else None)

    for news in news_to_display:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(news["image"], width=150)
        with col2:
            st.subheader(news["title"])
            st.markdown(f"[Read More]({news['link']})")
            st.markdown("---")
else:
    st.write("Select a category from the sidebar to view news.") # Message when no category is selected

# Web scraping example (Adapt to your target website)
def scrape_news(url):
    # ... (same scraping function as before)
    return []

# Example usage (uncomment and adapt):
# ... (same as before)