class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        record=dict()
        for j in strs:
            key = ''.join(sorted(j))
            if key not in record:
                record[key]=[j]
            else:
                record[key].append(j)
        return list(record.values())
        
        