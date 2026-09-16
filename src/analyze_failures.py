import os
import pandas as pd


RETRIEVAL_FILE = "results/retrieval_baseline.csv"
GENERATION_FILE = "results/generation_baseline.csv"

OUTPUT_FILE = "results/failure_analysis.csv"
SUMMARY_FILE = "results/summary/failure_analysis_summary.csv"


def classify_failure(row):
    retrieval_success = row["complete_evidence"] == 1
    generation_success = row["exact_match"] == 1

    if retrieval_success and generation_success:
        return "Retrieval Success + Generation Success"

    if retrieval_success and not generation_success:
        return "Retrieval Success + Generation Failure"

    if not retrieval_success and generation_success:
        return "Retrieval Failure + Generation Success"

    return "Retrieval Failure + Generation Failure"


def main():
    print("Loading retrieval results...")

    retrieval = pd.read_csv(RETRIEVAL_FILE)

    print(f"Retrieval rows: {len(retrieval)}")

    print("Loading generation results...")

    generation = pd.read_csv(GENERATION_FILE)

    print(f"Generation rows: {len(generation)}")

    generation = generation[
        generation["k"] != 0
    ]

    merged = pd.merge(
        retrieval,
        generation[
            [
                "question_id",
                "k",
                "gold_answer",
                "generated_answer",
                "exact_match",
                "f1"
            ]
        ],
        on=["question_id", "k"],
        how="inner"
    )

    print()
    print(f"Merged rows: {len(merged)}")

    merged["failure_category"] = (
        merged.apply(
            classify_failure,
            axis=1
        )
    )

    os.makedirs("results", exist_ok=True)

    merged.to_csv(
        OUTPUT_FILE,
        index=False
    )

    summary = (
        merged
        .groupby(
            [
                "k",
                "failure_category"
            ]
        )
        .size()
        .reset_index(name="count")
    )

    totals = (
        summary
        .groupby("k")["count"]
        .transform("sum")
    )

    summary["percentage"] = (
        summary["count"] /
        totals *
        100
    )

    os.makedirs(
        "results/summary",
        exist_ok=True
    )

    summary.to_csv(
        SUMMARY_FILE,
        index=False
    )

    print()
    print("==============================")
    print(" Failure Decomposition")
    print("==============================")
    print()

    for k in sorted(merged["k"].unique()):
        subset = merged[
            merged["k"] == k
        ]

        print(f"k = {k}")

        counts = (
            subset[
                "failure_category"
            ]
            .value_counts()
        )

        categories = [
            "Retrieval Success + Generation Success",
            "Retrieval Success + Generation Failure",
            "Retrieval Failure + Generation Success",
            "Retrieval Failure + Generation Failure"
        ]

        for category in categories:
            count = counts.get(category, 0)

            percentage = (
                count /
                len(subset) *
                100
            )

            print(
                f"  {category}: "
                f"{count} "
                f"({percentage:.1f}%)"
            )

        print()

    print(
        f"Detailed results saved to: "
        f"{OUTPUT_FILE}"
    )

    print(
        f"Summary saved to: "
        f"{SUMMARY_FILE}"
    )


if __name__ == "__main__":
    main()
