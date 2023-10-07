#!/usr/bin/env python3
import argparse
import os
import re
from typing import List, Tuple


def convert_and_validate_gitmodules_file(gitmodules_path: str = ".gitmodules") -> List[Tuple[str, str, str, str, str]]:
    if not os.path.exists(gitmodules_path):
        raise FileNotFoundError(
            f"Gitmodules file '{gitmodules_path}' not found.")

    with open(gitmodules_path, "r") as file:
        gitmodules_content = file.read()

    submodule_pattern = (
        r'\n\s*\[submodule\s+"([^"]+)"\]\n\s+path\s+=\s+([^ ]+)\n\s+url\s+=\s+([^ ]+)\n\s+shallow\s+=\s+([^ ]+)\n\s+ignore\s+=\s+([^ ]+)\n'
    )
    matches = re.findall(submodule_pattern, gitmodules_content)
    submodules = []
    for match in matches:
        submodule_name, submodule_path, submodule_url, submodule_shallow, submodule_ignore = match
        submodules.append((submodule_name, submodule_path,
                          submodule_url, submodule_shallow, submodule_ignore))
    return submodules


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert the gitmodules file to git submodule add commands.")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Add --force flag to git command")
    parser.add_argument("gitmodules_file", nargs="?",
                        default=".gitmodules", help="Path to the gitmodules file")
    args = parser.parse_args()
    gitmodules_file = args.gitmodules_file
    modules = convert_and_validate_gitmodules_file(gitmodules_file)

    for name, path, url, shallow, ignore in modules:
        git_command = f"git submodule add {'--force ' if args.force else ''}{url} {path}"
        print(git_command)


if __name__ == "__main__":
    main()
