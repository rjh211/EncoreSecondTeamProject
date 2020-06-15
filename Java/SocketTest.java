package Test;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;


public class SocketTest {
	ServerSocket serverSocket  = null;
	Socket socket = null;
	BufferedReader in = null;
	PrintWriter out = null;
	
	public void Connect(int port){
		try {
			this.serverSocket = new ServerSocket(port);
			System.out.println("클라이언트 대기중");
			this.socket = this.serverSocket.accept();
			System.out.println("클라이언트 접속");
			
			this.in = new BufferedReader(new InputStreamReader(this.socket.getInputStream()));
			this.out = new PrintWriter(this.socket.getOutputStream(),true);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public String ReceiveFromRaspberry(){
		String rev = null;
		try {
			rev = this.in.readLine();		//라즈베리파이에서 온 변수 1~5
			//System.out.println(Integer.parseInt(rev));
			//System.out.println(rev);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return rev;
	}
	
	public void SendToRaspberry(String Msg){
		this.out.println(Msg);
		this.out.flush(); 
	}
	
	public void Disconnect(){
		try {
			this.serverSocket.close();
			this.socket.close();
			this.in.close();
			this.out.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void Base64toImage(String data){
		String base64Image = data;
		byte[] imageBytes = javax.xml.bind.DatatypeConverter.parseBase64Binary(base64Image);	//byte 배열로 이미지 받아옴
		String path = "C:\\Users\\JH\\Desktop\\playdata\\Java\\Java\\src\\Test\\test.jpg";		//저장할 위치(jpg로 저장)
		File file = new File(path); 
		try(OutputStream outputStream = new BufferedOutputStream(new FileOutputStream(file))) {
			outputStream.write(imageBytes);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void main(String... args) {
		SocketTest st = new SocketTest();
		st.Connect(9999);
		/*st.SendToRaspberry(st.ReceiveFromRaspberry());*/
		st.Base64toImage(st.ReceiveFromRaspberry());
		st.Disconnect();
	}
}
