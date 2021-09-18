package problems_java;

public class leetCode5 {

    public static String longestPalindrome(String s){
         
        int[] result1 = new int[2];
        int[] result2 = new int[2];
        int start = 0 ;
        int end  = 0 ;

        for (int i = 0 ; i < s.length(); i ++){
            result1 = expand(s,i,i);
            result2 = expand(s,i,i+ 1);
            if(result1[1] - result1[0] >(end - start)){
                end = result1[1];
                start = result1[0];
            }
            if (result2[1] - result2[0] > (end - start)){
                end = result2[1];
                start = result2[0];
            }
        }
        return s.substring(start, end + 1);
    }

    public static int[] expand(String s , int left, int right){
        int[] result = new int[2];
        while ( left >=0 && right < s.length()){
            if(s.charAt(left) == s.charAt(right)){
                left -= 1;
                right += 1;
             }
             else{
                 break;
             }
        }
        result[0] = left + 1;
        result[1] = right - 1;
        return result;
    }
    public static void main(String[] args){
        String s = "babab";
        System.out.println(longestPalindrome(s));
        String s1 = "ababad";
        System.out.println(longestPalindrome(s1));

    }
}
