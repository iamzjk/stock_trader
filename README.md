# stock_trader

## Installation

* Python3.4 (zipline only work with python2.7/3.4) and Anaconda

		conda create -n stock_trader python=3.4 anaconda

	Activate virtual env  

		source activate stock_trader

* zipline
		
		conda install -c Quantopian zipline

* talib
		
		conda install -c Quantopian ta-lib

* pyfolio

		conda install -c Quantopian pyfolio


## Bug Fix For zipline
Replace the benchmarks.py file in zipline with:
[benchmarks.py](https://github.com/zipline-live/zipline/blob/master/zipline/data/benchmarks.py)

*The issue was caused by the connection to Yahoo Finance. The fix uses Google Finance API instead.*

## Test
1. Run zipline ingest to download finance data to local  

		$zipline ingest

2. Run `test_zipline.ipynb` to test the installation of zipline