package pb;

import java.io.FileInputStream;
import java.io.IOException;
import org.lf.pbtutorial.Account;

public class App {
    private static void readFrom(String path) {
        try {
            FileInputStream fis = new FileInputStream(path);
            Account message = Account.parseFrom(fis);

            System.out.println(message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("The program need one argument!");
            return;
        }

        readFrom(args[0]);   
    }
}
