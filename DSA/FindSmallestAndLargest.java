import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FindSmallestAndLargest {
    public static void main(String[] args){
        //System.out.println(getSmallestAndLargest(new int[]{1, 8, 2, 3}));
        getSmallestAndLargest2(new int[]{8, 5, 10, 3});
    }

    public static List<Integer> getSmallestAndLargest(int[] intArr){
        List<Integer> intArrList = new ArrayList<>();
        List<Integer> smallestLargest = new ArrayList<>();
        for(int num: intArr){
            intArrList.add(num);
        }
        Collections.sort(intArrList);
        smallestLargest.add(intArrList.get(0));
        smallestLargest.add(intArrList.get(intArrList.size() - 1));
        return smallestLargest;
    }

    // without using any libraries
    public static void getSmallestAndLargest2(int[] intArr){
        int smallest = intArr[0];
        int largest = intArr[0];

        for(int num: intArr){
            if(num > largest){
                largest = num;
            }
            else if (num < smallest){
                smallest = num;
            }
        }

        System.out.println("Smallest: " + smallest);
        System.out.println("Largest: " + largest);
    }
}
