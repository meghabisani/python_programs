import csv

# Global Variable Declaration
initial_time = 0
total_profit = 0


# Calculate the profit
def calc_profit(data_lst):

    # Variable declaration
    min_data = []
    max_data = []
    global initial_time
    global total_profit

    # Condition to check if the list is empty then only proceed otherwise exit the loop
    if data_lst != []:

        # Check for the the minimum price to open the trade within 40 mins
        for row in data_lst:

            if int(row[0]) <= initial_time + 40:
                 min_data.append(row)

        min_time, min_price = min(min_data, key=lambda item: item[1])
        initial_time = int(min_time)

        # Check the maximum price to close the trade mist be open for minimum 30 mins
        # and close before 60 mins with max profit
        for row in data_lst:

            if (int(row[0]) > initial_time + 30) and (int(row[0]) < initial_time + 60):
                max_data.append(row)

        if max_data != []:

            max_time, max_price = max(max_data, key=lambda item: item[1])
            index = data_lst.index(max(max_data, key=lambda item: item[1]))

            initial_time = int(max_time)

            # Calculate the trade profit and total profit
            profit = float(max_price) - float(min_price)
            total_profit += profit

            # Print Trade Result on Console
            print("Open at " + min_time + "(" + min_price + "), close "\
                + max_time + "(" + max_price + ") for profit " + ("%.3f" % profit))

            return calc_profit(data_lst[index+1:])
    else:
        return []


# Main Function: Populate CSV Data into List of Tuples, remove the header
# and then call the function to calculate the profit
def main():
    # Input file should be in the same folder structure wrt. to the relative path from where
    # this script is being executed
    contents = [tuple(row) for row in csv.reader(open('stock_data/new_data.csv', 'rU'))]
    contents.pop(0)
    calc_profit(contents)
    print("Total profit: %.3f" % total_profit)


main()