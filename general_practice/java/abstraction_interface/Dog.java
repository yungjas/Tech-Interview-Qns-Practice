public class Dog extends Animal implements Habits{
    public Dog(String name, int age){
        super(name, age);
    }

    public String makeNoise(){
        return "woof";
    }

    public String favFood(){
        return "dog food";
    }

    public String favToy(){
        return "stick";
    }
}
