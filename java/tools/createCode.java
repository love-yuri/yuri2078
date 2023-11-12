import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.*;

public class createCode {
  private static final int WIDTH = 200; // 图片宽度
  private static final int HEIGHT = 80; // 图片高度
  private static final int FONT_SIZE = 30; // 字体大小
  private static final String CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"; // 验证码字符集

  public static void main(String[] args) {
    BufferedImage image = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
    Graphics2D g2d = image.createGraphics();

    // 设置背景颜色为白色
    g2d.setColor(Color.WHITE);
    g2d.fillRect(0, 0, WIDTH, HEIGHT);

    // 添加干扰元素到背景中（随机绘制100个点）
    for (int i = 0; i < 100; i++) {
      int xPosition = (int) (Math.random() * WIDTH);
      int yPosition = (int) (Math.random() * HEIGHT);
      Color color = getRandomColor();
      g2d.setColor(color);
      g2d.setFont(new Font("", 0, 34));
      g2d.drawRect(xPosition, yPosition, 1, 1);
    }


    // 在图像上绘制随机字符串作为验证码
    for (int i = 0; i < 6; i++) { // 这里假设验证码长度为6个字符
      char character = getRandomCharacter();

      int xPosition = (i * (WIDTH / 7)) + (WIDTH / 14);
      int yPosition = (HEIGHT / 2) + (FONT_SIZE / 3);

      Color color = getRandomColor();
      g2d.setColor(color);

      // 使用不同颜色绘制每个字符
      g2d.drawString(Character.toString(character), xPosition, yPosition);
    }

    for(int i = 0; i < 15; i++) {
      Color color = getRandomColor();
      g2d.setColor(color);
      g2d.drawLine(random(WIDTH), random(HEIGHT), random(WIDTH), random(HEIGHT));
    }

    g2d.dispose(); // 清理图形上下文使用的系统资源

    try {
      File outputImage = new File("captcha.jpg"); // 保存生成的验证码图片
      ImageIO.write(image, "jpg", outputImage);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static int random(int manNum) {
    return (int) (Math.random() * manNum);
  }

  private static char getRandomCharacter() {
    int randomIndex = (int) (Math.random() * CHARACTERS.length());
    return CHARACTERS.charAt(randomIndex);
  }

  private static Color getRandomColor() {
    int red = (int) (Math.random() * 256);
    int green = (int) (Math.random() * 256);
    int blue = (int) (Math.random() * 256);
    return new Color(red, green, blue);
  }
}
