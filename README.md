# CoinComplete: A Principle Component Analysis Machine Learning Tool Used for Cryptocurrency investing.

# Abstract

My research determines if using machine learning to predict buy and sell orders through the Binance market is profitable.  Using a Principle component analysis (PCA) model to infer predictions on future market activity.  These predictions will be used to trade multiple currencies profitably.  For the purpose of this research, I will just be looking at Bitcoin (BTC) and Ethereum (ETH) as they are the most frequently traded coins. Using the Binance API, data is able to gathered from the present and the past.  Using this data in a Python script allows for manipulation of the data by applying it to the hyperparameters of the model.  The information that I am gathering will be able to predict when a person should buy and when a person should sell.  The research done here is done with careful consideration of previous other research done.  Previous research has taken a look at various other methods that have proven not successful.  Most other research had also taken place during a bull market when this research differentiates itself by being done during a bear market. This is research is intended to be used by crypto currency market analysts of any capacity.  It is something that is intended to help market traders more accurately know when to buy and sell.  This research was conducted to further the understanding of cryptocurrency market activity.  It attempts to answer questions about how to create profitable trading strategies in the crypto market.

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

# Conclusions

The results of this tool should not be taken as real financial recommendations. This is only meant to see if the previous market trends can indicate future market results. While the average result that we get from this is just above random, messing with the data the model is trained on could prove to be an interesting experiment.
