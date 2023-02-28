import java.util.Arrays;

// checking for full anagrams i.e. both strings need to have the same length
public class Anagram {
    public static void main(String[] args){
        checkAnagram("word", "wrdo");
        checkAnagram("mary", "army");
        checkAnagram("a", "a");
        checkAnagram("fill", "fil");
    }

    public static void checkAnagram(String inputStr1, String inputStr2){
        if(inputStr1.length() == inputStr2.length()){
            char[] charArr1 = inputStr1.toCharArray();
            char[] charArr2 = inputStr2.toCharArray();

            Arrays.sort(charArr1);
            Arrays.sort(charArr2);

            System.out.println(Arrays.equals(charArr1, charArr2));
        }
        else{
            System.out.println(false);
        }
    } 
}
