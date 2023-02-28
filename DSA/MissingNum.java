import java.util.Arrays;

public class MissingNum {
    public static void main(String[] args){
        findMissingNum(new int[] {1, 3, 4, 5});
        findMissingNum(new int[] {1, 3, 5, 7, 9, 10});
        findMissingNum(new int[] {1, 3, 5, 7, 10, 9});
    }

    public static void findMissingNum(int nums[]){
        Arrays.sort(nums);

        for(int i = 0; i < nums.length; i++){
            int nextIdx = 0;
            if(i < nums.length - 1){
                nextIdx = i + 1;
            }
            if(nums[nextIdx] - nums[i] > 1){
                System.out.println(nums[nextIdx] - 1);
            }
        }
        System.out.println();
    }
}
