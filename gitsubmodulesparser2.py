#!/bin/env python3
import re
import sys
import os
import argparse
from configparser import ConfigParser

gitmodules=".gitmodules"

def convert_gitmodules(gitmodules_file=gitmodules, force=False):
    """Convert gitmodules file to git submodule add commands.

    Args:
        gitmodules_file (str): Path to the gitmodules file. Default is ".gitmodules".
        force (bool): Whether to add the "--force" flag to the git command. Default is False.

    Returns:
        str: Converted git submodule add commands.
    """
    config = ConfigParser(allow_no_value=True)
    config.read(gitmodules_file)

    result = []
    for section in config.sections():
        if config.has_option(section, 'url'):
            submodule_name = config.get(section, 'name', fallback=section)
            submodule_path = config.get(section, 'path')
            submodule_url = config.get(section, 'url', fallback=None)

            git_command = "git submodule add"
            if force:
                git_command += " --force"
            git_command += f" {submodule_url if submodule_url else ''} {submodule_path}"
            result.append(git_command)

    return "\n".join(result)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true", help="Add --force flag to git command")
    parser.add_argument("gitmodules_file", nargs="?", default=gitmodules, help="Path to the gitmodules file")
    args = parser.parse_args()

    output = convert_gitmodules(args.gitmodules_file, args.force)
    print(output)
