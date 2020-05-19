# 주식 사고 팔기

## Description.

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

주어지는 배열의 i번째 요소는 i번째 날의 주식 가격이다.
주식을 한 번 사고, 한 번 팔 수 있다.
최대의 이익이 무엇인지 찾아라. 
단, 주식을 사기 전에 팔 수 없다. 

<hr/>

## Solution.

<pre>
배열의 길이가 0인 경우를 예외로 처리해준다.

배열의 0번째 요소를 buy 변수에 저장해둔다. (buy = prices[0])

손해가 없는 결과를 내야하므로 이익의 최대는 0으로 해둔다. (mx_profit = 0)

이득은 현재 가격 - 산 주식으로 하고 계산을 해본다. (profit = prices[i]-buy)

만약 현재 주식을 판다고 했을 때 가장 높은 이익이 난다면 팔아서 mx_profit에 더 높은 값이 들어가도록 갱신한다.

      if profit>mx_profit:
         mx_profit = profit
         
현재 주식의 가격이 더 낫다면 이걸 사게된다. 

      if buy>prices[i]:
         buy = prices[i]
 
</pre>            
          
