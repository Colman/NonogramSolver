import game.Game;
import util.AI;
import util.Context;
import util.GameLoader;
import util.Trial;
import util.model.Model;

import java.util.ArrayList;

public class Main {
    static final String GAME_NAME = "Sudoku.lud";

    public static void main(String[] args) {
        Game game = GameLoader.loadGameFromName(GAME_NAME);

        final Trial trial = new Trial(game);
        final Context context = new Context(game, trial);

        final ArrayList<AI> ais = new ArrayList<AI>();
        ais.add(null);
        ais.add(new Solver());

        game.start(context);

        ais.get(1).initAI(game, 1);

        Model model = context.model();
        while (!context.trial().over()) {
            model.startNewStep(context, ais, 1.0);
        }

        System.out.println("Outcome = " + context.trial().status());
    }
}
