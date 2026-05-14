public class Main {
    public static void main(String[] args){
        Movie SpiderMan = new Movie();
        SpiderMan.name = "SpiderMan";
        SpiderMan.realeaseYear = 2002;
        SpiderMan.totalMinutes = 121;

        SpiderMan.showDataSheet();
        SpiderMan.getRate(8);
        SpiderMan.getRate(5);
        SpiderMan.getRate(10);
        System.out.println(SpiderMan.rating);
        System.out.println(SpiderMan.totalRating);
        System.out.println(SpiderMan.getAvarageRate());
    }
}   