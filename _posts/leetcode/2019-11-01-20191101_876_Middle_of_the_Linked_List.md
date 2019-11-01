---
category: Leetcode
---

1. 문제 분석
  - list의 중가 노드르 반환하라
  - 최대 길이는 100
  - 가운데가 두개인 경우 두 번째 노드를 반환 --> 리스트의 길이가 짝수인 경우 가운데 있는 노드들 중 더 나중에 나오는 노드 반환
  - 풀이방법: 리스트 순회를 포인터 두 개로 하여 하나는 노드를 1step씩 진행하고 다른 하나는 2step씩 진행. 2step씩 진행하는 포인터가 끝에 도달하면 다른 포인터를 반환한다.
    * last->next == null이면 first_pointer를 return하고 last->next->next == null이며 first_pointer->next를 return한다.
2. Prerequisite
  - None?
3. 주의사항 Or 고려 사항
  - Null node에 대한 접근 주의
  - 짝수개인 리스트의 중간 노드 계산 주의
4. 결과
55.22%인데... 4ms라 고쳐볼 생각 없음. 아마 second를 두 번에 나눠 움직이는 걸 한방에 움직이면 될 것 같지만, 귀찮음.

```
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *first = head;
        ListNode *second = head;
        while( first && second ) {
            if( !second -> next )
                return first;
            first = first->next;
            second = second->next;
            if( !second -> next )
                return first;
            second = second->next;
        }
        return first;
    }
};
```
