from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key:Any, value:Any, next:Node) -> None:
        self.key = key      # 키(임의의 자료형)
        self.value = value  # 값(임의의 자료형)
        self.next = next    # 뒤쪽 노드를 참조(Node형)
        
class ChainedHash:
    def __init__(self, capacity:int) -> None:
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)을 선언

    def hash_value(self, key:Any) -> int:
        ''' 해시값을 구함 '''
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key:Any) -> Any:
        hash = self.hash_value(key)     # 검색하는 키의 해시값
        p = self.table[hash]            # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value
            
        return None                     # 검색 실패

    def add(self, key:Any, value:Any) -> bool:
        hash = self.hash_value(key)     # 추가하는 key의 해시값
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False            # 추가 실패
            p = p.next                  # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
        
    def remove(self, key:Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    # 해시 테이블을 덤프 : 해시 테이블의 내용을 한꺼번에 출력
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()