# When a share of common stock of some company is sold, the capital gain (or, sometimes, loss) is the difference between the share's selling price and the price originally paid to buy it. This rule is easy to understand for a single share, but if we sell multiple shares of tock bought over a long period of time, then we must identify the shares actually being sold. A standard accounting principle for identifying whch shares of a stock were sold in such a case is to use a FIFO protocol - the shares sold are the ones that have been held the longest (indeed, this is the default method built into several personal finance software packages). For example, suppose we buy 100 shares at $20 each on day 1, 20 shares at $24 on day 2, 200 shares at $36 on day 3, and then sell 150 shares on day 4 at $30 each. Then applying the FIFO protocol means that of the 150 shares sold, 100 where bought on day1, 20 where bought on day 2, and 30 where bought on day 3. The capital gain in this case would therefore be 100 * 10 + 20 * 6 + 30 * (-6), or $940. Write a program that takes as input a sequence of transactions of the form "buy x share(s) at $y each" or "sell x share(s) at $y each", assuming that the transactions occur on consecutive days and the values x and y are integers. Given this input sequence, the output should be the total capital gain (or loss) for the intire sequence, using the FIFO protocol to identify shares.


def IdentifyShare(seq, Nums=[], Prices=[], Out=[]):
    for i in range(len(seq)):
        transact = seq[i].split(" ")
        action = transact[0]
        num = int(transact[1])
        price = int(transact[4][1:])
        if action == "buy":
            Nums.append(num)
            Prices.append(price)
        elif action == "sell":
            if num > sum(Nums):
                raise ValueError("Not enough stock to sell.")
            else:
                for n in range(len(Nums)):
                    benefit = price - Prices[n]
                    if Nums[n] < num:
                        Out.append(Nums[n]*benefit)
                        num = num - Nums[n]
                    else:
                        Out.append(num*benefit)
                        Nums[0] = Nums[n]-num

    return sum(Out)

if __name__ in "__main__":
    seq = ["buy 100 shares at $20 each",
            "buy 20 shares at $24 each",
            "buy 200 shares at $36 each",
            "sell 150 shares at $30 each",
            "buy 100 shares at $30 each",
            "sell 250 shares at $23 each"]
    print(IdentifyShare(seq))
