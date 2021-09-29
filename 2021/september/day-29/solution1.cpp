class Solution {
public:
 
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        
      
        ListNode* ptr = head;
        int siz =0;
        while(ptr){
            siz++; ptr = ptr->next;
        }
        
        int sizeinPart = siz / k, extrapart = siz % k;
         ListNode *temp =NULL;
        vector<ListNode*> result(k);
        
        for(int i=0; i<k; i++){
            result[i]= head;
            for(int j =0; j< sizeinPart + (i < extrapart); j++){
                temp = head;
                head =head->next;
            }
            if(temp) temp->next = NULL;
        }
        return result;
        
    }
};