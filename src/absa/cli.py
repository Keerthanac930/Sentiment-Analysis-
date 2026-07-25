import argparse
import csv
from pathlib import Path

from src.absa.analyzer import AspectSentimentAnalyzer


def build_parser():
    parser = argparse.ArgumentParser(description="Aspect-Based Sentiment Analysis")
    parser.add_argument("--text", help="Review text to analyze")
    parser.add_argument("--input", help="CSV file containing a review column")
    parser.add_argument("--output", help="Optional path to save batch predictions")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    analyzer = AspectSentimentAnalyzer()

    if args.text:
        results = analyzer.analyze(args.text)
        if not results:
            print("No configured aspects were detected.")
            return

        for result in results:
            print(f"{result['aspect']}: {result['sentiment']} (score={result['score']})")
        return

    if args.input:
        with open(args.input, newline="", encoding="utf-8") as input_file:
            data = list(csv.DictReader(input_file))

        if data and "review" not in data[0]:
            raise ValueError("Input CSV must contain a review column.")

        results = analyzer.analyze_records(data)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", newline="", encoding="utf-8") as output_file:
                fieldnames = ["row_id", "review", "aspect", "matched_keywords", "sentiment", "score"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)
            print(f"Saved predictions to {output_path}")
        else:
            for result in results:
                print(
                    f"{result['row_id']} | {result['aspect']} | "
                    f"{result['sentiment']} | score={result['score']}"
                )
        return

    parser.print_help()


if __name__ == "__main__":
    main()
