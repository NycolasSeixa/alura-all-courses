package br.com.alura.screenmatch.models;

public class Title {
    private String name;
    private int realeaseYear;
    private boolean includedInPlan;
    private double rating;
    private int totalRating;
    private int totalMinutes;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getRealeaseYear() {
        return realeaseYear;
    }

    public void setRealeaseYear(int realeaseYear) {
        this.realeaseYear = realeaseYear;
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    public int getTotalRating() {
        return totalRating;
    }

    public void setTotalRating(int totalRating) {
        this.totalRating = totalRating;
    }

    public int getTotalMinutes() {
        return totalMinutes;
    }

    public void setTotalMinutes(int totalMinutes) {
        this.totalMinutes = totalMinutes;
    }

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

    public boolean isIncludedInPlan() {
        return includedInPlan;
    }

    public void setIncludedInPlan(boolean includedInPlan) {
        this.includedInPlan = includedInPlan;
    }
}
