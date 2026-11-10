"""Reusable plotting helpers for Lab 7."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def summarize_by_year(df, date_column="talk_date", value_column="word_count"):
    """Return yearly median and count for a numeric talk-level variable."""
    required = {date_column, value_column}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    data = df[[date_column, value_column]].copy()
    data[date_column] = pd.to_datetime(data[date_column], errors="coerce")
    data[value_column] = pd.to_numeric(data[value_column], errors="coerce")
    data = data.dropna(subset=[date_column, value_column])
    data["year"] = data[date_column].dt.year
    return data.groupby("year", as_index=False).agg(
        median_value=(value_column, "median"),
        observation_count=(value_column, "size"),
    )


def save_yearly_median_plot(summary, output_path="figures/yearly_median.png",
                            value_label="Median words per talk"):
    """Save a labeled line plot from a yearly summary table."""
    required = {"year", "median_value"}
    missing = required.difference(summary.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(data=summary, x="year", y="median_value", marker="o", ax=ax)
    ax.set(title=f"{value_label} by conference year",
           xlabel="Conference year", ylabel=value_label)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output
