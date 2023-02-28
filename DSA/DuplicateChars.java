import java.util.ArrayList;
import java.util.HashMap;

public class DuplicateChars{
    public static void main(String[] args){
        checkDuplicate("Programming");
        checkDuplicate("god");
        checkDuplicate("banana");
    }

    public static void checkDuplicate(String inputStr){
        HashMap<Character, Integer> charCount = new HashMap<>();
        
        for(int i = 0; i < inputStr.length(); i++){
            if(charCount.containsKey(inputStr.charAt(i))){
                charCount.put(inputStr.charAt(i), charCount.get(inputStr.charAt(i)) + 1);
            }
            else{
                charCount.put(inputStr.charAt(i), 1);
            }
        }

        for(Character c: charCount.keySet()){
            if(charCount.get(c) > 1){
                System.out.println(c);
            }
        }
        System.out.println();
    }
}