class Solution {
public:
    //implementation of Jarvis Convex Hull Algorithm
    int orientation(vector<int> A, vector<int> B, vector<int> C) {
        //Subtraction of slopes for orientation.
        return ((B[0] - A[0]) * (C[1] - A[1])) - ((B[1] - A[1]) * (C[0] - A[0]));
    }
    
    
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        //no need to check fence for 3 or less points.
        if (trees.size() <= 3) return trees;
        //sorting so points sorted from Leftmost to Rightmost
        sort(trees.begin(), trees.end());
		// Upper HULL construction
        //left most points
        vector<vector<int>> left;
        left.push_back(trees[0]);
        left.push_back(trees[1]);
        //first two points initialised iterate through rest of the points
        for (int i = 2; i < trees.size(); i++) {
            //initialise size 
            int ls = left.size();
            while (left.size() >= 2 && orientation(left[ls-2], left[ls-1], trees[i]) > 0) {
                left.pop_back();
                ls--;
            }
            left.push_back(trees[i]);
        }
		// Lower HULL construction
        //Right most points
        vector<vector<int>> right;
        right.push_back(trees[trees.size() - 1]);
        right.push_back(trees[trees.size() - 2]);
        //first two points initialised iterate through rest of the points
        for (int i = trees.size() - 3; i >= 0; --i) {
            int rs = right.size(); 
            while (right.size() >= 2 && orientation(right[rs-2], right[rs-1], trees[i]) > 0) {
                right.pop_back();
                rs--;
            }
            right.push_back(trees[i]);
        }
		// Last point is common in both
        left.pop_back();
        right.pop_back();
        //merge vectors for answer
        for (int i = 0; i < right.size(); i++) {
            left.push_back(right[i]);
        }
		//Remove duplicates
        sort(left.begin(), left.end());
        left.erase(std::unique(left.begin(), left.end()), left.end());
        
        return left;
    }
};