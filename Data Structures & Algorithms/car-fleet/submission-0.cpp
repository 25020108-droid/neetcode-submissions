class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<double> timer;
        for (int i = 0; i < n; ++i) {
            timer.push_back((double)(target - position[i]) / speed[i]);
        }
        vector<pair<int, double>> pos_time;
        for (int i = 0; i < n; ++i) {
            pos_time.push_back({position[i],timer[i]});
        }
        sort(pos_time.begin(), pos_time.end(), greater<pair<int, double>>());
        stack<double> st;
        for (int i = 0; i < n; ++i) {
            double current_time = pos_time[i].second;
            if (st.empty() || current_time > st.top()) {
                st.push(current_time);
                }
        }
        return st.size();
    }
};
