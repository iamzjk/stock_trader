# stock_trader

## Dependencies

### Python3.4 (zipline only work with python2.7/3.4) and Anaconda
`conda create -n stock_trader python=3.4 anaconda`
`source activate stock_trader`

### zipline
`conda install -c Quantopian zipline`

### talib
`conda install -c Quantopian ta-lib`

### pyfolio
`conda install -c Quantopian pyfolio`


### Fix a bug in zipline
replace the benchmarks.py file in zipline with:
https://github.com/zipline-live/zipline/blob/master/zipline/data/benchmarks.py

the issue was caused by the connection to Yahoo Finance. The fix use Google Finance instead.

### Run zipline ingest to download finance data to local
`$zipline ingest`

### Run test_zipline.ipynb to test the installation of zipline