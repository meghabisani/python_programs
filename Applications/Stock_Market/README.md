Stock Market!!
----------------------------------------------------------------
Generate a trading algorithm using historical data.


Introduction
----------------------------------------------------------------

1) When using historical data, algorithm will be able to make perfect trading choices. 
2) By looking at the data, algorithm will be able to select the best times to enter the market and the best time to exit in order to maximise return. 

	Rules to be observed:
	1. A trade must be open for a minimum of 30 mins and closed before reaching 60mins.
	2. Only 1 trade active at a time (eg, close at 1:36 time period you can then
	open at 1:37).
	3. Only make a profit from buying low and selling high.

3) The algorithm is only investing 1 ‘unit’ in each trade. If algorithm enters the market at 1.1
and exits at 1.2 then the algorithm has made 0.1 units of profit. 
4) Summing the return over all trades gives the algorithm’s total return. 

Data:
The data is a CSV file with 2 columns, time and price. Time is the minute for the data point, for
example, time=94 is 01hr 34mins. An Example of what the CSV file looks like is (full data in
external file):
Time,Price
0,1.2546
1,1.2567
2,1.2577
3,1.2579
4,1.2593
5,1.2668
6,1.2695
7,1.2689
8,1.2679
9,1.2679
10,1.2678

The following sample output was generated on a data set with 240 data points:

Trades are
Open at 0 (1.2546), close 58 (1.2796) for profit 0.025
Open at 64 (1.2635), close 94 (1.2845) for profit 0.021
Open at 101 (1.275), close 138 (1.2929) for profit 0.0179
Open at 139 (1.2846), close 169 (1.3016) for profit 0.017
Open at 178 (1.2943), close 228 (1.3728) for profit 0.0785
total profit 0.1594

Execution
----------------------------------------------------------------
To run the game:
python stock_market.py