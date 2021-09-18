package problems_java;

import java.util.ArrayList;
import java.util.Arrays;

public class leetCode18 {
    public List<List<Integer>> fourSum(int[] nums, int target){
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for ( int i =  0 ; i < nums.length; i++){
            if (i > 0 && nums[i] == nums[i - 1]){
                continue;
            }
            for (int j = i + 1; j < nums.length; j ++){
                if(j > i+1  && nums[j] == nums[j-1]){
                    continue;
                }
                int left = j + 1;
                int right = nums.length - 1;
                while (right > left){
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum > target ){
                        right -= 1;
                    }
                    else if (sum < 0 ){
                        left += 1;
                    }
                    else{
                        result.append(Arrays.asList([nums[i],nums[j],nums[left],nums[right]));
                        while(left < right && nums[left] == nums[left + 1]){
                            left += 1;
                        }
                        while(left < right && nums[right] == nums[right-1]){
                            right -= 1;
                        }
                        left += 1;
                        right -= 1;

                    }
                }
            }
        }
        return result;
    }
    public static void main(String[] args){
    }
}
