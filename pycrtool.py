import math
import random
import subprocess
import threading
import re
import uuid
import sqlite3
import requests
from bs4 import BeautifulSoup

class run_command:
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
        self.output = []
        self.last_index = 0
        self._start_reading()

    def _start_reading(self):
        def read_output(pipe, output_list):
            for line in iter(pipe.readline, ''):
                output_list.append(line.strip())
            pipe.close()

        self.stdout_thread = threading.Thread(target=read_output, args=(self.process.stdout, self.output))
        self.stderr_thread = threading.Thread(target=read_output, args=(self.process.stderr, self.output))
        
        self.stdout_thread.start()
        self.stderr_thread.start()

    def get_part(self):
        current_output = self.output[self.last_index:]
        self.last_index = len(self.output)
        return "\n".join(current_output)

    def get_con(self):
        return self.process.poll() is not None

    def get_all(self):
        return "\n".join(self.output)

class modern_replace:
    def dict_replace(text,replacements,regex=False):
        if regex:
            for old, new in replacements.items():
                text = re.sub(old, new, text)
            return text
        else:
            for old, new in replacements.items():
                text = text.replace(old, new)
            return text

    def cross_replace(text, a, b):
        while True:
            temp = str(uuid.uuid4())
            if temp not in text:
                break
        return text.replace(a, temp).replace(b, a).replace(temp, b)
    
    def count_replace(text,a,b,count=-1):
        if count == -1:
            while a in text:
                text = text.replace(a,b)
        elif count < -1:
            return ""
        else:
            for i in range(count):
                text = text.replace(a,b)
        return text

class modern_str:
    def add_text(text,text_len,add_str=" "):
        if len(text) >= text_len:
            return text
        remaining_length = text_len - len(text)
        new_text = text + (add_str * (remaining_length // len(add_str))) + add_str[:remaining_length % len(add_str)]
        return new_text

class simple_sqlite3:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join([f"{col} {typ}" for col, typ in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});"
        self.cursor.execute(query)
        self.conn.commit()

    def insert(self, table_name, data):
        columns = ', '.join(data.keys())
        values = ', '.join(['?' for _ in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def select(self, table_name, columns='*', condition=None):
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, data, condition):
        set_str = ', '.join([f"{col} = ?" for col in data.keys()])
        query = f"UPDATE {table_name} SET {set_str} WHERE {condition};"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition};"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()

class sort:
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sort.quick_sort(left) + middle + sort.quick_sort(right)

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort.merge_sort(arr[:mid])
        right = sort.merge_sort(arr[mid:])
        return sort.merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            sort.heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            sort.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            sort.heapify(arr, i, 0)
        return arr

    def counting_sort(arr):
        max_val = max(arr)
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        result = []
        for i in range(len(count)):
            result.extend([i] * count[i])
        return result

    def bucket_sort(arr):
        if len(arr) == 0:
            return arr
        min_val, max_val = min(arr), max(arr)
        bucket_count = len(arr)
        bucket_range = (max_val - min_val) / bucket_count
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            index = int((num - min_val) / bucket_range)
            if index == bucket_count:
                index -= 1
            buckets[index].append(num)
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(sorted(bucket))
        return sorted_arr

    def monkey_sort(arr):
        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        while not is_sorted(arr):
            random.shuffle(arr)
        return arr

class suan:
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def pythagoras(a=None, b=None, c=None):
        if a is not None and b is not None:
            c = math.sqrt(a**2 + b**2)
            return c
        elif a is not None and c is not None:
            b = math.sqrt(c**2 - a**2)
            return b
        elif b is not None and c is not None:
            a = math.sqrt(c**2 - b**2)
            return a
        else:
            return 0

class crawl:
    def bing_search(query,url_start="https://www.bing.com/search?q=",url_end=""):
        url = f"{url_start}{query}{url_end}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.find_all('h2'):
            title_tag = item.find('a')
            if title_tag:
                title = title_tag.get_text()
                link = title_tag['href']
                text_tag = item.find_next('p')
                text = text_tag.get_text() if text_tag else ''
                results.append([title, link, text])
        return results