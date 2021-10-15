class Solution {
public:
    bool hasCycle(ListNode *head) {
      unordered_map<ListNode*,int> map;
      ListNode* temp = head;
      while(temp){
        if(map.find(temp) != map.end())
          return true;
        else 
          map[temp] = temp->val;
        temp =temp->next;
      }
      return false;
    }
};