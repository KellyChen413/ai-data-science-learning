
class Car:
  def __init__(self, name, price):
    self.price = price
    self.name = name

  def get_price(self):
    return self.price
    
  def get_twd_price(self):
    return 0

car1 = Car("toyota", 1000000)
pr_usd = car1.get_price()
print(str(pr_usd))

pr_twd = car1.get_twd_price()
print(str(pr_twd))

# 1. 呼叫成員 name 印出廠牌
# 2. 這是全球美金計價, 請改成台幣計價(假設x30)
# 3. 不可以直接在 get_twd_price return  1000000 x 30
# 4. 需要在 get_twd_price 呼叫 self.price

