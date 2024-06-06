from example_project.config import DATA_DIR


if __name__ == "__main__":
    for csv_file in DATA_DIR.glob("*.csv"):
        print(f"Größe von {csv_file.name}:", csv_file.lstat().st_size)
