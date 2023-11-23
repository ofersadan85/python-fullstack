# VSCode plugins / extensions

We've already installed the Python extension, but there are a few more extensions that are useful for Python development, and development in general.

To install them, open VSCode and click on the "Extensions" icon in the left menu. Search for the following extensions and click "Install" (or "Update" if you already have them installed):

| extension | Description |
| --- | --- |
| Python | Python language support for VSCode |
| Python Extension Pack | A collection of popular Python extensions |
| Black Formatter | Code formatter, makes your code look nice, can be used with the keyboard shortcut `Alt+Shift+F` |
| Code Spell Checker | Checks your spelling in comments and strings |
| Error Lens | Shows errors and warnings inline |
| Flake8 | Linter, checks your code for errors and warnings |
| Git Graph | Shows a graph of your git history |
| GitHub Repositories | Shows your GitHub repositories in VSCode |
| isort | Sorts your Python imports |
| Prettier | Code formatter, makes your code look nice, can be used with the keyboard shortcut `Alt+Shift+F`. Note: We'll prefer to use Black Formatter instead of Prettier for Python code, but we'll use Prettier for other files like HTML, CSS, JavaScript, JSON, etc. |
| vscode-icons | Adds icons to files in the file explorer, just nice to have |

Each of these extensions has a page on the [VSCode Marketplace](https://marketplace.visualstudio.com/VSCode) where you can read more about them. Make sure to install the ones you think you'll need. Be careful when installing unfamiliar extensions, as they can slow down VSCode and cause other issues, including security issues.

Don't be afraid to remove extensions that you don't use or that you find annoying. You can always install them again later, and there is no mandatory set of extensions that you must have in this course (except for the Python extension).

## Customizing extensions

Most extensions have many configuration options, but we'll leave them at their default values for now. You can always change them later if you want. You can edit these either by right-clicking on the extension in the Extensions menu and clicking "Extension Settings", or by clicking on the "Settings" icon in the left menu and searching for the extension name. These settings can be synced across devices if you connect your VSCode to your GitHub account, and turn on "Settings Sync" in the VSCode settings.

## Example settings

We can also view and edit all VSCode settings (including extension settings) in JSON format by clicking `Ctrl+Shift+P` and searching for "Open User Settings (JSON)". Here is my example settings (with a brief description for each one), which include all of the above mentioned extensions, you may copy and replace any part you like to match your settings to mine:

```json
{
    "editor.inlineSuggest.enabled": true,  // Show suggestions inline, instead of in a popup
    "files.autoSave": "afterDelay",  // Automatically save files after a delay
    "git.autofetch": true, // Automatically fetch changes from remote repositories, i.e. GitHub
    "git.autorefresh": true, // Automatically refresh the git status bar
    "git.confirmSync": false, // Don't ask for confirmation when syncing changes
    "isort.args": [  // isort extension settings
        "--profile=black",  // Use the "black" profile to match with the Black Formatter extension
        "--line-length=120" // Use a line length of 120 characters, instead of the default 80
    ],
    "vsicons.dontShowNewVersionMessage": true,  // Don't show the "New version available" message
    "workbench.iconTheme": "vscode-icons",
    "[jsonc]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"  // Use Prettier to format JSON files with the "jsonc" syntax
    },
    "[json]": {
        "editor.defaultFormatter": "vscode.json-language-features"  // Use the built-in JSON formatter for JSON files with the "json" syntax
    },
    "black-formatter.args": [  // Black Formatter extension settings
        "--line-length=120"  // Use a line length of 120 characters, instead of the default 88
    ],
    "flake8.args": [  // Flake8 extension settings
        "--line-length=120"  // Use a line length of 120 characters, instead of the default 79
    ],
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"  // Use Black Formatter to format Python files
    },
}
```
