# gitsubmodulesparser

Convert `.gitmodules` entries into `git submodule add` commands.

## Usage

```bash
# Install deps
pip3 install -r requirements.txt
``````

```bash
# Syntax
python3 convert_gitmodules.py [gitmodules_path] [--force]
```

- `gitmodules_path` (optional): Path to the `gitmodules` file. Default is ".gitmodules".
- `--force` (optional): Include the "--force" flag in the `git submodule add` command. Default is not to include it.

## Example

```bash
# To convert Gitmodules, run the convert_gitmodules.py script.
python convert_gitmodules.py ~/.gitmodules --force

# Output
git submodule add --force https://github.com/tonsky/FiraCode fonts/fira
git submodule add --force https://github.com/JetBrains/JetBrainsMono fonts/JetBrainsMono
git submodule add --force https://github.com/zdharma-continuum/fast-syntax-highlighting .config/zsh/plugins/fast-syntax-highlighting
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
