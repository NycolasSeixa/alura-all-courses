public class Movie {
    String name;
    int realeaseYear;
    boolean includedInPlan;
    double rating;
    int totalRating;
    int totalMinutes;

    void showDataSheet(){
        System.out.println("Movie: " + name);
        System.out.println("Realease Year: " + realeaseYear);
    }

    void getRate(double rate){
        rating += rate;
        totalRating++;
    }

    double getAvarageRate() {
        return rating / totalRating;
    }
}