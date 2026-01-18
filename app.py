import streamlit as st

st.set_page_config(page_title="Chill With Cine", page_icon="🎬")

st.markdown(
    """
    <style>
    body {
        background-color: #0b0c10;
        color: #c5c6c7;
        font-family: 'Arial', sans-serif;
    }
    h2, h3 {
        color: #66fcf1;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown(
    "<p style='text-align: center; color: grey;'>Find movies that match your vibe ✨</p>",
    unsafe_allow_html=True
)

st.divider()

# --- Movie Data  ---
movies = {
    "English": {
        "Happy": {
            "Comedy": ["The Grand Budapest Hotel", "Paddington 2", "Crazy Rich Asians", "Sing", "School of Rock"],
            "Adventure": ["Guardians of the Galaxy", "Jumanji: Welcome to the Jungle", "Pirates of the Caribbean"]
        },
        "Sad": {
            "Drama": ["The Pursuit of Happyness", "Inside Out", "A Star is Born"],
            "Romance": ["La La Land", "The Notebook", "Titanic"]
        },
        "Action": {
            "Superhero": ["Avengers: Endgame", "Black Panther", "Spider-Man: No Way Home"],
            "Thriller": ["John Wick", "Mad Max: Fury Road", "Inception"]
        },
        "Chill": {
            "Fantasy": ["Harry Potter Series", "Stardust", "The Hobbit"],
            "Animation": ["Coco", "Up", "Moana"]
        }
    },
    "Hindi": {
        "Happy": {
            "Comedy": ["3 Idiots", "Chhichhore", "Munna Bhai MBBS"],
            "Adventure": ["Krrish", "Ra.One", "Baahubali 1"]
        },
        "Sad": {
            "Drama": ["Taare Zameen Par", "Kapoor & Sons"],
            "Romance": ["Kabhi Khushi Kabhie Gham", "Veer-Zaara"]
        },
        "Action": {
            "Superhero": ["Krrish 3", "Shaktimaan"],
            "Thriller": ["Dhoom 2", "War"]
        },
        "Chill": {
            "Fantasy": ["Baahubali 2", "Ra.One"],
            "Animation": ["Hanuman", "Roadside Romeo"]
        }
    },
    "Tamil": {
        "Happy": {"Comedy": ["Boss Engira Bhaskaran", "Soodhu Kavvum"], "Adventure": ["Enthiran", "Mersal"]},
        "Sad": {"Drama": ["Aruvi", "Vinnaithaandi Varuvaayaa"], "Romance": ["96", "OK Kanmani"]},
        "Action": {"Superhero": ["Maanagaram", "Vikram"], "Thriller": ["Kaithi", "Vikram Vedha"]},
        "Chill": {"Fantasy": ["Sivaji", "Raam"], "Animation": ["Kochadaiiyaan"]}
    },
    "Telugu": {
        "Happy": {"Comedy": ["F2", "Venky"], "Adventure": ["Magadheera", "Eega"]},
        "Sad": {"Drama": ["Mahanati", "Sammohanam"], "Romance": ["Geetha Govindam", "Ye Maaya Chesave"]},
        "Action": {"Superhero": ["RRR", "Sye"], "Thriller": ["Evaru", "Kshanam"]},
        "Chill": {"Fantasy": ["Baahubali 1", "Baahubali 2"], "Animation": ["Anaganaga O Dheerudu"]}
    },
    "Malayalam": {
        "Happy": {"Comedy": ["Kalyanaraman", "Godha"], "Adventure": ["Manichitrathazhu", "Pulimurugan"]},
        "Sad": {"Drama": ["Bangalore Days", "Charlie"], "Romance": ["Premam", "Ennu Ninte Moideen"]},
        "Action": {"Superhero": ["Minnal Murali"], "Thriller": ["Drishyam", "Mumbai Police"]},
        "Chill": {"Fantasy": ["Odiyan", "Lucifer"], "Animation": ["Punyalan Agarbattis"]}
    },
    "Japanese": {
        "Happy": {"Comedy": ["Our Little Sister", "Swing Girls"], "Adventure": ["Spirited Away", "Howl's Moving Castle"]},
        "Sad": {"Drama": ["Departures", "A Silent Voice"], "Romance": ["Your Name", "5 Centimeters per Second"]},
        "Action": {"Superhero": ["My Hero Academia Movie"], "Thriller": ["Battle Royale"]},
        "Chill": {"Fantasy": ["Princess Mononoke"], "Animation": ["My Neighbor Totoro"]}
    },
    "Korean": {
        "Happy": {"Comedy": ["Extreme Job", "Miss Granny"], "Adventure": ["Along with the Gods"]},
        "Sad": {"Drama": ["A Moment to Remember", "Secret Sunshine"], "Romance": ["The Classic", "Always"]},
        "Action": {"Superhero": ["Fabricated City"], "Thriller": ["Oldboy"]},
        "Chill": {"Fantasy": ["The Good, The Bad, The Weird"], "Animation": ["Leafie, A Hen into the Wild"]}
    }
}

posters = {
    # English
    "The Grand Budapest Hotel": "https://upload.wikimedia.org/wikipedia/en/1/1b/Grand_Budapest_Hotel_Poster.jpg",
    "Paddington 2": "https://m.media-amazon.com/images/I/81f0Z5fLZ0L._AC_SY679_.jpg",
    "Crazy Rich Asians": "https://m.media-amazon.com/images/I/91z+R5ThP2L._AC_SY679_.jpg",
    "Sing": "https://m.media-amazon.com/images/I/81pYkK5e4DL._AC_SY679_.jpg",
    "School of Rock": "https://m.media-amazon.com/images/I/71t5P8z8SbL._AC_SY679_.jpg",
    "Guardians of the Galaxy": "https://m.media-amazon.com/images/I/81uYVEzL+ML._AC_SY679_.jpg",
    "Jumanji: Welcome to the Jungle": "https://m.media-amazon.com/images/I/91oD3CzItAL._AC_SY679_.jpg",
    "Pirates of the Caribbean": "https://m.media-amazon.com/images/I/81m5cg+5Z7L._AC_SY679_.jpg",
    "The Pursuit of Happyness": "https://m.media-amazon.com/images/I/71Ff9o11ffL._AC_SY679_.jpg",
    "Inside Out": "https://m.media-amazon.com/images/I/71sG4I9WvPL._AC_SY679_.jpg",
    "A Star is Born": "https://m.media-amazon.com/images/I/81T1S4nJ6sL._AC_SY679_.jpg",
    "La La Land": "https://m.media-amazon.com/images/I/81Zck3lhl-L._AC_SY679_.jpg",
    "The Notebook": "https://m.media-amazon.com/images/I/71l61yV1KCL._AC_SY679_.jpg",
    "Titanic": "https://m.media-amazon.com/images/I/71S8uKTR+pL._AC_SY679_.jpg",
    "Avengers: Endgame": "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg",
    "Black Panther": "https://m.media-amazon.com/images/I/81xXAy5CbhL._AC_SY679_.jpg",
    "Spider-Man: No Way Home": "https://m.media-amazon.com/images/I/91V+ZlW1VxL._AC_SY679_.jpg",
    "John Wick": "https://m.media-amazon.com/images/I/81lHZzJ3J0L._AC_SY679_.jpg",
    "Mad Max: Fury Road": "https://m.media-amazon.com/images/I/81pQw34yIDL._AC_SY679_.jpg",
    "Inception": "https://m.media-amazon.com/images/I/91S1H5GFkXL._AC_SY679_.jpg",
    "Harry Potter Series": "https://m.media-amazon.com/images/I/91hhP2O+SML._AC_SY679_.jpg",
    "Stardust": "https://m.media-amazon.com/images/I/71h4BEnzZWL._AC_SY679_.jpg",
    "The Hobbit": "https://m.media-amazon.com/images/I/91fdPY2eGUL._AC_SY679_.jpg",
    "Coco": "https://m.media-amazon.com/images/I/81ZsWwA+ixL._AC_SY679_.jpg",
    "Up": "https://m.media-amazon.com/images/I/81tXTSIRuqL._AC_SY679_.jpg",
    "Moana": "https://m.media-amazon.com/images/I/71fXbEvmVGL._AC_SY679_.jpg",

    # Hindi
    "3 Idiots": "https://m.media-amazon.com/images/I/71dY6qz5OQL._AC_SY679_.jpg",
    "Chhichhore": "https://m.media-amazon.com/images/I/81r1o5bZ0VL._AC_SY679_.jpg",
    "Munna Bhai MBBS": "https://m.media-amazon.com/images/I/71psXKkuZ+L._AC_SY679_.jpg",
    "Krrish": "https://m.media-amazon.com/images/I/81PovGElPBL._AC_SY679_.jpg",
    "Ra.One": "https://m.media-amazon.com/images/I/91WlFOUJuML._AC_SY679_.jpg",
    "Baahubali 1": "https://m.media-amazon.com/images/I/81zJDv7JezL._AC_SY679_.jpg",
    "Taare Zameen Par": "https://m.media-amazon.com/images/I/81DGZ2x6igL._AC_SY679_.jpg",
    "Kapoor & Sons": "https://m.media-amazon.com/images/I/81f5bR7TfLL._AC_SY679_.jpg",
    "Kabhi Khushi Kabhie Gham": "https://m.media-amazon.com/images/I/71wWq+n2B+L._AC_SY679_.jpg",
    "Veer-Zaara": "https://m.media-amazon.com/images/I/81zIaCzFQDL._AC_SY679_.jpg",
    "Krrish 3": "https://m.media-amazon.com/images/I/81rYwLk9R-L._AC_SY679_.jpg",
    "Shaktimaan": "https://m.media-amazon.com/images/I/81R9IlPKZ-L._AC_SY679_.jpg",
    "Dhoom 2": "https://m.media-amazon.com/images/I/81RGW+0WrTL._AC_SY679_.jpg",
    "War": "https://m.media-amazon.com/images/I/81Tpm0A+88L._AC_SY679_.jpg",
    "Baahubali 2": "https://m.media-amazon.com/images/I/81s1xkVULKL._AC_SY679_.jpg",
    "Hanuman": "https://m.media-amazon.com/images/I/81P8z2oQmQL._AC_SY679_.jpg",
    "Roadside Romeo": "https://m.media-amazon.com/images/I/81nU+O0lfXL._AC_SY679_.jpg",

    # Tamil
    "Boss Engira Bhaskaran": "https://m.media-amazon.com/images/I/81iJ8pUMWkL._AC_SY679_.jpg",
    "Soodhu Kavvum": "https://m.media-amazon.com/images/I/81rM7W0MCGL._AC_SY679_.jpg",
    "Enthiran": "https://m.media-amazon.com/images/I/81Gg5jGgVCL._AC_SY679_.jpg",
    "Mersal": "https://m.media-amazon.com/images/I/91SxS9v+19L._AC_SY679_.jpg",
    "Aruvi": "https://m.media-amazon.com/images/I/81h0jB7+ojL._AC_SY679_.jpg",
    "Vinnaithaandi Varuvaayaa": "https://m.media-amazon.com/images/I/71z3f+5Z2WL._AC_SY679_.jpg",
    "96": "https://m.media-amazon.com/images/I/81q6OT8LoIL._AC_SY679_.jpg",
    "OK Kanmani": "https://m.media-amazon.com/images/I/71mXKZBf9PL._AC_SY679_.jpg",
    "Maanagaram": "https://m.media-amazon.com/images/I/81pO2wJ93XL._AC_SY679_.jpg",
    "Vikram": "https://m.media-amazon.com/images/I/81iPk4u1fLL._AC_SY679_.jpg",
    "Kaithi": "https://m.media-amazon.com/images/I/81xCN+Yp6PL._AC_SY679_.jpg",
    "Vikram Vedha": "https://m.media-amazon.com/images/I/81O5Q+czGNL._AC_SY679_.jpg",
    "Sivaji": "https://m.media-amazon.com/images/I/81bROt7hK2L._AC_SY679_.jpg",
    "Raam": "https://m.media-amazon.com/images/I/71xKJrPKlZL._AC_SY679_.jpg",
    "Kochadaiiyaan": "https://m.media-amazon.com/images/I/71Rygp7v0BL._AC_SY679_.jpg",

    # Telugu
    "F2": "https://m.media-amazon.com/images/I/81ayVbM4QbL._AC_SY679_.jpg",
    "Venky": "https://m.media-amazon.com/images/I/81zFjT0OQHL._AC_SY679_.jpg",
    "Magadheera": "https://m.media-amazon.com/images/I/81pXs2u7X-L._AC_SY679_.jpg",
    "Eega": "https://m.media-amazon.com/images/I/81hrnsoX9nL._AC_SY679_.jpg",
    "Mahanati": "https://m.media-amazon.com/images/I/81sZrhN5vWL._AC_SY679_.jpg",
    "Sammohanam": "https://m.media-amazon.com/images/I/81r1aSjU4AL._AC_SY679_.jpg",
    "Geetha Govindam": "https://m.media-amazon.com/images/I/81v+5T3JgPL._AC_SY679_.jpg",
    "Ye Maaya Chesave": "https://m.media-amazon.com/images/I/81wMf1XK3EL._AC_SY679_.jpg",
    "RRR": "https://m.media-amazon.com/images/I/81eHzX6p4VL._AC_SY679_.jpg",
    "Sye": "https://m.media-amazon.com/images/I/71H7FXIMdFL._AC_SY679_.jpg",
    "Evaru": "https://m.media-amazon.com/images/I/81jZVFxGB-L._AC_SY679_.jpg",
    "Kshanam": "https://m.media-amazon.com/images/I/81FqOwS4kjL._AC_SY679_.jpg",
    "Baahubali 1": "https://m.media-amazon.com/images/I/81zJDv7JezL._AC_SY679_.jpg",
    "Baahubali 2": "https://m.media-amazon.com/images/I/81s1xkVULKL._AC_SY679_.jpg",
    "Anaganaga O Dheerudu": "https://m.media-amazon.com/images/I/81x5p6kYkWL._AC_SY679_.jpg",

    # Malayalam
    "Kalyanaraman": "https://m.media-amazon.com/images/I/81T0hOoy+KL._AC_SY679_.jpg",
    "Godha": "https://m.media-amazon.com/images/I/81BhaFrgqKL._AC_SY679_.jpg",
    "Manichitrathazhu": "https://m.media-amazon.com/images/I/81hN09fIYlL._AC_SY679_.jpg",
    "Pulimurugan": "https://m.media-amazon.com/images/I/81z9Pj3LthL._AC_SY679_.jpg",
    "Bangalore Days": "https://m.media-amazon.com/images/I/81+NkqRZC2L._AC_SY679_.jpg",
    "Charlie": "https://m.media-amazon.com/images/I/81kkOHZc+VL._AC_SY679_.jpg",
    "Premam": "https://m.media-amazon.com/images/I/81mQHvlbJPL._AC_SY679_.jpg",
    "Ennu Ninte Moideen": "https://m.media-amazon.com/images/I/81TvCk1F+LL._AC_SY679_.jpg",
    "Minnal Murali": "https://m.media-amazon.com/images/I/81qijhyvQ7L._AC_SY679_.jpg",
    "Drishyam": "https://m.media-amazon.com/images/I/81yD1ipbCWL._AC_SY679_.jpg",
    "Mumbai Police": "https://m.media-amazon.com/images/I/81NlQYrA4JL._AC_SY679_.jpg",
    "Odiyan": "https://m.media-amazon.com/images/I/81GMe2F2JXL._AC_SY679_.jpg",
    "Lucifer": "https://m.media-amazon.com/images/I/81cJ5tR+xlL._AC_SY679_.jpg",
    "Punyalan Agarbattis": "https://m.media-amazon.com/images/I/81n0/UKBVL._AC_SY679_.jpg",

    # Japanese
    "Our Little Sister": "https://m.media-amazon.com/images/I/71oK+qDBBKL._AC_SY679_.jpg",
    "Swing Girls": "https://m.media-amazon.com/images/I/81h6dpCtDVL._AC_SY679_.jpg",
    "Spirited Away": "https://m.media-amazon.com/images/I/81k9oYw+7PL._AC_SY679_.jpg",
    "Howl's Moving Castle": "https://m.media-amazon.com/images/I/81nltg+p64L._AC_SY679_.jpg",
    "Departures": "https://m.media-amazon.com/images/I/71D+fJ9uFGL._AC_SY679_.jpg",
    "A Silent Voice": "https://m.media-amazon.com/images/I/71cPSTvwOFL._AC_SY679_.jpg",
    "Your Name": "https://m.media-amazon.com/images/I/71z7FjZJYRL._AC_SY679_.jpg",
    "5 Centimeters per Second": "https://m.media-amazon.com/images/I/71yRZ0xxAzL._AC_SY679_.jpg",
    "My Hero Academia Movie": "https://m.media-amazon.com/images/I/71lQTw1xAfL._AC_SY679_.jpg",
    "Battle Royale": "https://m.media-amazon.com/images/I/81A+nSVRz6L._AC_SY679_.jpg",
    "Princess Mononoke": "https://m.media-amazon.com/images/I/81s7HeCVQpL._AC_SY679_.jpg",
    "My Neighbor Totoro": "https://m.media-amazon.com/images/I/81Rk4gVChAL._AC_SY679_.jpg",

    # Korean
    "Extreme Job": "https://m.media-amazon.com/images/I/81sMQnYgQJL._AC_SY679_.jpg",
    "Miss Granny": "https://m.media-amazon.com/images/I/81W2mA0RojL._AC_SY679_.jpg",
    "Along with the Gods": "https://m.media-amazon.com/images/I/81iOH4Fo1kL._AC_SY679_.jpg",
    "A Moment to Remember": "https://m.media-amazon.com/images/I/81cF0bMeiHL._AC_SY679_.jpg",
    "Secret Sunshine": "https://m.media-amazon.com/images/I/71xFSlcRXKL._AC_SY679_.jpg",
    "The Classic": "https://m.media-amazon.com/images/I/71vCJ6j0xML._AC_SY679_.jpg",
    "Always": "https://m.media-amazon.com/images/I/71nFbFg9U-L._AC_SY679_.jpg",
    "Fabricated City": "https://m.media-amazon.com/images/I/81g+7jR6R1L._AC_SY679_.jpg",
    "Oldboy": "https://m.media-amazon.com/images/I/71+7bI3z1BL._AC_SY679_.jpg",
    "The Good, The Bad, The Weird": "https://m.media-amazon.com/images/I/81lK7ceKMJL._AC_SY679_.jpg",
    "Leafie, A Hen into the Wild": "https://m.media-amazon.com/images/I/81dQH8tAQ4L._AC_SY679_.jpg"
}



# --- UI ---
col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(
        "🎥 Choose a language",
        list(movies.keys())
    )

with col2:
    mood = st.radio(
        "🌈 Choose your mood",
        ["Happy", "Sad", "Action", "Chill"]
    )


if st.button("🎬 Recommend Movies"):
    if mood in movies[language]:
        st.subheader(f"🍿 {mood} {language} Movies")

        for genre, movie_list in movies[language][mood].items():
            st.markdown(f"## 🎞️ {genre}")

            # 3 columns for posters
            cols = st.columns(3)

            for i, movie in enumerate(movie_list):
                with cols[i % 3]:
                    # Get poster URL from dictionary
                    poster_url = posters.get(movie)
                    if poster_url:
                        st.image(poster_url, use_container_width=True)

                    # Movie title card
                    st.markdown(
                        f"""
                        <div style="
                            background-color:#1f2833;
                            padding:12px;
                            border-radius:15px;
                            margin-top:10px;
                            margin-bottom:10px;
                            text-align:center;
                            color:#ffffff;
                            box-shadow: 0 0 20px rgba(102,252,241,0.5);
                            transition: transform 0.2s;
                        " 
                        onmouseover="this.style.transform='scale(1.05)';" 
                        onmouseout="this.style.transform='scale(1)';">
                            🎬 <b>{movie}</b>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    else:
        st.warning("No movies found for this mood 😅")

