class Twitter:

    def __init__(self):

        # maybe its best to implement as a set

        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

        # each user should have their own queue
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        # probably tuples

        # case 1: the 

        max_time = self.time * -1


        tweet_info = (max_time, tweetId)

        heapq.heappush(self.tweets[userId],tweet_info)
        heapq.heapify(self.tweets[userId])

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        # do a max heap, its asking for biggest to smallest

        NewsFeed = []

        for tweet in self.tweets[userId]:
            NewsFeed.append(tweet)

        for follower in self.followers[userId]:      
            for tweet in self.tweets[follower]:
                NewsFeed.append(tweet)

        heapq.heapify(NewsFeed)

        new_News = []

        for i in range(len(NewsFeed)):
            add_tweet = heapq.heappop(NewsFeed)
            if len(new_News) == 10:
                break
            new_News.append(add_tweet[1])

        return new_News

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
