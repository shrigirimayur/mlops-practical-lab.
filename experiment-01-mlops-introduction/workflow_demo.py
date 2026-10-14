def main():
    stages = [
        "Problem definition",
        "Data collection and validation",
        "Preprocessing and feature engineering",
        "Model training and evaluation",
        "Versioning and deployment",
        "Monitoring and retraining",
    ]
    for index, stage in enumerate(stages, start=1):
        print(f"{index}. {stage}")
    print("Workflow diagram: see README.md")

if __name__ == "__main__":
    main()
