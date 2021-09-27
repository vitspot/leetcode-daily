// by Siddheshwar


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        actual = set()
        for e in emails:
            local, domain = e.split('@')
            cur = ''
            for c in local:
                if c == '+':
                    break
                elif c == '.':
                    continue
                else:
                    cur += c
            actual.add(cur+"@"+domain)

        return len(actual)
