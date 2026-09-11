from datasets import load_dataset
import json
import os
import random


SEED = 42
SAMPLE_SIZE = 100


def main():
    print("Loading HotpotQA dataset...")

    dataset = load_dataset(
        "hotpotqa/hotpot_qa",
        "distractor",
        split="validation"
    )

    print(f"Validation examples: {len(dataset)}")

    random.seed(SEED)

    indices = random.sample(
        range(len(dataset)),
        SAMPLE_SIZE
    )

    subset = dataset.select(indices)

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    output_path = (
        "data/processed/"
        "hotpotqa_validation_100.json"
    )

    records = []

    for example in subset:

        record = {
            "id": example["id"],
            "question": example["question"],
            "answer": example["answer"],
            "type": example["type"],
            "level": example["level"],
            "supporting_facts": example[
                "supporting_facts"
            ],
            "context": example["context"]
        }

        records.append(record)

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            indent=2,
            ensure_ascii=False
        )

    print()
    print(
        f"Saved {len(records)} examples "
        f"to {output_path}"
    )

    print()
    print("First example:")
    print()
    print("Question:")
    print(records[0]["question"])
    print()
    print("Answer:")
    print(records[0]["answer"])
    print()
    print("Supporting facts:")
    print(records[0]["supporting_facts"])


if __name__ == "__main__":
    main()
