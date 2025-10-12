

import java.util.*;
class MinStack {
    Stack<Integer> s;
    Stack<Integer> min;

    public MinStack() {
        s=new Stack<Integer>();
        min=new Stack<Integer>();
    }
    
    public void push(int val) {
        s.push(val);
        if(min.isEmpty()||min.peek()>=val)
        {
            min.push(val);
        }
    }
    
    public void pop() {
        int x=s.pop();
        if(x==min.peek())
        {
            min.pop();
        }
        
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {

return min.peek();

        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */