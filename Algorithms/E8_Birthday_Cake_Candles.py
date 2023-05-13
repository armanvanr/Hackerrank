def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for candle in candles:
        if candle == tallest:
            count+=1
    return count
print(birthdayCakeCandles([4,4,1,3]))

def birthday_cake_candles(candles):
    tallest = max(candles)
    return candles.count(tallest)
print(birthday_cake_candles([4,4,1,3]))