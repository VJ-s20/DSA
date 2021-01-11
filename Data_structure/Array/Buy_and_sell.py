'''
Buy and sell stocks:-
'''
A=[310,315,275,295,260,270,290,255,250]

# * Approch-1: using brute force
#! Time complexity: O(n^2)
#! space complexity O(1)

def buy_and_sell(stocks):
    max_profit=0
    for i in range(len(stocks)-1):
        for j in range(i+1,len(stocks)):
            if stocks[j]-stocks[i]>max_profit:
                max_profit=stocks[j]-stocks[i]
    return max_profit
print(buy_and_sell(A))
print("\n\n")


# * Approch 2: step-1: setting min val to the first item
# * step2: subtrating it form bigger val 
#* step3: if we found lesser val than a prev min val we update the min val
# * step4: and then try to found max val form min vaules 
#! Time coplexity: O(n)
#! space complxity: O(1)

def buy_and_sell(stocks):
    max_profit=0
    min_val=stocks[0]
    for i in range(1,len(stocks)):
        min_val=min(min_val,stocks[i])
        compare_val=stocks[i]-min_val
        max_profit=max(max_profit,compare_val)
    return max_profit
print(buy_and_sell(A))