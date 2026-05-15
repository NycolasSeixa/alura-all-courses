package br.com.alura.screenmatch.models;

public class Movie {
    public String name;
    public int realeaseYear;
    boolean includedInPlan;
    private double rating;
    private int totalRating;
    public int totalMinutes;

    public int getTotalRate(){
        return totalRating;
    }

    public void showDataSheet(){
        System.out.println("Movie: " + name);
        System.out.println("Realease Year: " + realeaseYear);
    }

    public void getRate(double rate){
        rating += rate;
        totalRating++;
    }

    public double getAvarageRate() {
        return rating / totalRating;
    }
}