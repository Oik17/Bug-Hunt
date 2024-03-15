#include <iostream>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        unordered_set<string> st(wordList.begin(), wordList.end());
        st.erase(beginWord);
        while(!q.empty()){
            string word = q.front().first;
            int steps = q.front().second;
            q.pop();
            if(word == endWord)
                return steps;
            for(int i=0;i<word.size();i++){
                char original = word[i];
                for(char ch='a';ch<='z';ch++){
                    word[i] = ch;
                    if (st.find(word) != st.end()){
                        st.erase(word);
                        q.push({word, steps + 1});
                    }
                }
                word[i] = original;
            }
        }
        return 0;
    }
};

int main() {
    Solution solution;
    string beginWord = "hit";
    string endWord = "cog";
    vector<string> wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
    cout << "Shortest transformation sequence length: " << solution.ladderLength(beginWord, endWord, wordList) << endl;
    return 0;
}


//  if (st.find(word) != st.end()){
//                         // Logical Error 1: Not incrementing the steps correctly
//                         // q.push({word, steps}); // Incorrect: Does not increment steps
//                         q.push({word, steps + 1}); // Corrected: Increment steps properly
//                         st.erase(word);
//                     }
//                 }
//                 // Logical Error 2: Restoring original character incorrectly
//                 // word[i] = original; // Incorrect: Restores original character too early
//             }
//             word[i] = original; // Corrected: Restore original character after inner loop
//         }
//         // Logical Error 3: Incorrect return value (always returns 1)
//         // return 1; // Incorrect: Always returns 1
//         return -1; // Corrected: Return a negative value to indicate failure
