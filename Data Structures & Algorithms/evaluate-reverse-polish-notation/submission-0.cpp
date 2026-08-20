class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> values;
        unordered_set<string> operators = {"+", "-", "*", "/"};

        for (const string& token : tokens) {
            if (operators.find(token) == operators.end()) {
                values.push(stoi(token));
            } else {
                int right = values.top();
                values.pop();

                int left = values.top();
                values.pop();

                if (token == "+") {
                    values.push(left + right);
                } else if (token == "-") {
                    values.push(left - right);
                } else if (token == "*") {
                    values.push(left * right);
                } else {
                    values.push(left / right);
                }
            }
        }

        return values.top();
    }
};
