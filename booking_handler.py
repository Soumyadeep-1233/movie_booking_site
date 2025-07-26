import pandas as pd

def load_movies(path="movies.csv"):
    return pd.read_csv(path)

def book_ticket(title, count, path="movies.csv"):
    df = pd.read_csv(path)
    if title in df['title'].values:
        index = df[df['title'] == title].index[0]
        available = df.at[index, 'seats']
        if available >= count:
            df.at[index, 'seats'] -= count
            df.to_csv(path, index=False)
            return True, f"Booked {count} tickets for {title}!"
        else:
            return False, f"Only {available} seats left!"
    return False, "Movie not found!"
