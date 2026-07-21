class MyHashMap(object):

    def __init__(self):
        self.data = [[] for _ in range(1000)]

    def _bucket(self, key):
        return self.data[key % 1000]    
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return    
        bucket.append([key, value])
              
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1    
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)