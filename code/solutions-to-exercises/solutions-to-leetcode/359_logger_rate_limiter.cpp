class Logger {
    unordered_map<string, int> loginfo;
public:
    /** Initialize your data structure here. */
    Logger() {
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if(loginfo.count(message) > 0 && loginfo[message] + 10 > timestamp){
            return false;
        }else{
            loginfo[message] = timestamp;
            return true;
        }
    }
};
