import javax.swing.*;
import java.awt.*;
import javax.swing.table.DefaultTableModel;



public class ChattingRoom extends JFrame {

	 private static final long serialVersionUID = 1L; //ChattingRoom 에러로 강제 추가. why?

	 JPanel Dong[] = new JPanel[2]; //영상 => 시나리오에 따른 Miku 영상 출력, RaspberryPi 영상 출력.

     JTextField tf, t1, t2; // tf:정해진 시나리오에 따라 텍스트 출력 // t1,t2: 영상 출처(텍스트)
     JTextPane pane;
     JComboBox<String> box; //String 제네릭 추가
     JButton b1,b2,b3;
     JTable table;
     DefaultTableModel model;

    public ChattingRoom() {
        setLayout(null); //null값을 주게 되면 Programmer가 직접 배치함
        
        setTitle("Miku와 함께 하는 HappyHappyLife"); // 창 title 설정

        JPanel p1 = new JPanel();
        JPanel p2 = new JPanel(); //2개의 패널객체 생성

        p1.setBackground(Color.BLACK);
        p2.setBackground(Color.BLACK); //패널 색상 블랙

        tf = new JTextField();
        t1 = new JTextField("Miku");
        t2 = new JTextField("RaspberryPI"); //패널 아래 표현할 텍스트
        t1.setHorizontalAlignment(JTextField.CENTER);
        t2.setHorizontalAlignment(JTextField.CENTER);

        b1 = new JButton("사진촬영"); //강퇴버튼을 사진촬영 버튼으로 활용
        b2 = new JButton("결과반영"); //초대버튼을 영상인식 결과반영 버튼으로 활용
        b3 = new JButton("종료");

        pane = new JTextPane();
        box = new JComboBox<String>();

        p1.setBounds(20, 20, 750, 500);
        p2.setBounds(800, 20, 450, 450); //패널크기. 추후 수정

        tf.setBounds(30, 600, 720, 60); //텍스트 입력창 or 출력창?
        tf.setBackground(new Color(153,0,115));
        tf.setForeground(Color.WHITE);

        t1.setBounds(20, 530, 750, 30);
        t1.setBackground(new Color(255,192,203));
        t1.setForeground(Color.BLACK);
        t2.setBounds(800, 480, 450, 30); //텍스트 창 크기
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
        b3.setBounds(1010, 635, 240, 40); //버튼 크기
        b3.setBackground(new Color(255, 51, 153)); //버튼 색깔
        b3.setForeground(Color.white); //글자 색깔
        
        Font font = new Font("YouandiModern HeadRegular", Font.BOLD, 25); // "YouandiModern HeadRegular" 글자체 사용
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
        //배치

        setSize(1920,1080); //전체 Frame size
        setVisible(true); //윈도우를 보여준다
        getContentPane().setBackground(Color.PINK); //전체 Frame Background
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
    
    public static void main(String[] args) {
        new ChattingRoom();
    }

 }