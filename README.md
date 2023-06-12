# RPGLE Github Scraping

RPGLE Github Scraping is a Python-based program that leverages Github's Code Search REST API to gather data from 1000 RPGLE repositories. The data is then processed using BeautifulSoup to extract the source code, which is compiled into a .csv file using Pandas.
This repo is part of the data aggregation intended to train a small scale coding LLM for RPGLE.

## Usage

To start using the RPGLE Github Scraping program, follow these steps:
1. Clone the repository and add a github api key into '.env-example' and rename to '.env'
2. Run the main Python script:

```bash
python main.py
```

2. The script will start gathering data from RPGLE repositories and process it. Once the process is complete, a .csv file will be generated in the same directory.

## Contact

Josue Sandoval - josuesandoval02@gmail.com

Please feel free to contact me if you have any questions or concerns. Happy coding!
