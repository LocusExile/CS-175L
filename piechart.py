import matplotlib.pyplot as plt

def main():
    filename = "expenses.txt"
    slicelabels, sliceprices = read_file()
    plot_expenses(slicelabels, sliceprices)

def read_file():
    slicelabels = []
    sliceprices = []
    try:
        with open('expenses.txt', 'r') as infile:
            for line in infile:
                expense, price = line.strip().split('\t')
                try:
                    price = int(price)
                    slicelabels.append(expense)
                    sliceprices.append(price)
                except ValueError as baddata:
                    print(baddata)
    except IOError as bad:
        print("bad input")

    return slicelabels, sliceprices

def plot_expenses(slice_labels, slice_prices):
    plt.pie(slice_prices, labels=slice_labels)
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == "__main__":
    main()
