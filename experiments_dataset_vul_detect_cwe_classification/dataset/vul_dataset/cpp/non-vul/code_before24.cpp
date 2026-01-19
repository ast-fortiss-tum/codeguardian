// Source: Row 1878 in ./dataset/CVEfixes/Analysis/results/C++/df_cpp_all.xlsx

FdOutStream::FdOutStream(int fd_, bool blocking_, int timeoutms_, size_t bufSize_)
  : fd(fd_), blocking(blocking_), timeoutms(timeoutms_),
    bufSize(bufSize_ ? bufSize_ : DEFAULT_BUF_SIZE), offset(0)
{
  ptr = start = sentUpTo = new U8[bufSize];
  end = start + bufSize;

  gettimeofday(&lastWrite, NULL);
}

