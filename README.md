# CoinComplete: A Principle Component Analysis machine learning tool used for Cryptocurrency investing.

+ Run Instructions:

First install the required packages:
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
Run this program to load the data **NOTE: Date Variables are able to be changed**:
```
python data_processor.py
```

Run with Jupyter Notebook **NOTE: Model able to be changed**:
```
sentiment.ipynb
```

To start trading with trained data run **NOTE: Target coin able to be changed**:
```
trading.ipynb
```

**NOTE** this will NOT work unless you replace the key values in the keys.py with YOUR unique secret key and API key generated here https://www.binance.us/settings/api-management?tab=exchange (mine loaded for educational use only).