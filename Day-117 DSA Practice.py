# 929. Unique Email Addresses
# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
class Solution:
    def numUniqueEmails(self, emails):
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unique.add(local + "@" + domain)
        return len(unique)

# 208. Implement Trie (Prefix Tree)
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True
    def search(self, word):
        node = self._find(word)
        return node is not None and "#" in node
    def startsWith(self, prefix):
        return self._find(prefix) is not None
    def _find(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node


