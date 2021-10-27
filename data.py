####COMPILES AND PROVIDES ACCESS TO DATASETS IN /COMPILED-DATASETS####
####SAM CHANOW####

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


def read_price_change_from_day(filename, day):  # day format is the same as above
    pass


def group_posts_from_day(l_posts):  # Returns a string that is the concatenation of all the posts from one day
    return ' /END_OF_POST '.join(l_posts)  # specialized token meaning end of post


def label_data(agg_post, price_change):  # label the aggregate post data with the price change from its day
    pass


def get_labeled_data_from_day(day):  # the public facing function that other files should access
    pass


if __name__ == "__main__":  # Simple main function, acts as a searching tool for r-cryptocurrency-posts
    # print(read_posts_from_day('data/raw-datasets/bitcoin-posts/r-bitcoin-posts.txt', '2021-10-24'))
    while True:
        query = input("Search Date (YYYY-MM-DD): ")
        if query == 'quit': exit(0)
        fileN = -1
        results = []
        try:
            while results == []:
                fileN += 1
                results = read_posts_from_day('data/raw-datasets/cryptocurrency-posts/r-cryptocurrency-posts0' + str(fileN) + '.txt', query)
        except FileNotFoundError:
            print("The data for that date is not contained in this dataset.")
        print('\n\n'.join(results))
