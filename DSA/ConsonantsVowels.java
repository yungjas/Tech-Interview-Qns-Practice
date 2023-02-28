import java.util.*;

public class ConsonantsVowels {
    public static void main(String[] args){
        count("aei");
        count("interview");
    }
    
    public static void count(String inputStr){
        int numVowels = 0;
        int numConsonants = 0;
        ArrayList<Character> vowels = new ArrayList<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        for(int i = 0; i < inputStr.length(); i++){
            if(vowels.contains(inputStr.charAt(i))){
                numVowels++;
            }
            else{
                numConsonants++;
            }
        }

        System.out.printf("%s = Vowels: %d, Consonants: %d\n", inputStr, numVowels, numConsonants);
    }
}
