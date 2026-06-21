import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def copy_file(src_path: Path, dist_dir: Path):
    ext = src_path.suffix.lower().replace(".", "")
    target_dir = dist_dir / ext
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, target_dir / src_path.name)


def process_directory(src_dir: Path, dist_dir: Path, executor: ThreadPoolExecutor):
    for item in src_dir.iterdir():
        if item.is_dir():
            executor.submit(process_directory, item, dist_dir, executor)
        else:
            executor.submit(copy_file, item, dist_dir)


def sort_files(src: str, dist: str = "dist"):
    src_dir = Path(src)
    dist_dir = Path(dist)
    dist_dir.mkdir(parents=True, exist_ok=True)

    files = [f for f in src_dir.rglob("*") if f.is_file()]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda f: copy_file(f, dist_dir), files)
