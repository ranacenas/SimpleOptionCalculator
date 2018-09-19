# Simple Option Calculator
A simple calculator that can run on the terminal for ease of input to calculate options trading scenarios

DISCLAIMER: THIS CALCULATOR DOES NOT PROVIDE ANY ADVICE, RECOMMENDATIONS, OR CLAIM TO PROVIDE ANY ACCURATE INFORMATION. THIS CALCULATOR IS NOT LIABLE FOR ANY LOSSES INCURRED  AND SHOULD BE USED AT YOUR OWN DISCRETION. BY DOWNLOADING AND RUNNING THIS PROGRAM, YOU AGREE TO HAVE READ THIS DISCLAIMER AND ACCEPT TO USE THIS PROGRAM AT YOUR OWN RISK. 

# How to use:
### Download Python 3
If you don't have Python 3 in your computer, download python 3 here https://www.python.org/downloads/.

### Running the program

Download the file and open it using python (right click and click on `open with...`)

## Functions 

### PD = Price Difference Calculator

Enter "pd" when prompted to use this calculator. The purpose of this calculator is to display profit/loss scenarios for various numbers of contracts bought. Upon typing 'pd' and pressing `enter`, it will ask the current price of the long call/put, then the price you hope to sell the long call/put. By pressing `enter`, it will execute and display the net profit/loss, cost of the trade, and the gross cost when selling for each number of contracts in `numcon_pd` (see settings below)

Example

    enter pd or pp pd
    What is the price of the option? 1.75
    What is the price you want get out 2.45
    1.0  contract(s). Profit $ 48.10  buy cost: $ 185.95 Sell Cost: $ 234.05
    2.0  contract(s). Profit $ 116.10  buy cost: $ 361.95 Sell Cost: $ 478.05
    4.0  contract(s). Profit $ 252.10  buy cost: $ 713.95 Sell Cost: $ 966.05
    10.0  contract(s). Profit $ 660.10  buy cost: $ 1769.95 Sell Cost: $ 2430.05

### PP = Profit Predictor 

Enter "pp" when prompted to use this calculator. The purpose of this is to display the price to sell the option to make a profit set in the `profit_goals` variable. It will ask the price of the option, how much you would want to make, and the number of contracts you plan to buy/own. Once executed, it will display the cost of the trade, the price to break even, the profit, and the price to sell the option.

Example

    enter pd or pp pp
    What is the price of the trade 1.75
    How much money do you want to make? 500
    How many contracts? 3
    The cost of this trade is $ 537.95
    To break even, sell at this price $ 1.836
    Sell at $ 3.50 to make $ 500
    Sell at $ 2.00 to make $ 50
    Sell at $ 2.17 to make $ 100
    Sell at $ 2.34 to make $ 150
    Sell at $ 2.50 to make $ 200

# Settings

To change the settings, simply open the python file in an IDE, code editor, or on Notepad(if you don't have any IDEs or code editors) and change the values. When changing the settings on Notepad, ensure that you save the file as a python file by adding ".py" at the end of the file name. It is important you don't change any other code other than the settings to ensure it runs correctly and smoothly.


The only variables that can be changed in this program are `com_base`, `com_per`, `numcon_pd`, and `profit_goals`

**`com_base`** is the base commission for most brokers. If you're using robinhood, you can set this to 0.0.

**`com_per`** is the commission per contract most brokers charge. Current default setting is 1.0 for $1.00.

**`numcon_pd`** is a list of integers that represent the number of contracts in a scenario. So, if you are wondering how much an option trade would cost you and by how much a profit/loss would be depending on the amount of contracts you buy, the program will display and calculate it for you.

**`profit_goals`** is a list of integers that the program will use to calculate the price to sell the long option. For example, the current list is 50, 100, 150, and 200 therefore this program will use this list to calculate at what price to sell the long option to make $50, $100, $150, and $200. 

