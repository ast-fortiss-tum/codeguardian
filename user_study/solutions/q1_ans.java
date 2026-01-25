// Correct answer: CWE-190: Integer Overflow or Wraparound
// Source: from cwe-snippets, snippets_90/non-compliant/Java/cwe-0190/byte_max_multiply_01.java
/*
 * The Byte.MAX_VALUE in Java is 127, and when we attempt to multiply 127 by 2, the expected mathematical result is 254. 
 * However, due to the byte data type in Java being an 8-bit signed integer with a range from -128 to 127, 
 * this operation will lead to an overflow. When the result of the multiplication (254) is cast back to a byte, 
 * it will not fit within the byte range. 
 */


// Solution:
// The solution is to check if the multiplication by 2 would cause an overflow before performing the operation.
public void func() throws Throwable {
    byte data = Byte.MAX_VALUE;

    if (data > 0) {
        // Check if multiplication by 2 would cause overflow.
        if (data > Byte.MAX_VALUE / 2) {
            // Handle the potential overflow case.
            System.out.println("Warning: Operation would cause overflow.");
        } else {
            // Safe to perform the operation.
            byte result = (byte)(data * 2);
            IO.writeLine("result: " + result);
        }
    }
}
