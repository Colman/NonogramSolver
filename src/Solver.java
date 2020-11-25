import game.Game;
import util.AI;
import util.Context;
import util.Move;

public class Solver extends AI {
    /**
     * Constructor
     */
    public Solver() {
        this.friendlyName = "SudokuSolver";
    }

    //-------------------------------------------------------------------------

    @Override
    public Move selectAction(Game game, Context context, double maxSeconds, int maxIterations, int maxDepth) {

        return null;
    }

    @Override
    public void initAI(Game game, int playerID) {
    }
}
