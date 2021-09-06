import pancakeswap

INPUT_TOKEN_ADDRESS = ""
OUTPUT_TOKEN_ADDRESS = ""


def execute():
    exchangeType = input("Buy(1)/Sell(2): ")
    while (True):
        if (exchangeType == "1"):
            print("\n=================================> BUY")
            # Buy
            inputAmount = input("Input amount: ")
            if (inputAmount == "exchange"): execute()
            if (inputAmount == "restart"):
                print("\n" * 30)
                run()
            tokens = float(inputAmount) / float(input("Token price: "))
            print("Expected tokens: " + str(tokens))
            pancakeswap.exchange(INPUT_TOKEN_ADDRESS, OUTPUT_TOKEN_ADDRESS, inputAmount, tokens)
        else:
            print("\n=================================> SELL")
            # Sell
            tokens = input('Sell amount: ')
            if (tokens == "exchange"): execute()
            if (tokens == "restart"):
                print("\n"*30)
                run()
            outputAmount = float(tokens) * float(input("Token price: "))
            print("Expected output: " + str(outputAmount))
            pancakeswap.exchange(OUTPUT_TOKEN_ADDRESS, INPUT_TOKEN_ADDRESS, tokens, outputAmount)

def run():
    INPUT_TOKEN_ADDRESS = input("Input token address: ")
    OUTPUT_TOKEN_ADDRESS = input("Output token address: ")
    execute()

run()
