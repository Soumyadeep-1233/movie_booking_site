import streamlit as st
from booking_handler import load_movies, book_ticket
from utils import display_title

st.set_page_config(page_title="Movie Booking", layout="centered")
st.title(display_title())

st.subheader("📅 Available Movies")
movies = load_movies()

for i, row in movies.iterrows():
    st.write(f"**{row['title']}** | ⏰ {row['time']} | 🎟️ {row['seats']} seats left")

st.markdown("---")
st.subheader("🎫 Book Your Ticket")

movie_list = movies['title'].tolist()
selected = st.selectbox("Choose a movie:", movie_list)
count = st.number_input("How many tickets?", 1, 10, step=1)

if st.button("Book Now"):
    success, msg = book_ticket(selected, count)
    if success:
        st.success(msg)
    else:
        st.error(msg)
