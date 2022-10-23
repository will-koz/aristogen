# Aristogen

Aristogen is a Python script for creating aristocrat and patristocrat ciphers by taking quotes from
Wikiquote. Its name is a portmanteau of aristocrat (the thing it generates) and generate (the
action it performs on aristocrats).

This is built using [wikiquote](https://github.com/federicotdn/wikiquote) package.

## Installation

Once you have Python and make installed on your system, run `./install`. The installer is
self-guided.

## Running

Running Aristogen is done through the wrapper script `./run.sh`. It is a wrapper for `make`. The
default number of quotes is 7; meaning that once you have selected 7 quotes, it will export those to
`quotes.json`, and then ask if you want to edit them. By default, this is done in vim.

Once you are done editing the quotes, the toolchain will continue to make the key and ciphers, and
will finally format them to be printed as HTML.

## License

This is licensed under the [MIT License](license.txt).
