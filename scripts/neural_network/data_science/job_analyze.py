import pandas as pd


# Функция для замены \n\n на <br>
def replace_newlines(text):
    return text.replace('\n', '<br>')

def make_clickable(val):
    return f'<a href="{val}">{val}</a>'

def save_html(df : pd.DataFrame):
    # Save the DataFrame as an HTML file
    html_output = df.to_html(escape=False)

    # Применение функции ко всем строкам в DataFrame
    df['Description'] = df['Description'].apply(replace_newlines)
    df['Detail URL'] = df['Detail URL'].apply(make_clickable)

    # Write the HTML to a file
    with open('/home/fly/temp/dataframe.html', 'w') as file:
        file.write(html_output)

    print("DataFrame saved as HTML page successfully.")

def filter_df(df: pd.DataFrame, key_word: str):
    filtered_df = df[df['Description'].str.contains(key_word, case=False, na=False)]
    return filtered_df

def main():
    df = pd.read_csv('/home/fly/work/job_data/cpp_all_onsite_belgrade_06_08_24.csv')
    save_html(df)
    key_words = ["web", "c\+\+", "python", "robotics", "embed"]
    filtered_df = filter_df(df, "web")
    save_html(filtered_df)

if __name__ == "__main__":
    main()

