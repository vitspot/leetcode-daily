```python
class Interval(NamedTuple):
    start: int
    end: int
    
    def __str__(self) -> str:
        if self.start == self.end:
            return str(self.start)
        else:
            return f"{self.start}->{self.end}"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        return list(map(str, self.range_iterator(nums)))
    
    def range_iterator(self, nums: List[int]) -> Iterable[Interval]:
        start = end = -inf
        for n in nums:
            if end < n-1:
                if end > -inf:
                    yield Interval(start, end)
                start = end = n
            end = n
        if end > -inf: yield Interval(start, end)
```