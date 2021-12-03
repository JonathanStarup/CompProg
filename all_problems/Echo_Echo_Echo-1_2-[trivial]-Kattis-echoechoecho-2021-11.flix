// https://open.kattis.com/problems/echoechoecho
/// namespace EchoEchoEcho {
///     use List.repeat;
///     use String.unwords;

///     pub def solveProblem(readLine: Unit -> String & Impure, writeLine: String -> Unit & Impure): Unit & Impure =
///         let word = readLine();
///         let output = ???;//unwords(word |> repeat(3));
///         writeLine(output)
    
///     pub def solveTerminalProblem(): Unit & Impure =
///         use Console/StdIn.{readLine => optReadLine};
///         let rl = _ -> match optReadLine() {
///             case None => ???
///             case Some(line) => line
///         };
///         solveProblem(rl, println)

/// }

// remove `_` to run. `_` is used to avoid dublicate definition of main
def _main(_args: Array[String]): Int32 & Impure = 
    ??? as & Impure; ///EchoEchoEcho.solveTerminalProblem();
    0