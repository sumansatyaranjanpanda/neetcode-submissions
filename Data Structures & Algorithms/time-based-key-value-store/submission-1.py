class TimeMap:

    def __init__(self):
        self.map={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key]=[]
        self.map[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""

        arr=self.map[key]

        l=0
        r=len(arr)-1

        ans=""


        while l<=r:
            mid=l+(r-l)//2

            if arr[mid][0]<=timestamp:
                ans=arr[mid][1]
                l=mid+1
            else:
                r=mid-1
        
        return ans


        
