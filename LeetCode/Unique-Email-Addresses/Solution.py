1class Solution:
2    def numUniqueEmails(self, emails: List[str]) -> int:
3        d = Counter()
4        for mail in emails:
5            local, domain = mail.split("@")
6            local = local.replace(".", "")
7            if "+" in local:
8                local = local[:local.index("+")]
9            d[local + "@" + domain] += 1
10        print(d)
11        return len(d)