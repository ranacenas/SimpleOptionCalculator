
def total_cost_of_trade(x, y):         #For options trading 
    cost = (x*y*100)+ 4.95 + (0.75*y)
    return cost                     #x = price of contract y=number of contracts
#to be continued: create algorithm for desired profits, what price to sell at,
#predicting future stock prices

def return_cost(x,y):
    ret = (x*y*100) - 4.95 - (0.75*y)
    return ret

def profit_prediction(x, y, z):   #z= current price of contract
    profit = ((z-x)*y*100)-4.95-(y*0.75)
    return profit

def contractcom(f):
    com = 4.95+ (f * 0.75)
    return float(com)

if __name__=='__main__':

    count = 0
    tries = 10000
    
  
    while count < tries:
        setting = input('enter pd or pp ')
        if setting == 'pd':
            p1 = input('What is the price of the option? ')
            p2 = input('What is the price you want to get out ')
            numcon = input('How many contracts?')

            price1 = total_cost_of_trade((float(p1)), (float(numcon)))
            price2 = return_cost((float(p2)), (float(numcon)))
            print( price2 - price1)
            print (price1)
            print(price2)
            
        if setting == 'pp':
            
            potential = input\
        ('What is the price of the trade ')
            des = input('How much money do you want to make? ')
            numcon = input('How many contracts?')
        
            p = total_cost_of_trade((float(potential)), (float(numcon)))
            beven = (float(p)+ contractcom(float(numcon)))/(float(numcon)*100)
            desi = (float(p) + float(des) + contractcom(float(numcon)))/ (float(numcon)* 100)
        
            print ("The cost of this trade is",(p))
            print ("To break even, sell at this price", "%.3f" %(beven))
            print ("Sell at", "%.2f" % (desi), "to make", (des))
     

