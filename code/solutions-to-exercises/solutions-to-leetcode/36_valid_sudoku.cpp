class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, bool> num_mapper;
        // line
        for(vector<char> v: board){
            num_mapper.clear();
            for(char c: v){
                if(c != '.'){
                    if(num_mapper.count(c) > 0){
                        return false;
                    }else{
                        num_mapper[c] = true; 
                    }
                }
            }
        }

        // row;
        for(int r = 0; r < 9; ++r){
            num_mapper.clear();
            for(int l = 0; l < 9; ++l){
                char c = board[l][r];
                if(c != '.'){
                    if(num_mapper.count(c) > 0){
                        return false;
                    }else{
                        num_mapper[c] = true; 
                    }
                }
            }
        }

        // box
        for(int i=0; i<9; i+=3){
            for(int j=0; j<9; j+=3){
                num_mapper.clear();
                for(int x = i; x<i+3;++x){
                    for(int y = j; y<j+3; ++y){
                        char c = board[x][y];
                        if(c != '.'){
                            if(num_mapper.count(c) > 0){
                                return false;
                            }else{
                                num_mapper[c] = true; 
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
};