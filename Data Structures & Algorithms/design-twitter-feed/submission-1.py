class Twitter:
    ##implement this first
    def __init__(self):
        self.time = 0
        self.tweets_map = {}
        self.following_map = {}
        
    #second
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_map:
            self.tweets_map[userId] = []
        self.tweets_map[userId].append([-self.time, tweetId])
        self.time += 1
   
    #last
    def getNewsFeed(self, userId: int) -> List[int]:
        s = set()
        result = []
        max_heap = []

        s.add(userId)
        if userId in self.following_map:
            for followee in self.following_map[userId]:
                s.add(followee)
        for person in s:
            if person in self.tweets_map and self.tweets_map[person]:
                index = len(self.tweets_map[person]) - 1
                time, tweet_id = self.tweets_map[person][index]
                heapq.heappush(
                    max_heap, [time, tweet_id, person, index]
                )
        heapq.heapify(max_heap)

        while max_heap and len(result) < 10:
            time, tweet_id, author, index = heapq.heappop(max_heap)
            result.append(tweet_id)

            if index > 0:
                index -= 1
                time, tweet_id = self.tweets_map[author][index]
                heapq.heappush(max_heap, [time, tweet_id, author, index])

        return result
        
        
    #follow and unfollow third
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_map:
            self.following_map[followerId] = set()
        self.following_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_map:
            self.following_map[followerId].discard(followeeId)
        
