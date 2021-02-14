# Binance-data-collection-real-time-and-historical
## Summary of task:
*This task has consisted of two-part. First, the close prices of BTC in every minute candles from 24 hours ago needed to be gathered. Secondly, the aforementioned part must be done for the next 24 hours in real-time. Data have been collected from <a href='https://www.binance.com/en'>binance.com</a>*
<br>
</br>

## Bitcoin’s historical prices data in xlsx format:
<p align="left"> For this part of the task, I found a third-party library named <a href='https://python-binance.readthedocs.io/en/latest/'>python-binance</a>. The way this library work needed Binance API to connect to the Binance servers via Python or several other programming languages. due to that, the first step is to create an account with Binance. An API key should be created after it. </p>

**Installing library:**

```
  pip install python-binance
```
<br>
</br>

**Importing library:**

```
  from binance. client import Client
```

**Initialize the client by passing API key and secret:**

```
  client = Client (api_key, api_secret)
```

**make the call for historical data by requesting historical candle data:**

```
  bars = client.get_historical_klines ('BTCUSDT', '1m', timestamp, limit=1000)
```
