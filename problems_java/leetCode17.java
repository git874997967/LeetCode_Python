package problems_java;

import java.util.ArrayList;

public class leetCode17 {

    static ArrayList<String> list = new ArrayList<String>();
    static StringBuilder temp = new StringBuilder();

    public static ArrayList<String> letterCombinations(String digits){
        if(digits == null || digits.length() == 0){
            return list;
        }
        String[] numString = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        backTracking(digits,numString,0);
        return list;
    }
    public static void backTracking(String digits, String[] numString, int startIndex){
        if(startIndex == digits.length()){
            list.add(temp.toString());
            return;
        }
        String str = numString[digits.charAt(startIndex) - '0'];
        for ( int i = 0 ; i < str.length(); i ++){
                temp.append(str.charAt(i));
                backTracking(digits, numString, startIndex + 1);
                temp.deleteCharAt(temp.length() - 1);
        }

    }
    public static void main(String[] args){

    }
    
}
