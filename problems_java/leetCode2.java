package problems_java;

import java.util.HashMap;
import java.util.Map;

public class leetCode2 {
    public static int[] twoSum(int[] nums,int target){
        int[] res = new int[2];
        if(nums == null || nums.length == 0){
            return res;
        }
        Map<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i ++){
            int temp = target - nums[i];
            if( map.containsKey(temp)){
                res[1] = i;
                res[0] = map.get(temp);
            }
            map.put(nums[i], i);
            
        }
        return res;
    }
    public static void main(String[] args){
        int[] nums = {2,5,11,7};
        int target = 9;
        int[] result = twoSum(nums,target);

        System.out.println("the result is " + result[0] + " " + result[1]);
    }
}
