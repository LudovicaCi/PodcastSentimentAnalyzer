import pandas as pd


# Function to load dataset from a JSON file into a DataFrame
def load_dataset():
    # Specify the path to the JSON file
    path = 'resources/reviews.json'

    # Load the JSON file into a DataFrame in chunks of 100,000 lines each
    df_chunks = pd.read_json(path, lines=True, chunksize=100000)

    # Concatenate the DataFrame chunks into a single DataFrame with a continuous index
    df = pd.concat(df_chunks, ignore_index=True)

    # Return the combined DataFrame
    return df


# Main block of code
if __name__ == '__main__':
    # Call the load_dataset function to obtain the DataFrame with reviews data
    reviews = load_dataset()

    # Specify the path for the output CSV file where the DataFrame will be saved
    output_csv_path = 'resources/reviews_podcast.csv'

    # Save the DataFrame to a CSV file, excluding the index column
    reviews.to_csv(output_csv_path, index=False)
