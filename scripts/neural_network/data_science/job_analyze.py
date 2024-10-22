import pandas as pd


def replace_newlines(text: str):
    return text.replace("\n", "<br>")


def make_clickable(val):
    return f'<a href="{val}">{val}</a>'


def highlight_word(description: str, word: str, color_num: int) -> str:

    css_colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "gray",
        "orange",
        "purple",
        "pink",
        "brown",
        "cyan",
        "magenta",
        "lime",
        "navy",
    ]

    color_name = css_colors[color_num]

    return description.replace(
        word, f'<span style="background-color: {color_name};">{word}</span>'
    )


def save_html(df: pd.DataFrame, name: str):
    html_output = df.to_html(escape=False)
    count = df.shape[0]

    filename = f"/home/fly/temp/df_{name}_{count}.html"

    with open(filename, "w") as file:
        file.write(html_output)

    print(f"DataFrame saved: {name}. count: {count}")


def filter_df(df: pd.DataFrame, common_series: pd.Series, key_word: str):
    filter_1 = df["Description"].str.contains(key_word, case=False, na=False)
    filter_2 = df["Title"].str.contains(key_word, case=False, na=False)
    filter = filter_1 | filter_2
    common_series.loc[:] = common_series | filter

    filtered_df = df[filter]

    return filtered_df


def main(filename: str):
    df = pd.read_csv(filename)

    df = df.iloc[:, :6]

    df.loc[:, "Description"] = df["Description"].apply(replace_newlines)
    df.loc[:, "Detail URL"] = df["Detail URL"].apply(make_clickable)

    # C++
    # key_words = [
    #     "c\+\+",
    #     "python",
    #     "embed",
    #     "cloud",
    #     "backend",
    #     "game",
    #     "robotics",
    #     "computer vision",
    #     "frontend",
    #     "front-end",
    #     "engineer",
    #     "automotive",
    # ]

    key_words = [
        "c\+\+",
        "python",
        "embed",
        "cloud",
        "backend",
        "game",
        "robotics",
        "computer vision",
        "frontend",
        "front-end",
        "engineer",
        "automotive",
        "ROS",
    ]

    for color_num, kw in enumerate(key_words):
        kw = kw.replace("\\", "")
        df.loc[:, "Description"] = df["Description"].apply(
            lambda x: highlight_word(x, kw, color_num)
        )
        df.loc[:, "Description"] = df["Description"].apply(
            lambda x: highlight_word(x, kw.capitalize(), color_num)
        )

    save_html(df, "all")

    common_series = pd.Series([False] * len(df["Description"]))

    for kw in key_words:
        filtered_df = filter_df(df, common_series, kw)
        save_html(filtered_df, kw)

    other_df = df[~common_series]
    save_html(other_df, "other")


if __name__ == "__main__":
    filename = "/home/fly/work/job_data/cpp_all_onsite_belgrade_02_10_24.csv"
    main(filename)
