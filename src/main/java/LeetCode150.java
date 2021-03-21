import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 * 150. 逆波兰表达式求值
 */
public class LeetCode150 {

    public int evalRPN(String[] tokens) {
        List<String> operators = Arrays.asList("+", "-", "*", "/");
        //+、-、*、/
        Stack<String> stack = new Stack<>();

        for (String token : tokens) {
            if (operators.contains(token)) {
                String num1 = stack.pop();
                String num2 = stack.pop();
                int i = Integer.parseInt(num1);
                int i1 = Integer.parseInt(num2);
                int sum = 0;
                if ("+".equals(token)) {
                    sum = i1 + i;
                }
                if ("-".equals(token)) {
                    sum = i1 - i;
                }
                if ("*".equals(token)) {
                    sum = i1 * i;
                }
                if ("/".equals(token)) {
                    sum = i1 / i;
                }
                stack.push(sum + "");
            } else {
                stack.push(token);
            }
        }
        return Integer.parseInt(stack.pop());
    }

    public static void main(String[] args) {
        String[] input = {"2", "1", "+", "3", "*"};
        LeetCode150 leetCode150 = new LeetCode150();
        System.out.println(leetCode150.evalRPN(input));
    }
}
