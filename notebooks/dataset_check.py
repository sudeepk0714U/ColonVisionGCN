from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from utils.config import DATASET_DIR, CLASSES


VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp"
}


def main():

    print("=" * 60)
    print("COLON DISEASE DATASET CHECK")
    print("=" * 60)

    total_images = 0

    for class_name in CLASSES:

        class_dir = DATASET_DIR / class_name

        if not class_dir.exists():

            print(
                f"\nWARNING: Missing directory: {class_dir}"
            )

            continue

        images = [
            file
            for file in class_dir.iterdir()
            if file.is_file()
            and file.suffix.lower() in VALID_EXTENSIONS
        ]

        count = len(images)

        total_images += count

        print(
            f"{class_name:30s}: {count:5d}"
        )

    print("-" * 60)

    print(
        f"Total images: {total_images}"
    )

    print(
        f"Number of classes: {len(CLASSES)}"
    )


if __name__ == "__main__":
    main()