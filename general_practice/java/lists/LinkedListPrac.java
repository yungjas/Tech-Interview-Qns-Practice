import java.util.*;

public class LinkedListPrac {
    public static void main(String[] args){
        LinkedList<String> ll = new LinkedList<>();

        // Adding elements to the linked list
        ll.add("A"); // adds to the end of the list
        ll.add("B");
        ll.addLast("C"); // adds to the beginning of the list
        ll.addFirst("D"); // adds to the first of the list
        ll.add(2, "E"); // adds to the 3rd position of the list
  
        System.out.println(ll);
    }
}
