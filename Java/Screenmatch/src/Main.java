import br.com.alura.screenmatch.calculations.TimeCalculator;
import br.com.alura.screenmatch.models.Serie;


public class Main {
    public static void main(String[] args){
        
        Serie Lost = new Serie();
        Lost.setName("Lost");
        Lost.setRealeaseYear(2000);
        Lost.setEpsPerSeason(10);
        Lost.setSeasons(10);
        Lost.showDataSheet();
        Lost.setEpsPerSeason(10);
        Lost.setMinutesPerEp(50);
        System.out.println(Lost.getTotalMinutes());

        TimeCalculator timer = new TimeCalculator();
        // timer.addMovie(m);
    }
}   