public class AnimalTest {
    public static void main(String[] args){
        Dog dog = new Dog("Tucker", 3);
        Cat cat = new Cat("Lulu", 4);

        System.out.println(dog.getName() + " " + dog.makeNoise());
        System.out.println(cat.getName() + " " + cat.makeNoise());
        
        System.out.println(dog.favFood());
        System.out.println(dog.favToy());
        System.out.println(cat.favFood());
        System.out.println(cat.favToy());
    }
}
