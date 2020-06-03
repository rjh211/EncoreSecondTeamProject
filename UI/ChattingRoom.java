import javax.swing.*;
import java.awt.*;
import javax.swing.table.DefaultTableModel;



public class ChattingRoom extends JFrame {

	 private static final long serialVersionUID = 1L; //ChattingRoom ������ ���� �߰�. why?

	 JPanel Dong[] = new JPanel[2]; //���� => �ó������� ���� Miku ���� ���, RaspberryPi ���� ���.

     JTextField tf, t1, t2; // tf:������ �ó������� ���� �ؽ�Ʈ ��� // t1,t2: ���� ��ó(�ؽ�Ʈ)
     JTextPane pane;
     JComboBox<String> box; //String ���׸� �߰�
     JButton b1,b2,b3;
     JTable table;
     DefaultTableModel model;

    public ChattingRoom() {
        setLayout(null); //null���� �ְ� �Ǹ� Programmer�� ���� ��ġ��
        
        setTitle("Miku�� �Բ� �ϴ� HappyHappyLife"); // â title ����

        JPanel p1 = new JPanel();
        JPanel p2 = new JPanel(); //2���� �гΰ�ü ����

        p1.setBackground(Color.BLACK);
        p2.setBackground(Color.BLACK); //�г� ���� ��

        tf = new JTextField();
        t1 = new JTextField("Miku");
        t2 = new JTextField("RaspberryPI"); //�г� �Ʒ� ǥ���� �ؽ�Ʈ
        t1.setHorizontalAlignment(JTextField.CENTER);
        t2.setHorizontalAlignment(JTextField.CENTER);

        b1 = new JButton("�����Կ�"); //�����ư�� �����Կ� ��ư���� Ȱ��
        b2 = new JButton("����ݿ�"); //�ʴ��ư�� �����ν� ����ݿ� ��ư���� Ȱ��
        b3 = new JButton("����");

        pane = new JTextPane();
        box = new JComboBox<String>();

        p1.setBounds(20, 20, 750, 500);
        p2.setBounds(800, 20, 450, 450); //�г�ũ��. ���� ����

        tf.setBounds(30, 600, 720, 60); //�ؽ�Ʈ �Է�â or ���â?
        tf.setBackground(new Color(153,0,115));
        tf.setForeground(Color.WHITE);

        t1.setBounds(20, 530, 750, 30);
        t1.setBackground(new Color(255,192,203));
        t1.setForeground(Color.BLACK);
        t2.setBounds(800, 480, 450, 30); //�ؽ�Ʈ â ũ��
        t2.setBackground(new Color(255,192,203));
        t2.setForeground(Color.BLACK);
        
        pane.setBounds(20, 580, 750, 100);
        pane.setBackground(new Color(230,0,172));

        b1.setBounds(1010, 525, 240, 40);
        b1.setBackground(new Color(255, 51, 153));
        b1.setForeground(Color.white);
        b2.setBounds(1010, 580, 240, 40);
        b2.setBackground(new Color(255, 51, 153));
        b2.setForeground(Color.white);
        b3.setBounds(1010, 635, 240, 40); //��ư ũ��
        b3.setBackground(new Color(255, 51, 153)); //��ư ����
        b3.setForeground(Color.white); //���� ����
        
        Font font = new Font("YouandiModern HeadRegular", Font.BOLD, 25); // "YouandiModern HeadRegular" ����ü ���
        tf.setFont(font);
        t1.setFont(font);
        t2.setFont(font);
        b1.setFont(font);
        b2.setFont(font); 
        b3.setFont(font);
        
        add(p1);add(p2);
        add(t1);add(t2);
        add(tf);add(pane);add(box);
        add(b1);add(b2);add(b3);
        //��ġ

        setSize(1920,1080); //��ü Frame size
        setVisible(true); //�����츦 �����ش�
        getContentPane().setBackground(Color.PINK); //��ü Frame Background
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
    
    public static void main(String[] args) {
        new ChattingRoom();
    }

 }