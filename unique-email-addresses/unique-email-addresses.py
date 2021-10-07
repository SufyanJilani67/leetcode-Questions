class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output=set()
        for email in emails:
            local,domain = email.split("@")
            temp= ""
            for i in local:
                if i == ".":
                    continue
                elif i == "+":
                    break
                else:
                    temp += i
            output.add(temp + "@" + domain)
        return len(output)