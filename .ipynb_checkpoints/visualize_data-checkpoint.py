from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PROJECT_DIR = Path(__file__).parent
DATA_FILE = PROJECT_DIR / "scraped_quotes.csv"
OUTPUT_FILE = PROJECT_DIR / "data_visualization_dashboard.png"


def load_quotes(data_file=DATA_FILE):
    data = pd.read_csv(data_file)
    required_columns = {"quote", "author"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")
    if data.empty:
        raise ValueError("Dataset has no rows to visualize.")

    for column in required_columns:
        data[column] = data[column].astype("string").str.strip()
        data[column] = data[column].replace("", pd.NA)
    data = data.dropna(subset=["quote", "author"])
    data = data.drop_duplicates(subset=["quote", "author"]).copy()
    if data.empty:
        raise ValueError("No complete quote records remain for visualization.")

    data["character_count"] = data["quote"].str.len()
    return data


def make_dashboard(data, output_file=OUTPUT_FILE):
    author_counts = data["author"].value_counts().head(10)
    sns.set_theme(style="whitegrid")
    figure, axes = plt.subplots(1, 2, figsize=(14, 6))

    colors = sns.color_palette("crest", n_colors=len(author_counts))
    bars = axes[0].bar(author_counts.index, author_counts.values, color=colors)
    axes[0].bar_label(bars, padding=3)
    axes[0].set_title("Authors with the Most Quotes")
    axes[0].set_xlabel("Author")
    axes[0].set_ylabel("Quotes in sample")
    axes[0].tick_params(axis="x", rotation=35)

    sns.histplot(
        data=data,
        x="character_count",
        bins="auto",
        kde=False,
        color="#6a51a3",
        ax=axes[1],
    )
    axes[1].set_title("Quote Lengths in the Sample")
    axes[1].set_xlabel("Characters per quote")
    axes[1].set_ylabel("Number of quotes")

    figure.suptitle("A Snapshot of Quotes to Scrape", fontsize=16)
    figure.tight_layout()
    figure.savefig(output_file, dpi=250, bbox_inches="tight")
    plt.close(figure)


def main():
    data = load_quotes()
    make_dashboard(data)
    print(f"Dashboard saved to {OUTPUT_FILE}")
    print(f"Visualized {len(data)} complete, unique quote records.")
    print("The charts describe this scraped sample; author counts are not popularity measures.")


if __name__ == "__main__":
    main()
