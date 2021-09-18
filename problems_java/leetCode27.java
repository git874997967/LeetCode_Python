package problems_java;

import java.util.Arrays;

public class leetCode27 {
    public static int[] removeDup(int[] nums, int target){
        int i = 0;
        for ( int j = 0 ; j < nums.length; j ++){
            if( nums[j] == target){
                continue;
            }
            else{
                nums[i] = nums[j];
                i += 1;
            }
        }
        return Arrays.copyOfRange(nums,0, i);
    }
    public static void main(String[] args){
        int[] nums = new int[]{0,1,2,2,3,0,4,2};
        int[] result = removeDup(nums, 2);
        for(int i :result){
            System.out.println(i);
        }
    }
}
