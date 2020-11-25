import game.Game;
import game.types.board.SiteType;
import game.util.graph.Vertex;
import util.AI;
import util.Context;
import util.Move;
import util.action.Action;

public class Solver extends AI {
    public Solver() {
        this.friendlyName = "SudokuSolver";
    }

    //-------------------------------------------------------------------------

    @Override
    public Move selectAction(Game game, Context context, double maxSeconds, int maxIterations, int maxDepth) {

        for (Vertex vertex : game.board().graph().vertices()) {
           // System.out.println(vertex.id());
        }

        return null;
    }

    @Override
    public void initAI(Game game, int playerID) {
        //Do nothing
    }
}
