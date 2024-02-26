# NPM - Node Package Manager

We will use NPM to install packages for our JavaScript projects. NPM is a package manager for JavaScript, and it is the default package manager for the JavaScript runtime environment Node.js.

NPM Comes pre-installed with Node.js, so if you have Node.js installed, you should have NPM installed as well. On Windows, we'll use NVM-Windows to install Node.js and NPM.

So we'll have 3 main steps:

1. [NVM-Windows installation](#nvm-windows-installation)
2. [Node.js installation](#node-installation) (we'll use NVM-Windows to install the latest version of Node.js)
3. [Verification](#verification)

## NVM-Windows installation

[![Download zip](https://custom-icon-badges.demolab.com/badge/-Download-blue?style=for-the-badge&logo=download&logoColor=white "Download NVM-Windows")](https://github.com/DenverCoder1/readme-download-button-action/archive/1.0.2.zip)

NVM = Node Version Manager. It allows you to install and manage multiple versions of Node.js on the same machine. This is useful when you have multiple projects that require different versions of Node.js. It also allows you to switch between versions easily.

The NVM-Windows GitHub repository is located [here](https://github.com/coreybutler/nvm-windows), but you can go directly to [this link](https://github.com/coreybutler/nvm-windows/releases/latest/download/nvm-setup.exe) or the button above to download the latest installer.

Accept all the default options during the installation.

After the installation, open a new command prompt and type `nvm`. If you see the help message, then NVM is installed correctly.

## Node installation

Now that we have NVM installed, we can use it to install Node.js. Open a new command prompt and type the following command:

```powershell
nvm install latest
```

And after it's done, also type:

```powershell
nvm use latest
```

This will set the latest version of Node.js as the default version.

## Verification

If nothing went wrong, you should be able to type the following commands and get the versions of NVM, Node.js and NPM:

```powershell
nvm --version
node --version
npm --version
```

If you see the versions of NVM, Node.js and NPM, then everything is installed correctly. The latest versions at the time of writing are:

- NVM: 1.1.12
- Node.js: v21.6.2
- NPM: 10.2.4
