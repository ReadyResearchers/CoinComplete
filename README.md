# CoinComplete: A Principle Component Analysis Machine Learning Tool Used for Cryptocurrency investing.

# Run Instructions:

1. Clone the repository locally

2. Install the required packages:
```
pip install tensorflow
pip install numpy
pip install python-binance
pip install binance
pip install pandas
pip install collections
pip install plotly
pip install scikit-learn
pip install ta
pip install warnings
pip install plot_utils
pip install time
pip install random
pip install keras
pip install os
```
**RUNS BEST IN VISUAL STUDIO WITH ms-toolsai.jupyter**
**LOOK FOR ALL CAP COMMENTS FOR CHANGEABLE VARIABLES**

Run this program to load the data **NOTE: Date time frame variables are able to be changed inside file**:
```
python data_processor.py
```
Use: Shows heat map dislaying profit loss (A great way to find good target data)

Run with Jupyter Notebook **NOTE: Model able to be tweaked inside file**:
```
sentiment.ipynb
```
Use: Used to train model off of data collected. Also able to change model variables:
```
SEQ_LEN = 60  # how long of a preceding sequence to collect for RNN
FUTURE_PERIOD_PREDICT = 3  # future prediction length
RATIO_TO_PREDICT = "BTC" # Coin being predicted
EPOCHS = 10  # passes
BATCH_SIZE = 64  # amount of in batch
```

To start trading with trained data run **NOTE: Target coin able to be changed inside file**:
**Example Input: BTC-60-SEQ-3-PRED-1679535879 (found in /models)**
```
trading.ipynb
```
Used: Used to conduct live market orders on the Binance.US exchange(amount traded is how confident the prediction is).


**NOTE** this will NOT work unless you replace the key values in the keys.py with YOUR unique secret key and API key generated here https://www.binance.us/settings/api-management?tab=exchange (mine loaded for educational use only).
