import pyupbit

access = "5LPBvEU7BnWmyEx0KKjmVLxyJLo4FRw849EqdPVV"          # 본인 값으로 변경
secret = "MIAx007lZpMWCdLpaxrE1iXpL26x3GIOJWlvvzUi"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회