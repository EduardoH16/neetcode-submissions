class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1. Count frequencies
    unordered_map<int, int> counts;
    for (int num : nums) {
        counts[num]++;
    }

    // 2. Use a min-heap to keep track of top k elements
    // Min-heap of pairs: {frequency, element}
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

    for (auto const& [val, freq] : counts) {
        minHeap.push({freq, val});
        if (minHeap.size() > k) {
            minHeap.pop(); // Remove the least frequent among the top k+1
        }
    }

    // 3. Extract elements from heap
    vector<int> result;
    while (!minHeap.empty()) {
        result.push_back(minHeap.top().second);
        minHeap.pop();
    }
    return result;
    }
};
