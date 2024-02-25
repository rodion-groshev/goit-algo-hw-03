import argparse
import shutil
from pathlib import Path


def copy_files(src: Path, dst: Path):
    if not dst.exists():
        dst.mkdir(parents=True, exist_ok=True)
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst.joinpath(item.name))
            else:
                extension = item.suffix.lstrip('.')
                new_dir = dst.joinpath(extension)
                new_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy(item, new_dir.joinpath(item.name))
    except Exception as err:
        print(f"Unexpected {err}")


def parse_argv():
    parser = argparse.ArgumentParser("Сортування директорії")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Вхідна папка"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("output"),
        help="Вихідна папка",
    )
    return parser.parse_args()


def main():
    args = parse_argv()
    print(f"Вхідні аргументи: {args}")
    copy_files(args.source, args.output)


if __name__ == "__main__":
    main()
