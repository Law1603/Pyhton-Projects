# Stock-Price-Predictor
This program predicts stock prices using LSTM (Long Short-Term Memory) neural networks. The data is fetched using the `yfinance` library which connects to Yahoo Finance. To view this code https://github.com/Law1603/Pyhton-Projects/blob/main/Stock%20Price%20Predictor/Stock%20Price%20Predictor.py

## Steps Taken to Create this Project

1. **Data Collection:** Used the `yfinance` library to fetch historical stock prices from Yahoo Finance.
2. **Data Preprocessing:** The fetched data was scaled using `MinMaxScaler` from `scikit-learn` to transform the stock prices to a range of 0 to 1.
3. **Model Building:** Built an LSTM (Long Short-Term Memory) model using `tensorflow`. This model takes the past 60 days of stock prices to predict the next day's closing price.
4. **Model Training:** The LSTM model was trained on the historical stock data.
5. **Testing and Prediction:** After training, the model was tested on more recent data to predict stock prices and compare them with actual prices.
6. **Visualization:** Used `matplotlib` to visualize the actual vs. predicted stock prices.

## Libraries Used

- `numpy`: For numerical operations and data manipulation.
- `pandas`: For handling and analyzing structured data.
- `matplotlib`: For plotting and visualizing data.
- `yfinance`: For fetching stock data from Yahoo Finance.
- `tensorflow`: For building and training the LSTM neural network model.
- `scikit-learn`: For data preprocessing using `MinMaxScaler`.

## How to Run

1. Ensure you have the required libraries installed:
    ```
    pip install numpy matplotlib pandas yfinance tensorflow scikit-learn
    ```

2. Run the `main.py`:
    ```
    python main.py
    ```

## Tested Stocks

The program has been tested for the following stocks:
- Tesla (TSLA)
![image](https://github.com/Law1603/Stock-Price-Predictor/assets/78369461/bde41416-b8e3-48b0-ae32-b5d71f9ceca4)

- JP Morgan (JPM)
  ![image](https://github.com/Law1603/Stock-Price-Predictor/assets/78369461/82f2d7a5-78ee-42c1-90c0-ab3ce8511099)

- Apple (AAPL)
  ![image](https://github.com/Law1603/Stock-Price-Predictor/assets/78369461/9fdc7ca7-7f38-4e1b-aa3a-0c374b269878)


## Disclaimer

 **Do not use it to make investment decisions**. The stock market is unpredictable and influenced by numerous factors outside the scope of this program. 
