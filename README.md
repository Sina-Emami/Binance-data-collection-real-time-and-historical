# Binance data collection real-time and historical
## Summary of project:
*This project has consisted of two-part. First, the close prices of BTC in every minute candles from 24 hours ago needed to be gathered. Secondly, the aforementioned part must be done for the next 24 hours in real-time. Data have been collected from <a href='https://www.binance.com/en'>binance.com</a>*
</br>

## Bitcoin’s historical prices data in xlsx format:
<p align="left"> For this part of the task, I found a third-party library named <a href='https://python-binance.readthedocs.io/en/latest/'>python-binance</a>. The way this library work needed Binance API to connect to the Binance servers via Python or several other programming languages. due to that, the first step is to create an account with Binance. An API key should be created after it. </p>
</br>

**Installing library:**

```
  pip install python-binance
```

**Importing library:**

```
  from binance. client import Client
```
</br>

**Initialize the client by passing API key and secret:**

```
  client = Client (api_key, api_secret)
```
</br>

**Make the call for historical data by requesting historical candle data:**

```
  bars = client.get_historical_klines ('BTCUSDT'(symbol), 
                                       '1m'(Candles interval), 
                                       timestamp(Star getting data from this Timestamp), 
                                       limit=1000)
```
</br>

In the background, this endpoint will continuously query the API in a loop, collecting 1000 price points at a time, until all data from the start point reaches the now timestamp.

![historical Kline payload](images/historical%20Kline%20payload.jpg) 
<br>
</br>
Here is a definition of the data returned as per the Binance API documentation, and only the close and close time is needed:   

```
  bars_arr = bars_arr[:, [4,6]]
```

After that, the data must be converted to a data frame and the time column should be transformed to date and time. At last, it would be written into excel.

## Bitcoin’s real time prices data in xlsx format:
<p align="left"> For this part, it is better to stream the updates. what I mean is that, The Kline/Candlestick Stream push updates to the current klines/candlestick every second and it is possible to collect the data in real-time. To stream the data, I choose the WebSocket library. Every second message would receive from the stream which is in JSON format and contain some information. Only the close price and close time of candles are important, duo to that the code would store the data from massages just when “Is this kline closed?” be True. Additionally, the massage must be converted to something that python understands. </p>
</br>

![real_time stream Kline payload](images/real_time%20stream%20Kline%20payload.jpg) 
<br>
</br>
Here is the message that we receive in the stream. the kline close time(“T”), close price(“c”) and Is this kline closed? (“x”) are needed.
<br>
</br>

**Installing library:**
```
  pip install websocket_client
```
</br>

**Importing library:**
```
  import websocket
```
</br>

websocket.WebSocketApp a stream address connection needed. (this informantion was gathered from <a href="https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams">binance spot api documantion</a>)
*	The base endpoint is: wss://stream.binance.com:9443
*	Streams can be accessed either in a single raw stream or in a combined stream
*	Raw streams are accessed at /ws/<streamName>
*	For Kline/Candlestick Streams Name: '<'symbol'>'@kline_'<'interval'>'
</br>
  
**The aforementioned lines were from binance-spot-api documentation. The address I will use:**

```
  SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
```
</br>

The stream must be close after 24 hours that’s why a timestamp needed to close it:
```
  tmiestamp_close_ws = datetime.now() + timedelta(hours=24)
```

at the end all the collection data should be converted to data frame so they can be written on xlsx format file.


## The way code run:
```
  python data_collection_btcusdt_real_time
```

for the historical data you need to pass the api key and api secret.
</br>

## Sources:
* <a href="https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams"> binance github document</a>
* https://python-binance.readthedocs.io/en/latest/overview.html
* https://algotrading101.com/learn/binance-python-api-guide/

