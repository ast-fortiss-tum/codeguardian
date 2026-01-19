// Source: Row 38 in ./dataset/CVEfixes/Analysis/results/Java/df_java_cwe_787.xlsx

package java.io;

public class FileOutputStream extends OutputStream {
  //   static {
  //     System.loadLibrary("natives");
  //   }

  private int fd;

  public FileOutputStream(FileDescriptor fd) {
    this.fd = fd.value;
  }

  public FileOutputStream(String path) throws IOException {
    this(path, false);
  }

  public FileOutputStream(String path, boolean append) throws IOException {
    fd = open(path, append);
  }
  

  public FileOutputStream(File file) throws IOException {
    this(file.getPath());
  }

  private static native int open(String path, boolean append) throws IOException;

  private static native void write(int fd, int c) throws IOException;

  private static native void write(int fd, byte[] b, int offset, int length)
    throws IOException;

  private static native void close(int fd) throws IOException;

  public void write(int c) throws IOException {
    write(fd, c);
  }

  public void write(byte[] b, int offset, int length) throws IOException {
    if (b == null) {
      throw new NullPointerException();
    }

    if (offset < 0 || offset + length > b.length) {
      throw new ArrayIndexOutOfBoundsException();
    }

    write(fd, b, offset, length);
  }

  public void close() throws IOException {
    if (fd != -1) {
      close(fd);
      fd = -1;
    }
  }
}
