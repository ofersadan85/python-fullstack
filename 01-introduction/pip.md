# PyPi / pip

Python comes with it's own package manager called `pip`. It's used to install packages from the [Python Package Index (PyPi)](https://pypi.org/). Most installations of Python will already have `pip` installed, you can verify by running one of the following commands in your terminal:

```powershell
pip
pip --version
python -m pip
py -m pip  # On Windows only
py -3.9 -m pip  # If you have multiple versions of Python installed on Windows
python3 -m pip  # On Linux/MacOS
python3.9 -m pip  # If you have multiple versions of Python installed on Linux/MacOS
```

If you get an error, you can install `pip` by following the instructions [here](https://pip.pypa.io/en/stable/installing/). Usually, you can install `pip` by running one of the following commands in your terminal:

```powershell
python -m ensurepip --upgrade
py -m ensurepip --upgrade  # On Windows only
py -3.9 -m ensurepip --upgrade  # If you have multiple versions of Python installed on Windows
python3 -m ensurepip --upgrade  # On Linux/MacOS
python3.9 -m ensurepip --upgrade  # If you have multiple versions of Python installed on Linux/MacOS
```

And then verify that it's installed by running one of the commands above.

## Installing packages

Once you have `pip` installed, you can install packages by running the following command in your terminal:

```powershell
pip install <package-name>
```

For example, to install the `httpx` package, you would run:

```powershell
pip install httpx
```

Or to install a specific version of a package, you can run:

```powershell
pip install <package-name>==<version>
```

For example, to install version `0.18.2` of the `httpx` package, you would run:

```powershell
pip install httpx==0.18.2
```

We might already have `httpx` installed but wish to update it to the latest version. To do this, we can run:

```powershell
pip install --upgrade httpx
```

## Dependant packages

When you install a package, it might have other packages that it depends on. These packages will be installed automatically. For example, the `httpx` package depends on the `certifi` package. When you install `httpx`, `certifi` will be installed automatically.

## Uninstalling packages

To uninstall a package, you can run:

```powershell
pip uninstall <package-name>
```

For example, to uninstall the `httpx` package, you would run:

```powershell
pip uninstall httpx
```

## Requirements file

When you install a package, you can specify the version you want to install. For example, to install version `0.18.2` of the `httpx` package, you would run:

```powershell
pip install httpx==0.18.2
```

You can also specify the version of a package in a file called `requirements.txt`. This file can be used to install multiple packages at once. For example, if we have a `requirements.txt` file that looks like this:

```text
httpx==0.18.2
certifi==2020.12.5
```

We can install all the packages in the file by running:

```powershell
pip install -r requirements.txt
```
