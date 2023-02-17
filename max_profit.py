
import sys

# Trick
# low: Tracks lowest price encountered so far.
# temp_profit: current-val - lowest value so far (makes it forward looking)
# ---- temp_profit could go up or down based on current value.
# profit: Keeps track of highest profit so far, gets overwritten only when we see higher profit.
class MaxProfit:
  def __init__(self, prices):
    self.prices = prices

  def max_profit(self):
    high = 0
    low = sys.maxsize
    profit = 0
    for i, p in enumerate(self.prices):
      if low > p:
        low = p
        low_i = i
      temp_profit = p - low  
      if temp_profit >= profit:
        profit = temp_profit
    return (profit)

if __name__ == '__main__':
  prices = [7,1,5,3,6,4]
  m = MaxProfit(prices)
  p = m.max_profit()
  print (f'Max profit: {p}')

