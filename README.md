# GrandTourer

GrandTourer is a CLI tool for easily launching applications on MacOS with a two letter command: ```gt```. It's a drop-in replacement for ```open -a``` - with string matching.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install GrandTourer.

```bash
pip install grandtourer
```

## Usage

Type gt followed by the first few letters of your application name.

Spaces, capitals, it doesn't matter - GrandTourer will find the relevant application. If there is more than one possible match, you might need to include a few more letters.

```shell
$ gt saf
# Launches Safari

$ gt skadawb
No apps found

$ gt cal
Did you mean one of the following?
calculator
calendar
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
