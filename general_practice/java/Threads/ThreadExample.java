import java.io.*;

public class ThreadExample extends Thread {
    public void run()
    {
        System.out.print("Welcome to GeeksforGeeks.");
    }
    public static void main(String[] args)
    {
        ThreadExample t = new ThreadExample(); // creating thread
        t.start(); // starting thread
    }
}
