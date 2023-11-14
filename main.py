from other import LinkedList, Node
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size=10):
        self.array = [None] * size
        self.count = 0
        self.keys_list = LinkedList()

    def __str__(self):
        pairs = []
        node = self.keys_list.head
        while node:
            key = node.data
            value = self[key]
            pairs.append(f"'{key}' : {value}")
            node = node.next
        return "{" + ", ".join(pairs) + "}"

    def __setitem__(self, key, value):
        index = self._hash(key)
        pair = Pair(key, value)
        if self.array[index] is None:
            self.array[index] = LinkedList()
        self.array[index].append(pair)
        self.keys_list.append(key)
        self.count += 1

    def __getitem__(self, key):
        index = self._hash(key)
        if self.array[index] is None:
            raise KeyError(f"'{key}'")
        node = self.array[index].head
        while node:
            if node.data.key == key:
                return node.data.value
            node = node.next
        raise KeyError(f"'{key}'")

    def _hash(self, key):
        return hash(key) % len(self.array)

    def pop(self, key):
        index = self._hash(key)
        if self.array[index] is None:
            raise KeyError(f"'{key}'")
        node = self.array[index].head
        prev = None
        while node:
            if node.data.key == key:
                value = node.data.value
                if prev:
                    prev.next = node.next
                else:
                    self.array[index].head = node.next
                self.keys_list.remove(key)
                self.count -= 1
                return value
            prev = node
            node = node.next
        raise KeyError(f"'{key}'")

    def keys(self):
        return self.keys_list
def romanToInt(romNum: str):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0

    for char in romNum[::-1]:
        value = roman_numerals[char]

        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
def rareWord(s: str) -> str:
    '''
    Принимает на вход строку и выводит слово, которое встречается во фразе реже всего.
    Если редких слов несколько, нужно вывести то, которое меньше в лексикографическом порядке.
    Регистр слов не учитывается (приводите к нижнему), знаки препинания в предложениях игнорируются.
    >>> rareWord('aa, bb, AA, BB')
    'aa'
    >>> rareWord('bb, ccc, a, DDDD')
    'a'
    '''
    import re

    words = re.findall(r'\b\w+\b', s.lower())
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    min_count = min(word_counts.values())
    rarest_words = [word for word, count in word_counts.items() if count == min_count]
    rarest_words.sort()

    return rarest_words[0]
ht1 = HashTable()
ht1['key2'] = 10
ht1['key1'] = 5
ht1['key1']
