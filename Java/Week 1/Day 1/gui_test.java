import javax.swing.JOptionPane;

public class gui_test {
    public static void main(String[] args) {
        String name = JOptionPane.showInputDialog(null, "enter your name: ");
        JOptionPane.showMessageDialog(null, "hello " + name);

    }
}
