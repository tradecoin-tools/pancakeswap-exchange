Pancakeswap update price too slow so sometime we loss the perfect price. This tool will help you exchange on Pancakeswap with no delay time.

# Installation guide
`If you need 1:1 support, please read the end of this page.`

## Step 1: Environment
#### Windows
Step by step as this guide: https://phoenixnap.com/kb/how-to-install-python-3-windows

#### MacOS
Step by step as this guide: https://docs.python-guide.org/starting/install3/osx/

#### Linux
If you're using linux, I think you all know how to do that. In case you don't know, please install Windows or MacOS then follow the above guide.

## Step 2: Install & Run
Install git for your machine.

Open terminal then type the following command
```shell script
git clone git@github.com:tradecoin-tools/pancakeswap-exchange.git
```
```shell script
cd pancakeswap-exchange
```
```shell script
pip install -r requirements.txt
```

Open config.py file then edit `YOUR_PUBLIC_KEY` (your wallet address) and `YOUR_PRIVATE_KEY`

Run app with the following command
```shell script
python main.py 
```

## How to use
Once run successfully, you can trade with some following very simple steps:
- Enter trading pair

    ```shell script
    Input token address:
    ``` 
    This is the address of the first token such as USDT/BUSD/BNB/...
    
    Note that it's TOKEN ADDRESS, isn't TOKEN SYMBOL. 
    For example token address of BUSD is `0xe9e7cea3dedca5984780bafc599bd69add087d56`. You can find token address on https://bscscan.com

- Enter trading type:
    ```shell script
    Buy(1)/Sell(2): 
    ```
    Enter 1 for "BUY" and 2 if you "SELL"

- Enter amount:
    ```shell script
    Input amount:
    ```
    If you want to buy, you will input amount of USDT/USDC/BNB here.
    If you want to sell, you will input amount of the token that you're selling here.

    ```shell script
    Token price:
    ```
    Enter token price that you want to BUY or SELL here.
    
- Transaction will be submitted then return tx hash. You can see this transaction's status in https://bscscan.com/tx/{TX_HASH}

## How is this app secure?
(1) When this application run on your laptop, all keys are only stored and used in your local machine.

(2) This is open source, so you can review this code by any Python Developer.

# Contribution
- If you have any idea, you can submit here: https://forms.gle/LaHKXMhRxv4WPXfF7

- Only donate if you maked profit with our tool. We will use this donation to keep developing awesome tools.
DONATE ADDRESS: `0xc77a3a0c7F1d4e641D96013ad323539176c1FaFA`


`SUPPORT INSTALLATION VIA TEAMVIEWER OR STEP BY STEP FOR ANY DONATOR`

After donated, you can contact our support via Telegram: https://t.me/greenmancoin 
