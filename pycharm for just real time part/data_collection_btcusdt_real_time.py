import pandas as pd
import websocket
import json
from datetime import timedelta, datetime

# import pprint
# import numpy as np


def convert_dataframe(data):
    """
        convert 2d array with timstamp column in to datafram with date and time column
        parameter: 2d array
        return: datafram
    """

    btc_df = pd.DataFrame(data, columns=['close_price', 'close_time'])
    btc_df['close_time'] = pd.to_datetime(btc_df['close_time'], unit='ms')
    return btc_df


# the stream wss
SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

close_price = []
close_timestamp = []


def on_open(ws):
    print('opened connection')


def on_close(ws):
    print('closed connection')


def on_message(ws, message):
    # print('received message')
    json_message = json.loads(message)
    # pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_close = candle['x']
    close_p = candle['c']
    close_t = candle['T']

    if is_candle_close:
        close_price.append(float(close_p))
        close_timestamp.append(close_t)

        if tmiestamp_close_ws <= datetime.now():
            ws.close()


i = 0

while i < 24:
    # set the timestmp for 24 hour later for closing the stream
    tmiestamp_close_ws = datetime.now() + timedelta(hours=1)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open,
                                on_close=on_close,
                                on_message=on_message)
    ws.run_forever()
    # for check the updates every hour
    print(i + 1, " hours have past")
    print(len(close_price), " data have been collected")
    i = i + 1

close_candle = []

# Convert 2 list in to 2d array
for i in range(len(close_price)):
    close_candle.append([close_price[i], close_timestamp[i]])

btc_24h_real_time_df = convert_dataframe(close_candle)
print(btc_24h_real_time_df)

# write them on excel
btc_24h_real_time_df.to_excel('BTCUSDT_24h_real_time.xlsx')
