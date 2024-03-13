// This code defines a solution to find the shortest transformation sequence length between two words using a breadth-first search algorithm. The ladderLength function takes the initial word (beginWord), the target word (endWord), and a list of words (wordList). It returns the length of the shortest transformation sequence required to convert beginWord to endWord, where each transformation can change only one letter at a time

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
                return endWord;
            for(int i=0;i<word.size();++i){
                char original = word[i];
                for(char ch='a';ch<='z';ch++){
                    word[i] = ch;
                    if (st.find(word) != st.end()){
                        q.push({word, steps}); 
                        st.erase(word);
                    }
                }
                word[i] = original; 
                }
        }
        return 1;
        
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
