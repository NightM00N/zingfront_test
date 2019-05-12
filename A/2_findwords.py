# -*- coding:utf-8 -*-

'''
@author: zjm
@file: 2_findwords.py
@time: 2019/5/11 19:33
@desc: 查找字符问题,深度查找字典树
'''
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie:
    # 前缀树，利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # 单词插入树
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        # 判断是否有以prefix开头的单词
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return False
        return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        :desc: 查找符合的单词
        """
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for w in words:
            trie.insert(w)
        ans = []
        for i in range(m):
            for j in range(n):
                tmp = [[0 for q in range(n)] for q in range(m)]
                str = board[i][j]
                self.findWord(i, j, trie, board, tmp, str, ans)
        return ans

    def findWord(self, i, j, trie, board, tmp, str, ans):
        """
        :type i: num
        :type j: num
        :type trie: class Trie
        :type board: List[List[str]]
        :type tmp: List[List[num]]
        :type str: str
        :type ans: List[str]
        :desc: 查找符合的单词
        """
        m = len(board)
        n = len(board[0])
        tmp[i][j] = 1
        if trie.startsWith(str) == False:  # 判断是否有以str开头的单词，没有则直接返回
            tmp[i][j] = 0
            return
        if trie.search(str) and str not in ans:
            ans.append(str)
        if i > 0 and tmp[i - 1][j] == 0:  # 左
            self.findWord(i - 1, j, trie, board, tmp, str + board[i - 1][j], ans)
            if j > 0 and tmp[i - 1][j - 1] == 0:  # 左 上
                self.findWord(i - 1, j - 1, trie, board, tmp, str + board[i - 1][j - 1], ans)
        if j > 0 and tmp[i][j - 1] == 0:  # 上
            self.findWord(i, j - 1, trie, board, tmp, str + board[i][j - 1], ans)
            if i < m - 1 and tmp[i + 1][j - 1] == 0:  # 上 右
                self.findWord(i + 1, j - 1, trie, board, tmp, str + board[i + 1][j - 1], ans)
        if i < m - 1 and tmp[i + 1][j] == 0:  # 右
            self.findWord(i + 1, j, trie, board, tmp, str + board[i + 1][j], ans)
            if j < n - 1 and tmp[i + 1][j + 1] == 0:  # 右 下
                self.findWord(i + 1, j + 1, trie, board, tmp, str + board[i + 1][j + 1], ans)
        if j < n - 1 and tmp[i][j + 1] == 0:  # 下
            self.findWord(i, j + 1, trie, board, tmp, str + board[i][j + 1], ans)
            if i > 0 and tmp[i - 1][j + 1] == 0:  # 下 左
                self.findWord(i - 1, j + 1, trie, board, tmp, str + board[i - 1][j + 1], ans)
        tmp[i][j] = 0

if __name__ == '__main__':
    targets = ["ARE", "PENPIEAPPLE", "APPLEPEN", "APPLE",
               "LIPS", "RED", "AIR", "PLEASE"]

    letters = [['A', 'R', 'E'],
               ['I', 'P', 'D'],
               ['E', 'L', 'P']]

    print(Solution().findWords(board=letters, words=targets))
    # ['AIR', 'APPLE', 'ARE', 'RED']


# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n)