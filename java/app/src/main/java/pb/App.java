package pb;

import java.io.FileInputStream;
import java.io.IOException;
import org.lf.pbtutorial.Account;

public class App {
    private static void readFrom(String path) {
        try {
            FileInputStream fis = new FileInputStream(path);
            Account account = Account.parseFrom(fis);

            System.out.println(account);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("The program needs one argument!");
            return;
        }

        readFrom(args[0]);
    }
}
