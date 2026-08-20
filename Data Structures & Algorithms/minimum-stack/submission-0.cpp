class MinStack {
private:
    struct Node {
        int val;
        int minVal; 
        Node* next;

        Node(int v, int minV) {
            val = v;
            minVal = minV;
            next = nullptr;
        }
    };

    Node* head; 

public:
    MinStack() {
        head = nullptr;
    }
    
    void push(int val) {
        if (head == nullptr) {
            head = new Node(val, val); }
            else {
                int currentMin = std::min(val, head->minVal);
                Node* newNode = new Node(val, currentMin);
                newNode->next = head;
                head = newNode;
            }
    }
    
    void pop() {
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    
    int top() {
        return head->val;
    }
    
    int getMin() {
        return head->minVal;
    }
};
