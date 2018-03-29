# CDR Parser

Cli application to parse Cisco cdr records into xlsx worksheets.


The program parses and output a small subset of columns. Currently it only supports the follwoing

```python
['gcid',
'calling_party',
'called_party',
'reached_party',
'duration',
'datetime_connected',
'datetime_disconnected',
'datetime_placed']
```

## Getting Started

### Installing

Clone the [stable](https://github.com/krasnyineko/CDR-Parser/tree/stable) branch and install using either pip or setup.py

### Running

Basic syntax. If no output is specified the file is automatically given a name with the format of `%Y-%m-%d_%H%M%S.xlsx`

```
Usage: cdrparser [OPTIONS] CDR_CSV [CRITERIA]...

Options:
  -o, --output TEXT
  --help             Show this message and exit.

```

#### Examples

Parse with no filter and output to parsed.xlsx

```bash
cdrparser -o parsed.xlsx cdr_records.csv
```

Parse and save only records that contain the phone numbers specified

```bash
cdrparser cdr_records.csv 9998887777 7899 5678

```

## TODO

* [ ] Add CSV writer
* [ ] Add Tests
* [ ] Improve filtering to apply to all columns
* [ ] Allow specification of which columns to output


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/krasnyineko/CDR-Parser/tags).
