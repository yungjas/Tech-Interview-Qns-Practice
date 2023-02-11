public class Cat extends Animal implements Habits{
    public Cat(String name, int age){
        super(name, age);
    }

    public String makeNoise(){
        return "meow";
    }

    public String favFood(){
        return "cat food";
    }

    public String favToy(){
        return "toy with string";
    }
}
