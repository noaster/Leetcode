struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
     
        ListNode* res = new ListNode(0);
        ListNode* prev = res;
        int carriage = 0;
        
        while(true)
        {
            carriage = linkAddTwoNumbers(prev, l1, l2);
            l1 = l1 != nullptr ? l1->next : nullptr;
            l2 = l2 != nullptr ? l2->next : nullptr;
            if (l1 != nullptr || l2 != nullptr || carriage != 0)
            {
                prev->next = new ListNode(carriage);
                prev = prev->next;
            }
            else
            {
                break;
            }
        }
        
        return res;
    }

    int linkAddTwoNumbers(ListNode* res, ListNode* l1, ListNode* l2)
    {
        int sum = res->val;
        if (l1 != nullptr)
        {
            sum += l1->val;
        }
        if (l2 != nullptr)
        {
            sum += l2->val;
        }
        
        res->val = sum % 10;
        
        return sum / 10;
    }
};