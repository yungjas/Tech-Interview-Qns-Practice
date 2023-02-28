import java.util.*;

public class Palindrome {
    public static void main(String[] args){
        System.out.println(checkPalindrome("madam", "madam"));
        System.out.println(checkPalindrome("apple", "madam"));
    }

    public static boolean checkPalindrome(String inputStr1, String inputStr2){
        ArrayList<Character> charArrList1 = new ArrayList<>();
        ArrayList<Character> charArrList2 = new ArrayList<>();

        for(int i = 0; i < inputStr1.length(); i++){
            charArrList1.add(inputStr1.charAt(i));
        }
        
        for(int i = inputStr2.length() - 1; i >= 0; i--){
            charArrList2.add(inputStr2.charAt(i));
        }

        if(charArrList1.equals(charArrList2)){
            return true;
        }
        return false;
    }
}
