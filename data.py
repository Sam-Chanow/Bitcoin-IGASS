####COMPILES AND PROVIDES ACCESS TO DATASETS IN /COMPILED-DATASETS####
####SAM CHANOW####

import sys
import pandas
from datetime import date, timedelta


def read_posts_from_day(filename, day):  # day is a string in form 'YYYY-MM-DD
    # Return list of posts from a single day
    posts = []
    with open(filename, 'r') as fp:
        ln = 0
        post = ""
        last_line = ""
        curr_date = ""
        for line in fp:
            if line == "\n": continue  # jump past empty lines
            if (ln == 0) or (last_line == "-------------------------------\n"):
                curr_date = line[-11:-1]
                if post != "":
                    posts.append(post)
                    post = ""
            elif (curr_date == day) and (line != "-------------------------------\n"):  # Gather data for this post
                line = line.strip()
                post += line
            ln += 1
            last_line = line
    return posts


def read_price_change_from_day(filename, day):  # day format is the same as above, expects csv file such as coin_Bitcoin.csv
    with open(filename, 'r') as fp:
        for line in fp:
            # element 6 is the open price and element 7 is the close price
            # element 3 is the date
            line_split = line.split(',')
            date = line_split[3][:10]
            if date == day:
                open_p = float(line_split[6])
                close_p = float(line_split[7])
                return close_p - open_p


def clean_post_data(post):  # post is a string of text
    post = post.lower().strip()
    post = post.replace('\n', "")
    return post


def group_posts_from_day(l_posts):  # Returns ls
    # a string that is the concatenation of all the posts from one day
    return ' /ENDPOST/ '.join(l_posts)  # join all the posts


def label_data(agg_post, price_change):  # label the aggregate post data with the price change from its day
    return ['UP' if price_change > 0 else 'DOWN', agg_post] # Label with up or down for price movement


def get_labeled_data_from_day(day):  # the public facing function that other files should access
    # This will access the compiled dataset not the raw dataset
    pass


if __name__ == "__main__":  # Simple main function, acts as a searching tool for r-cryptocurrency-posts
    # print(read_posts_from_day('data/raw-datasets/bitcoin-posts/r-bitcoin-posts.txt', '2021-10-24'))
    # print(read_price_change_from_day('data/raw-datasets/bitcoin-price/coin_Bitcoin.csv', '2020-10-24'))
    while True:
        if (len(sys.argv) > 1) and (sys.argv[1] == '-compile'): #this command will be used to build a compiled dataset
            print("WARNING THERE ARE NO SAFEGUARDS AGAINST OVERWRITING DATA OR INCORRECT DATES")
            data_file = input("File to build dataset in: ")
            begin_date = input("Begin date to build dataset with (YYYY-MM-DD): ")
            end_date = input("End date to build dataset with (YYYY-MM-DD) (Exclusionary): ")
            try:
                fp = open(data_file, 'w')
                # Get a list of dates in-between the start and end date
                dates = pandas.date_range(pandas.to_datetime(begin_date), pandas.to_datetime(end_date)-timedelta(days=1), freq='d')
                # print(dates)
                prev_posts = "" # since it is the posts in relation to the price change the next day
                for date in dates:
                    print(date)
                    date = str(date)[:10]
                    price_change = float(read_price_change_from_day('data/raw-datasets/bitcoin-price/coin_Bitcoin.csv', date))
                    bitcoin_l = read_posts_from_day('data/raw-datasets/bitcoin-posts/r-bitcoin-posts.txt', date)
                    crypto_l = []
                    fileN = -1
                    while crypto_l == []:
                        fileN += 1
                        if fileN > 2: break
                        crypto_l = read_posts_from_day('data/raw-datasets/cryptocurrency-posts/r-cryptocurrency-posts0' + str(fileN) + '.txt', date)

                    # Now we clean and aggregate the data
                    posts = bitcoin_l + crypto_l
                    posts = [clean_post_data(post) for post in posts]
                    posts = group_posts_from_day(posts)
                    labeled_data = label_data(prev_posts, price_change)
                    prev_posts = posts
                    # Using a unique separator here to make parsing easier as the text is plain text
                    if not labeled_data[1] == "":
                        fp.write(labeled_data[0] + ' //POSTDATACOMPILED// ' + labeled_data[1] + '\n')
                fp.close()
                exit(0)
            except FileNotFoundError:
                print("File is incorrect or does not exist...exiting...")
                exit(0)
        query = input("Search Date (YYYY-MM-DD): ")
        if query == 'quit': exit(0)
        fileN = -1
        results = []
        try:
            while results == []:
                if len(sys.argv) == 1:
                    print("Incorrect command, must be used as 'python3 data.py -<price | post>")
                    exit(0)
                if sys.argv[1] == '-post':
                    fileN += 1
                    results = read_posts_from_day('data/raw-datasets/cryptocurrency-posts/r-cryptocurrency-posts0' + str(fileN) + '.txt', query)
                    results = [clean_post_data(post) for post in results]
                elif sys.argv[1] == '-price':
                    results = [str(read_price_change_from_day('data/raw-datasets/bitcoin-price/coin_Bitcoin.csv', query))]
                else:
                    print("The option -" + sys.argv[1] + " is not valid, only -post and -price can be queried.")
                    exit(0)
        except FileNotFoundError:
            print("The data for that date is not contained in this dataset.")
        print('\n\n'.join(results))
