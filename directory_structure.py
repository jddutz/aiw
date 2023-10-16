import os
import fnmatch


def load_gitignore_patterns(gitignore_path=".gitignore"):
    """
    Loads the patterns specified in a .gitignore file.

    Args:
    - gitignore_path (str): The path to the .gitignore file. Defaults to ".gitignore" in the current directory.

    Returns:
    - list: A list of patterns specified in the .gitignore file.
    """
    patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(line)
    return patterns


def write_files_to_txt(start_directory=".", output_file="directory_structure.txt"):
    """
    Writes the list of all files in each subdirectory of the specified start directory to a text file,
    respecting .gitignore rules.

    Args:
    - start_directory (str): The directory from which to start the search. Defaults to the current working directory.
    - output_file (str): The file to which the directory structure will be written. Defaults to "directory_structure.txt".
    """
    gitignore_patterns = load_gitignore_patterns()

    with open(output_file, "w") as file:
        for dirpath, dirnames, filenames in os.walk(start_directory):
            # Ignore directories starting with a period
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]

            # Filter directories and filenames based on .gitignore patterns
            dirnames[:] = [
                d
                for d in dirnames
                if not any(
                    fnmatch.fnmatch(d, pattern) for pattern in gitignore_patterns
                )
            ]
            filenames = [
                f
                for f in filenames
                if not any(
                    fnmatch.fnmatch(f, pattern) for pattern in gitignore_patterns
                )
            ]

            if filenames:
                file.write(f"\nIn directory: {dirpath}\n")
                for filename in filenames:
                    file.write(f"{filename}\n")


if __name__ == "__main__":
    write_files_to_txt()
