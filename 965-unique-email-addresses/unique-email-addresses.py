class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = Counter()
        for mail in emails:
            local, domain = mail.split("@")
            local = local.replace(".", "")
            if "+" in local:
                local = local[:local.index("+")]
            d[local + "@" + domain] += 1
        print(d)
        return len(d)