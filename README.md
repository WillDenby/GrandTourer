# GrandTourer

GrandTourer is a CLI tool for easily launching applications on MacOS with a two letter command: `gt`. It's a drop-in replacement for `open -a`, but without the need for precise capitalisation, spacing, and first words like "Microsoft" or "Adobe" if you have multiple applications from them.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install GrandTourer. GrandTourer requires Python >=3.8.

```shell
$ pip install grandtourer
```

## Usage

Type `gt` followed by the first few letters of your application name.

There's no need for spaces and capital letters - GrandTourer will find the relevant application. If there is more than one possible match, you might need to include a few more letters.

```shell
$ gt calc
# Launches 'Calculator'

$ gt calculossus
No apps found

$ gt cal
Did you mean one of the following?
1. Calculator
2. Calendar
Enter the number you want. Enter any other number to exit:
```

Also, if you have, for example, the Microsoft Office or Adobe Creative Cloud suites installed, you don't need to include the first word. So:

```shell
$ gt adobeil
# Launches 'Adobe Illustrator'

$ gt il
# Also launches 'Adobe Illustrator'
```

## License

Made by [Will](https://github.com/WillDenby) and released under the [MIT](https://choosealicense.com/licenses/mit/) License
