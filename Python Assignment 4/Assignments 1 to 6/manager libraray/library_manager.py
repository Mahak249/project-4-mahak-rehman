import streamlit as st
import pandas as pd

# Initialize session state for storing books
if 'books' not in st.session_state:
    st.session_state.books = []

# Title
st.title("Library Manager")

# Tabs for different sections
tabs = st.tabs(["Add Book", "View Books", "Search Book", "Delete Book"])

# --- Add Book ---
with tabs[0]:
    st.header("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=0, max_value=2100, step=1)

    if st.button("Add Book"):
        if title and author:
            st.session_state.books.append({
                "Title": title,
                "Author": author,
                "Year": int(year)
            })
            st.success(f"Book '{title}' added!")
        else:
            st.warning("Please fill in all fields.")

# --- View Books ---
with tabs[1]:
    st.header("All Books")
    if st.session_state.books:
        df = pd.DataFrame(st.session_state.books)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No books available.")

# --- Search Book ---
with tabs[2]:
    st.header("Search Book by Title")
    search_title = st.text_input("Enter title to search")
    if search_title:
        results = [book for book in st.session_state.books if search_title.lower() in book['Title'].lower()]
        if results:
            st.write("Search Results:")
            st.dataframe(pd.DataFrame(results), use_container_width=True)
        else:
            st.warning("No matching book found.")

# --- Delete Book ---
with tabs[3]:
    st.header("Delete a Book")
    if st.session_state.books:
        book_titles = [book['Title'] for book in st.session_state.books]
        book_to_delete = st.selectbox("Select book to delete", book_titles)
        if st.button("Delete Book"):
            st.session_state.books = [book for book in st.session_state.books if book['Title'] != book_to_delete]
            st.success(f"Deleted '{book_to_delete}'")
    else:
        st.info("No books to delete.")
