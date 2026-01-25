public class q1 {

    public static void main(String[] args) {
        try {
            new q1().func();
        } catch (Throwable e) {
            System.out.println("An error occurred during execution: " + e.getMessage());
        }
    }
    
    public void func() throws Throwable {
        byte data = getDataFromSource();
        
        if (data > 0) {
            byte result = (byte) (data * 2);
            IO.writeLine("result: " + result); 
            
            if (result > 0) {
                IO.writeLine("The operation was successful.");
            }
        } else {
            IO.writeLine("No operation performed. Data must be positive.");
        }
    }
    
    private byte getDataFromSource() {
        return Byte.MAX_VALUE;
    }
}
