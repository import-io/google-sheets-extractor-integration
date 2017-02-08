# Import.io Google Sheets Extractor Integration

This repository includes a script solution that uses URLs taken from a Google sheet
and copies to an existing Import.io Extractor, then lastly executes the Extractor
to collect data from the supplied URLs.

The command script is implemented using Python, which can be executed on any
operating system that supports a Python version 3.5 or later.

## Installation

The command requires the installation of Python 3.5 or later with some additional
third-party packages that can be installed using [pip](https://pip.pypa.io/en/stable/).

```
$ pip install importio_gsei
```

## Operation

The command has 6 different sub-commands that are invoked similiarly as follows:

```
$ gsextractor <sub-command>
```

where `sub-command` is one of the following:

- _copy-urls_ - Copies URLs from a specified Google sheet to designated Extractor.
- _extractor-start_ - Initiates a crawl-run of an Extractor.
- _extractor-status_ - Provides a status of the crawl-run(s) of an Extractor.
- _extractor-urls_ - Displays the list of URLs associated with an Extractor.
- _extract_ - Performs the complete extraction operation from copying the URLs from the Google
sheet to running the Extractor to extract data from web pages.
- _sheet-urls_ - Displays a list of the URLs in a Google sheet given the sheet id and range.

Help can be displayed which shows the available sum-commands as follows:

```
$ gsextractor -h
usage: gsextractor [-h] [-v]
                  {copy-urls,extract,extractor-start,extractor-status,extractor-urls,sheet-urls}
                  ...

Google Sheets URL Feed

positional arguments:
  {copy-urls,extract,extractor-start,extractor-status,extractor-urls,sheet-urls}
                        commands
    copy-urls           Copies URLs from google sheet to an extractor
    extract             Runs the full extraction process
    extractor-start     Starts an extractor
    extractor-status    Displays the status of recent craw runs
    extractor-urls      Displays the URLs from an extractor
    sheet-urls          Displays the URLs from a google sheet

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

Detail help on each of the commands is provided by the `-h` with the corresponding sub-command:

```
$ gsextractor <sub-command> -h
```

The version of the program can be displayed by running the command with the `-v` option:

```
$ gsextractor <sub-command> -v
0.3.0
```

### copy-urls

Copy the URLs in the Google Sheet to the Extractor URLs

```
$ gsextractor copy-urls -i <spreasdheet_id> -r <spreadsheet_range> -e <extractor_id>
```

### extractor-start

Initiate a crawl-run on a specific Extractor

```
$ gsextractor extractor-start -e <extractor_id>
```

### extractor-status

Display the status of a crawl-run(s) on a specific Extractor

```
$ gsextractor extractor-status  -e <extractor id>
```

### extractor-urls

Displays the URLs associated with a specific Extractor

```
$ gsextractor extractor-urls  -e <extractor id>
```

### extract

Runs the complete operation of copying URLs from a Google sheet to an Extractor, and starting the Extractor

```
$ gsextractor extract -i <spreasdheet_id> -r <spreadsheet_range> -e <extractor_id>
```

### sheet-urls

Displays the URLs from a specifice Google sheet and range

```
$ gsextractor sheeturls -i <spreasdheet_id> -r <spreadsheet_range>
```

## Programmatic Execution

The same operations as listed above can performed programmatically from Python similar to the following
example:

```python
from importio_gsei import GsExtractorUrls

g = GsExtractorUrls()
g.extractor_start(extractor_id)
```

### copy_urls()

```python
from importio_gsei import GsExtractorUrls

g = GsExtractorUrls()
g.copy_urls(spread_sheet_id, spread_sheet_range, extractor_id)
```

### extractor_start()

```python
from importio_gsei GsExtractorUrls

g = GsExtractorUrls()
g.extractor_start(extractor_id)
```

### extractor_status()

```python
from importio_gsei import GsExtractorUrls

g = GsExtractorUrls()
crawl_runs = g.extractor_status(extractor_id)
for crawl_run in crawl_runs:
    print(crawl_run)
```

### extractor_urls()

```python
from importio_gsei import GsExtractorUrls

g = GsExtractorUrls()
urls = g.extractor_urls(extractor_id)
for url in urls:
    print(url)
```

### extract

```python
from importio_gsei import GsExtractorUrls

g = GsExtractorUrls()
g.extract(spread_sheet_id, spread_sheet_range, extractor_id)
```

### sheet_urls

```python
from importio_gsei import GsExtractorUrls

g = GsExtractorUrls()
urls = g.extract(spread_sheet_id, spread_sheet_range)
for url in urls:
    print(url)
```





